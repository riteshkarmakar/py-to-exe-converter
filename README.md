
<div align="center">
  <h1>Py to Exe Converter GUI</h1>

  <p align="justify">
    A user-friendly graphical interface built with Python and PySide6 to convert your Python (.py) scripts into standalone Windows executables (.exe) using the power of PyInstaller.
  </p>

  <picture>
    <img src=".github/main_window.png">
  </picture>
</div>

## Features

- Easy-to-use graphical interface.
- Select script location, icon file, and version file via file dialogs.
- Choose between creating a single directory (`--onedir`) or a single file (`--onefile`) executable.
- Select between console-based (`--console`) or windowed (`--windowed`, hides console) applications.
- Specify additional files to bundle with the executable.
- Define custom build paths.
- Import and Export configuration settings.
- View the `pyinstaller` command being generated.
- Real-time log output from `pyinstaller`.

## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).
- **PyInstaller:** This GUI application is a front-end for PyInstaller. You *must* install it separately.

## Installation

1.  **Install PyInstaller:**
    Open your terminal or command prompt and run:
    ```bash
    pip install pyinstaller
    ```

2.  **Get the Py to Exe Converter GUI:**
    - **Option A: Clone the repository:**
        ```bash
        git clone https://github.com/riteshkarmakar/py-to-exe-converter.git
        cd py-to-exe-converter
        ```
    - **Option B: Download a release:**
        Go to the [Releases](https://github.com/riteshkarmakar/py-to-exe-converter/releases) page of this repository and download the latest version (e.g., a `.zip` file or a pre-built executable).

3.  **Install Dependencies (if cloning):**
    If you cloned the repository, navigate to the project directory and install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Potential Issues

### Windows Defender False Flagging
This application may be false flagged as a virus by Windows Defender. To exclude the app from being flagged:

1. Open Windows Security.
2. Navigate to **Virus & threat protection**.
3. Click **Manage settings** under **Virus & threat protection settings**.
4. Scroll down and click **Add or remove exclusions** under **Exclusions**.
5. Click **Add an exclusion**, then select **Folder** and choose the folder:

   `C:\Users\<your-username>\AppData\Local\Programs\Py to Exe Converter`

   Replace `<your-username>` with your actual Windows username.

## How to Use

1.  **Ensure PyInstaller is installed:** If you haven't already, install PyInstaller using `pip install pyinstaller`.
2.  **Launch the Application:**
    - If you cloned the repo: run `cd src` and `python main.pyw` from the terminal in the project directory.
    - If you downloaded a pre-built executable: double-click the executable file and install it.
3.  **Configure Options:**
    - **Script Location:** Browse and select the Python `.py` file you want to convert.
    - **Icon Location (Optional):** Browse and select an `.ico` file to use as the icon for your executable.
    - **Version File Location (Optional):** Browse and select a version file for advanced version information embedding.
    - **One Directory / One File:** Choose whether PyInstaller should bundle everything into a single executable file (`One File`) or create a directory containing the executable and its dependencies (`One Directory`). `One Directory` is often faster to start and easier to debug.
    - **Console Based / Window Based:** Select `Console Based` if your script is a command-line application or if you want the console window to appear. Select `Window Based` for GUI applications (like those made with PySide6, Tkinter, etc.) to hide the console window.
    - **Additional Files (Optional):** Use the "Additional Files" tab to add data files, assets, or other non-Python files that your script needs to run.
    - **Build Paths (Optional):** Customize where temporary build files and the final executable are placed.
4.  **Run Conversion:** Click the "Run" button.
5.  **Monitor Output:** Check the "Log" tab to see the output from PyInstaller during the conversion process. Any errors will be displayed here.
6.  **Find Executable:** Once finished, your executable will be located in the `dist` subfolder within your project directory or the selected location.

## Credits

This application utilizes the following libraries:

- [PyInstaller](https://pypi.org/project/pyinstaller/): For the core functionality of converting Python scripts to executables.
- [PySide6](https://pypi.org/project/PySide6/): For creating the graphical user interface.
- [requests](https://pypi.org/project/requests/) For checking updates.

## Developer

- **Ritesh Karmakar**
- **Email:** `riteshkarmakar7407@gmail.com`

## License

This project is licensed under the GNU General Public License v3.0.

For the full license text, please see the [LICENSE](https://github.com/riteshkarmakar/py-to-exe-converter/blob/master/LICENSE) file included in this repository or visit [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).