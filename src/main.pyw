import sys
import json
import requests
from typing import TypedDict
from pathlib import Path
from typing import Literal

from PySide6.QtCore import QProcess, QSettings, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem,
    QPushButton, QLineEdit, QTableWidget, QRadioButton, QMessageBox
)

from ui.main_window_ui import Ui_MainWindow
from pyinstaller_command_generator import generate_pyinstaller_command


CURRENT_VERSION = "v1.0.0"
UPDATE_URL = "https://api.github.com/repos/riteshkarmakar/py-to-exe-converter/releases/latest"
DOCUMENTATION_URL = "https://github.com/riteshkarmakar/py-to-exe-converter"

class BuildConfig(TypedDict):
    script_path: str
    noconfirm: bool
    icon_path: str
    version_file_path: str
    one_file: bool
    windowed: bool
    additional_data: list[tuple[str, str]]
    distpath: str
    workpath: str
    specpath: str
    name: str
    contents_dir: str
    manual_args: str


class AppConfig(TypedDict):
    build_config: BuildConfig
    working_dir: str
    manual_args: str


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.init_signals_slots()
        self.show()
        if self.action_auto_update_check.isChecked():
            self.check_for_updates()

    def init_ui(self) -> None:
        self.setGeometry(300, 60, 950, 700)
        self.tableWidget.setColumnWidth(0, 200)
        self.settings = QSettings("Ritesh Karmakar", "Py to Exe Converter")
        self.action_auto_update_check.setChecked(self.settings.value("auto_update_check", True, type=bool))
        self.process = None
        self.command_lst = ""
        self.build_config: BuildConfig = {
            "script_path": "",
            "noconfirm": True,
            "icon_path": "",
            "version_file_path": "",
            "one_file": False,
            "windowed": False,
            "additional_data": [],
            "distpath": "",
            "workpath": "",
            "specpath": "",
            "name": "",
            "contents_dir": "",
            "manual_args": "",
        }
        self.widget_config_map = {
            self.lineEdit_script: "script_path",
            self.lineEdit_icon: "icon_path",
            self.lineEdit_version: "version_file_path",
            self.radioBtn_one_file: "one_file",
            self.radioBtn_windowed: "windowed",
            self.tableWidget: "additional_data",
            self.lineEdit_distpath: "distpath",
            self.lineEdit_workpath: "workpath",
            self.lineEdit_specpath: "specpath",
            self.lineEdit_name: "name",
            self.lineEdit_contents_dir: "contents_dir",
            self.lineEdit_manual_args: "manual_args",
        }

    def init_signals_slots(self) -> None:
        for btn in self.tabWidget.findChildren(QPushButton):
            btn.clicked.connect(self.handle_btns)

        for widget, key in self.widget_config_map.items():
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(lambda text, key=key: self.update_config_and_command(key, text))
            if isinstance(widget, QRadioButton):
                widget.toggled.connect(lambda checked, key=key: self.update_config_and_command(key, checked))
            if isinstance(widget, QTableWidget):
                widget.cellChanged.connect(self.handle_table_change)

        self.action_exit.triggered.connect(lambda: QApplication.exit(0))
        self.action_auto_update_check.toggled.connect(lambda checked: self.settings.setValue("auto_update_check", checked))
        self.action_read_documentation.triggered.connect(lambda: QDesktopServices.openUrl(QUrl(DOCUMENTATION_URL)))
        self.action_check_for_updates.triggered.connect(self.check_for_updates)
        self.action_import_config.triggered.connect(self.import_config)
        self.action_export_config.triggered.connect(self.export_config)
        self.action_clear.triggered.connect(self.clear_all_fields)
        self.action_run.triggered.connect(self.run_command)

    def check_for_updates(self) -> None:
        try:
            response = None
            response = requests.get(UPDATE_URL)
            response.raise_for_status()
        except:
            if self.sender() != self.action_check_for_updates:
                return
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Update Check Failed!")
            msg.setText("Unable to fetch update information.")
            msg.setInformativeText("Please check your internet connection or try again later.")
            msg.setDetailedText(f"Error code: {response.status_code if response != None else "None"}\nURL: {UPDATE_URL}")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        release_data = response.json()
        latest_version = release_data["tag_name"]
        release_page_url = release_data["html_url"]
        download_url = release_data["assets"][0]["browser_download_url"]
        
        if latest_version > CURRENT_VERSION:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Update Available")
            msg.setText(
                f"<h3>A New Version ({latest_version}) is Available!</h3>"
                f"To learn more about what's new, click 'View Details' below.</p>"
            )
            msg.setInformativeText("Would you like to update now?")
            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Help | QMessageBox.StandardButton.Cancel
            )
            msg.button(QMessageBox.StandardButton.Help).setText("View Details")
            
            # Open the download URL or View Details
            result = msg.exec()
            if result == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl(download_url))
            elif result == QMessageBox.StandardButton.Help:
                QDesktopServices.openUrl(QUrl(release_page_url))

        else:
            if self.sender() == self.action_check_for_updates:
                QMessageBox.information(
                    self, "No Update Available", f"You are currently using the latest version ({CURRENT_VERSION})"
                )

    def handle_btns(self) -> None:
        btn = self.sender()
        match btn:
            case self.btn_script:
                script_path, _ = QFileDialog.getOpenFileName(self, "Select Python File", filter="Python File (*.py; *.pyw)")
                if script_path:
                    self.lineEdit_script.setText(script_path)

            case self.btn_icon:
                icon_path, _ = QFileDialog.getOpenFileName(self, "Select Icon File", filter="Icon File (*.ico)")
                if icon_path:
                    self.lineEdit_icon.setText(icon_path)

            case self.btn_version:
                version_file_path, _ = QFileDialog.getOpenFileName(self, "Select Version File", filter="Text File (*.txt)")
                if version_file_path:
                    self.lineEdit_version.setText(version_file_path)

            case self.btn_working_dir:
                working_dir = QFileDialog.getExistingDirectory(self, "Select a Folder")
                if working_dir:
                    self.lineEdit_working_dir.setText(working_dir)

            case self.btn_distpath:
                dist_dir = QFileDialog.getExistingDirectory(self, "Select a Folder")
                if dist_dir:
                    self.lineEdit_distpath.setText(dist_dir)

            case self.btn_workpath:
                work_dir = QFileDialog.getExistingDirectory(self, "Select a Folder")
                if work_dir:
                    self.lineEdit_workpath.setText(work_dir)

            case self.btn_specpath:
                spec_dir = QFileDialog.getExistingDirectory(self, "Select a Folder")
                if spec_dir:
                    self.lineEdit_specpath.setText(spec_dir)

            case self.btn_add_files:
                self.tableWidget.blockSignals(True)

                row_count = self.tableWidget.rowCount()
                paths, _ = QFileDialog.getOpenFileNames(self, "Select Files")
                alreaded_added_files = [self.tableWidget.item(i, 0).text() for i in range(row_count)]
                for path in paths:
                    if path not in alreaded_added_files:
                        self.tableWidget.insertRow(row_count)
                        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(path))
                        self.tableWidget.setItem(row_count, 1, QTableWidgetItem("."))
                        row_count += 1
                
                self.handle_table_change()
                self.tableWidget.blockSignals(False)

            case self.btn_add_folder:
                self.tableWidget.blockSignals(True)

                row_count = self.tableWidget.rowCount()
                path = QFileDialog.getExistingDirectory(self, "Select a Folder")
                alreaded_added_files = [self.tableWidget.item(i, 0).text() for i in range(row_count)]
                if path and path not in alreaded_added_files:
                    self.tableWidget.insertRow(row_count)
                    self.tableWidget.setItem(row_count, 0, QTableWidgetItem(path))
                    self.tableWidget.setItem(row_count, 1, QTableWidgetItem(path.split("/")[-1] + "/"))
                    row_count += 1

                self.handle_table_change()
                self.tableWidget.blockSignals(False)

            case self.btn_remove:
                self.tableWidget.blockSignals(True)

                row = self.tableWidget.currentRow()
                if row != -1:
                    self.tableWidget.removeRow(row)

                self.handle_table_change()
                self.tableWidget.blockSignals(False)

    def clear_all_fields(self) -> None:
        if QMessageBox.warning(
            self, "Clear All Fields", "Are you sure you want to clear all fields?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        ) != QMessageBox.StandardButton.Yes:
            return

        for lineedit in self.centralwidget.findChildren(QLineEdit):
            lineedit.clear()
        self.radioBtn_one_directory.setChecked(True)
        self.radioBtn_console.setChecked(True)
        self.tableWidget.setRowCount(0)
        self.textEdit_log.clear()
        self.textEdit_current_command.clear()

    def handle_table_change(self) -> list[tuple[str, str]]:
        data = []
        for row in range(self.tableWidget.rowCount()):
            data.append((self.tableWidget.item(row, 0).text(), self.tableWidget.item(row, 1).text()))

        self.update_config_and_command("additional_data", data)

    def update_config_and_command(self, key: str, value: str | bool) -> None:
        self.build_config[key] = value
        self.command_lst, command_text = generate_pyinstaller_command(**self.build_config)
        self.textEdit_current_command.setText(command_text)

        if key == "script_path":
            # Automatically set working directory based on script location.
            # If the script is inside a 'src' folder, go one level up — likely the project root.
            # Otherwise, use the script's parent directory.
            script_path = Path(value)
            if script_path.parent.name == "src":
                self.lineEdit_working_dir.setText(script_path.parent.parent.as_posix())
            else:
                self.lineEdit_working_dir.setText(script_path.parent.as_posix())

    def import_config(self) -> None:
        self.tableWidget.blockSignals(True)

        config_path, _ = QFileDialog.getOpenFileName(self, "Import Config", "Saved Configs", "JSON File (*.json)")
        if config_path:
            try:
                with open(config_path) as f:
                    app_config: AppConfig = json.load(f)
            
                self.build_config: BuildConfig = app_config["build_config"]
                self.lineEdit_working_dir.setText(app_config["working_dir"])
                self.lineEdit_manual_args.setText(app_config["manual_args"])

                for widget, key in self.widget_config_map.items():
                    if isinstance(widget, QLineEdit):
                        widget.setText(self.build_config[key])
                    elif isinstance(widget, QRadioButton):
                        widget.setChecked(self.build_config[key])
                    elif widget == self.tableWidget:
                        self.tableWidget.setRowCount(0)
                        table_data = self.build_config[key]
                        self.tableWidget.setRowCount(len(table_data))
                        for r, row_data in enumerate(table_data):
                            self.tableWidget.setItem(r, 0, QTableWidgetItem(row_data[0]))
                            self.tableWidget.setItem(r, 1, QTableWidgetItem(row_data[1]))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{repr(e)}")
                raise
            
            self.handle_table_change()

        self.tableWidget.blockSignals(False)

    def export_config(self) -> None:
        Path("Saved Configs").mkdir(exist_ok=True)
        config_path, _ = QFileDialog.getSaveFileName(self, "Export Config", "Saved Configs", "JSON File (*.json)")
        if config_path:
            app_config: AppConfig = {
                "build_config": self.build_config,
                "working_dir": self.lineEdit_working_dir.text().strip(),
                "manual_args": self.lineEdit_manual_args.text().strip(),
            }
            with open(config_path, "w") as f:
                json.dump(app_config, f, indent="\t")

    def log(self, message: str, color: Literal["black", "grey", "red", "green", "blue", "yellow", "orange"] = "black"):
        self.textEdit_log.append(f"<span style='color: {color}'>" + message.strip().replace("\n", "<br>") + "</span>")

    def run_command(self) -> None:
        if self.process is not None:
            return
        
        if not self.build_config["script_path"]:
            self.tabWidget.setCurrentIndex(0)
            QMessageBox.warning(self, "Missing Script", "Please select a Python script to convert before building the executable.")
            return
        
        working_dir = self.lineEdit_working_dir.text().strip()
        working_dir_path = Path(working_dir)
        if not working_dir or not working_dir_path.is_dir():
            self.tabWidget.setCurrentIndex(2)
            QMessageBox.warning(self, "Invalid Directory", "The working directory you entered does not exist or is not a folder.")
            return
        
        self.textEdit_log.clear()

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.errorOccurred.connect(self.handle_process_error)
        self.process.finished.connect(self.handle_process_finished)

        self.process.setWorkingDirectory(working_dir)
        self.process.start(self.command_lst[0], self.command_lst[1:])

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.log(stdout)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.log(stderr)

    def handle_process_error(self, error):
        error_map = {
            QProcess.FailedToStart: "Failed to start. The executable might be missing or not accessible.",
            QProcess.Crashed: "The process crashed.",
            QProcess.Timedout: "The process timed out.",
            QProcess.WriteError: "An error occurred when attempting to write to the process.",
            QProcess.ReadError: "An error occurred when attempting to read from the process.",
            QProcess.UnknownError: "An unknown error occurred."
        }
        error_message = error_map.get(error, "An unexpected error occurred.")
        self.log(f"[Error] {error_message}", color="red")

        self.process.close()
        self.process = None

    def handle_process_finished(self, exitCode, exitStatus):
        self.log(f"[Finished] Exit code: {exitCode}, Status: {exitStatus}", color="green" if exitCode == 0 else "red")
        self.process = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")
    window = MainWindow()
    sys.exit(app.exec())
