# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 712)
        icon = QIcon()
        icon.addFile(u":/ui/icons/app-icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action_run = QAction(MainWindow)
        self.action_run.setObjectName(u"action_run")
        icon1 = QIcon()
        icon1.addFile(u":/ui/icons/powershell.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_run.setIcon(icon1)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon2 = QIcon()
        icon2.addFile(u":/ui/icons/clear.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_clear.setIcon(icon2)
        self.action_import_config = QAction(MainWindow)
        self.action_import_config.setObjectName(u"action_import_config")
        icon3 = QIcon()
        icon3.addFile(u":/ui/icons/import_config.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_import_config.setIcon(icon3)
        self.action_export_config = QAction(MainWindow)
        self.action_export_config.setObjectName(u"action_export_config")
        icon4 = QIcon()
        icon4.addFile(u":/ui/icons/export_config.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_export_config.setIcon(icon4)
        self.action_check_for_updates = QAction(MainWindow)
        self.action_check_for_updates.setObjectName(u"action_check_for_updates")
        self.action_auto_update_check = QAction(MainWindow)
        self.action_auto_update_check.setObjectName(u"action_auto_update_check")
        self.action_auto_update_check.setCheckable(True)
        self.action_read_documentation = QAction(MainWindow)
        self.action_read_documentation.setObjectName(u"action_read_documentation")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioBtn_console = QRadioButton(self.groupBox_2)
        self.radioBtn_console.setObjectName(u"radioBtn_console")
        self.radioBtn_console.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioBtn_console)

        self.radioBtn_windowed = QRadioButton(self.groupBox_2)
        self.radioBtn_windowed.setObjectName(u"radioBtn_windowed")

        self.horizontalLayout_2.addWidget(self.radioBtn_windowed)


        self.gridLayout_2.addWidget(self.groupBox_2, 4, 0, 1, 2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioBtn_one_directory = QRadioButton(self.groupBox)
        self.radioBtn_one_directory.setObjectName(u"radioBtn_one_directory")
        self.radioBtn_one_directory.setChecked(True)

        self.horizontalLayout.addWidget(self.radioBtn_one_directory)

        self.radioBtn_one_file = QRadioButton(self.groupBox)
        self.radioBtn_one_file.setObjectName(u"radioBtn_one_file")

        self.horizontalLayout.addWidget(self.radioBtn_one_file)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_script = QLineEdit(self.tab)
        self.lineEdit_script.setObjectName(u"lineEdit_script")
        self.lineEdit_script.setReadOnly(False)
        self.lineEdit_script.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_script, 1, 0, 1, 1)

        self.btn_script = QPushButton(self.tab)
        self.btn_script.setObjectName(u"btn_script")

        self.gridLayout_3.addWidget(self.btn_script, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_icon = QLineEdit(self.tab)
        self.lineEdit_icon.setObjectName(u"lineEdit_icon")
        self.lineEdit_icon.setReadOnly(False)
        self.lineEdit_icon.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineEdit_icon, 1, 0, 1, 1)

        self.btn_icon = QPushButton(self.tab)
        self.btn_icon.setObjectName(u"btn_icon")

        self.gridLayout_4.addWidget(self.btn_icon, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_version = QLineEdit(self.tab)
        self.lineEdit_version.setObjectName(u"lineEdit_version")
        self.lineEdit_version.setReadOnly(False)
        self.lineEdit_version.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lineEdit_version, 1, 0, 1, 1)

        self.btn_version = QPushButton(self.tab)
        self.btn_version.setObjectName(u"btn_version")

        self.gridLayout_5.addWidget(self.btn_version, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 2, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 5, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_add_files = QPushButton(self.tab_2)
        self.btn_add_files.setObjectName(u"btn_add_files")

        self.gridLayout.addWidget(self.btn_add_files, 0, 0, 1, 1)

        self.btn_add_folder = QPushButton(self.tab_2)
        self.btn_add_folder.setObjectName(u"btn_add_folder")

        self.gridLayout.addWidget(self.btn_add_folder, 0, 1, 1, 1)

        self.btn_remove = QPushButton(self.tab_2)
        self.btn_remove.setObjectName(u"btn_remove")

        self.gridLayout.addWidget(self.btn_remove, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 150))
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_working_dir = QLineEdit(self.tab_3)
        self.lineEdit_working_dir.setObjectName(u"lineEdit_working_dir")
        self.lineEdit_working_dir.setReadOnly(False)
        self.lineEdit_working_dir.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_working_dir, 1, 0, 1, 1)

        self.btn_working_dir = QPushButton(self.tab_3)
        self.btn_working_dir.setObjectName(u"btn_working_dir")

        self.gridLayout_6.addWidget(self.btn_working_dir, 1, 1, 1, 1)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_distpath = QLineEdit(self.tab_3)
        self.lineEdit_distpath.setObjectName(u"lineEdit_distpath")
        self.lineEdit_distpath.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.lineEdit_distpath, 1, 0, 1, 1)

        self.btn_distpath = QPushButton(self.tab_3)
        self.btn_distpath.setObjectName(u"btn_distpath")

        self.gridLayout_7.addWidget(self.btn_distpath, 1, 1, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_workpath = QLineEdit(self.tab_3)
        self.lineEdit_workpath.setObjectName(u"lineEdit_workpath")
        self.lineEdit_workpath.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.lineEdit_workpath, 1, 0, 1, 1)

        self.btn_workpath = QPushButton(self.tab_3)
        self.btn_workpath.setObjectName(u"btn_workpath")

        self.gridLayout_8.addWidget(self.btn_workpath, 1, 1, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_specpath = QLineEdit(self.tab_3)
        self.lineEdit_specpath.setObjectName(u"lineEdit_specpath")
        self.lineEdit_specpath.setReadOnly(False)
        self.lineEdit_specpath.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.lineEdit_specpath, 1, 0, 1, 1)

        self.btn_specpath = QPushButton(self.tab_3)
        self.btn_specpath.setObjectName(u"btn_specpath")

        self.gridLayout_9.addWidget(self.btn_specpath, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lineEdit_name = QLineEdit(self.tab_3)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit_name)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.lineEdit_contents_dir = QLineEdit(self.tab_3)
        self.lineEdit_contents_dir.setObjectName(u"lineEdit_contents_dir")
        self.lineEdit_contents_dir.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.lineEdit_contents_dir)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(208, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.lineEdit_manual_args = QLineEdit(self.centralwidget)
        self.lineEdit_manual_args.setObjectName(u"lineEdit_manual_args")
        self.lineEdit_manual_args.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_manual_args)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.textEdit_current_command = QTextEdit(self.centralwidget)
        self.textEdit_current_command.setObjectName(u"textEdit_current_command")
        self.textEdit_current_command.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit_current_command)

        self.copyright_label = QLabel(self.centralwidget)
        self.copyright_label.setObjectName(u"copyright_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyright_label.sizePolicy().hasHeightForWidth())
        self.copyright_label.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.copyright_label)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_log = QTextEdit(self.groupBox_3)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit_log)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalLayout_5.setStretch(0, 3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(40, 40))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 950, 26))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar.addAction(self.action_run)
        self.toolBar.addAction(self.action_clear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_import_config)
        self.toolBar.addAction(self.action_export_config)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_read_documentation)
        self.menuHelp.addAction(self.action_check_for_updates)
        self.menuSettings.addAction(self.action_import_config)
        self.menuSettings.addAction(self.action_export_config)
        self.menuSettings.addAction(self.action_auto_update_check)
        self.menuFile.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Py to Exe Converter", None))
        self.action_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.action_import_config.setText(QCoreApplication.translate("MainWindow", u"Import Config", None))
        self.action_export_config.setText(QCoreApplication.translate("MainWindow", u"Export Config", None))
        self.action_check_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates...", None))
        self.action_auto_update_check.setText(QCoreApplication.translate("MainWindow", u"Auto Update Check at Startup", None))
#if QT_CONFIG(tooltip)
        self.action_auto_update_check.setToolTip(QCoreApplication.translate("MainWindow", u"Auto Update Check at Startup", None))
#endif // QT_CONFIG(tooltip)
        self.action_read_documentation.setText(QCoreApplication.translate("MainWindow", u"Read Documentation", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"(--console / --windowed)", None))
#if QT_CONFIG(tooltip)
        self.radioBtn_console.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Open a console window for standard i/o (default).</p><p>On Windows this option has no effect if the first script is a \u2018.pyw\u2019 file.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioBtn_console.setText(QCoreApplication.translate("MainWindow", u"Console Based", None))
#if QT_CONFIG(tooltip)
        self.radioBtn_windowed.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Windows and macOS: do not provide a console window for standard i/o.</p><p>On macOS this also triggers building a macOS .app bundle.</p><p>On Windows this option is automatically set if the first script is a \u2018.pyw\u2019 file. This option is ignored on *NIX systems.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioBtn_windowed.setText(QCoreApplication.translate("MainWindow", u"Window Based (hide the console)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"(--onedir / --onefile)", None))
#if QT_CONFIG(tooltip)
        self.radioBtn_one_directory.setToolTip(QCoreApplication.translate("MainWindow", u"Create a one-folder bundle containing an executable (default).", None))
#endif // QT_CONFIG(tooltip)
        self.radioBtn_one_directory.setText(QCoreApplication.translate("MainWindow", u"One Directory", None))
#if QT_CONFIG(tooltip)
        self.radioBtn_one_file.setToolTip(QCoreApplication.translate("MainWindow", u"Create a one-file bundled executable.", None))
#endif // QT_CONFIG(tooltip)
        self.radioBtn_one_file.setText(QCoreApplication.translate("MainWindow", u"One File", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"Path of the python script to be processed.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Script Location:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_script.setToolTip(QCoreApplication.translate("MainWindow", u"Path of the python script to be processed.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_script.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Path to the icon file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Icon Location (--icon):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_icon.setToolTip(QCoreApplication.translate("MainWindow", u"Path to the icon file.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_icon.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"Add a version resource from FILE to the exe.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Version File Location (--version-file):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_version.setToolTip(QCoreApplication.translate("MainWindow", u"Add a version resource from FILE to the exe.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_version.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General Options", None))
        self.btn_add_files.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.btn_add_folder.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Additional data files or directories containing data files to be added to the application.</p><p>To put a file in the top-level application directory, use . as destination.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Additional Files", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_working_dir.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Set the working directory where the PyInstaller command will run.</p><p>This is useful if your script or related files are in a specific folder.</p><p>Equivalent to running the command after a 'cd' into that directory.</p><p>Note: If your script is inside a 'src' folder, the directory one level above 'src' is auto-selected as the working directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_working_dir.setPlaceholderText("")
        self.btn_working_dir.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Set the working directory where the PyInstaller command will run.</p><p>This is useful if your script or related files are in a specific folder.</p><p>Equivalent to running the command after a 'cd' into that directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Working Directory:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_distpath.setToolTip(QCoreApplication.translate("MainWindow", u"Where to put the bundled app (default: ./dist)", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_distpath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./dist", None))
        self.btn_distpath.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"Where to put the bundled app (default: ./dist)", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bundled App Output Folder (--distpath):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_workpath.setToolTip(QCoreApplication.translate("MainWindow", u"Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_workpath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./build", None))
        self.btn_workpath.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Temporary Build Files Folder (--workpath):", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("MainWindow", u"Folder to store the generated spec file (default: current directory)", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Spec File Output Folder (--specpath):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_specpath.setToolTip(QCoreApplication.translate("MainWindow", u"Folder to store the generated spec file (default: current directory)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_specpath.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Name to assign to the bundled app and spec file (default: first script\u2019s basename).", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name (--name):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_name.setToolTip(QCoreApplication.translate("MainWindow", u"Name to assign to the bundled app and spec file (default: first script\u2019s basename).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>For onedir builds only, specify the name of the directory in which all supporting files (i.e. everything except the executable itself) will be placed in.</p><p>Use \u201c.\u201d to re-enable old onedir layout without contents directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contents Directory (--contents-directory):", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_contents_dir.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>For onedir builds only, specify the name of the directory in which all supporting files (i.e. everything except the executable itself) will be placed in.</p><p>Use \u201c.\u201d to re-enable old onedir layout without contents directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Build Paths", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Manual Argument Input:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_manual_args.setToolTip(QCoreApplication.translate("MainWindow", u"Manual arguments must be in the format: --option \"value\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current Command:", None))
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ritesh karmakar\n"
"riteshkarmakar7407@gmail.com", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

