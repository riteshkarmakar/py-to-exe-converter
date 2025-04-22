import shlex

def generate_pyinstaller_command(
    script_path: str,
    noconfirm: bool = False,
    icon_path: str | None = None,
    version_file_path: str | None = None,
    one_file: bool = False,
    windowed: bool = False,
    additional_data: list[tuple[str, str]] | None = None,
    distpath: str | None = None,
    workpath: str | None = None,
    specpath: str | None = None,
    name: str | None = None,
    contents_dir: str | None = None,
    manual_args: str | None = None
) -> tuple[list[str], str]:
    """Generate a PyInstaller command with customizable options.

    Args:
        script_path (str): Path to your Python script.
        noconfirm (bool): Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation. Defaults to False.
        icon_path (str, optional): Path to .ico file for the executable. Defaults to None.
        version_file_path (str, optional): Add a version resource from FILE to the exe. Defaults to None.
        one_file (bool, optional): Whether to generate a single file executable. Defaults to False.
        windowed (bool, optional): Whether to hide the console window (for GUI apps). Defaults to False.
        additional_data (list[tuple[str, str]], optional): List of (source, destination) tuples for data files. Defaults to None.
        distpath (str, optional): Where to put the bundled app (default: ./dist).
        workpath (str, optional): Where to put all the temporary work files, .log, .pyz and etc. (default: ./build).
        specpath (str, optional): Folder to store the generated spec file (default: current directory).
        name (str, optional): Name of the executable. Defaults to None.
        contents_dir (str, optional): For onedir builds only, specify the name of the directory in which
                                      all supporting files (i.e. everything except the executable itself) will be placed in.
                                      Use “.” to re-enable old onedir layout without contents directory.
        manual_args (str, optional): Additional command-line arguments provided manually 
                                     by the user. These will be appended at the end of the command.

    Returns:
        tuple: A tuple containing
        - A list of command-line arguments suitable for running with QProcess or subprocess.
        - A formatted string version of the command for display, logging, or copy-pasting.

    """

    command = ["pyinstaller"]

    if noconfirm:
        command.append("--noconfirm")
    if icon_path:
        command.extend(["--icon", icon_path])
    if version_file_path:
        command.extend(["--version-file", version_file_path])
    if one_file:
        command.append("--onefile")
    if windowed:
        command.append("--windowed")

    if additional_data:
        for src, dest in additional_data:
            command.extend(["--add-data", f"{src}:{dest}"])

    if distpath:
        command.extend(["--distpath", distpath])
    if workpath:
        command.extend(["--workpath", workpath])
    if specpath:
        command.extend(["--specpath", specpath])
    if name:
        command.extend(["--name", name])
    if contents_dir:
        command.extend(["--contents-directory", contents_dir])
    if manual_args:
        try:
            command.extend(shlex.split(manual_args))
        except ValueError:
            # If the manual arguments contain unbalanced quotes or other syntax issues,
            # shlex.split() raises a ValueError. We just skip adding them in that case.
            pass

    command.append(script_path)

    return command, shlex.join(command)
