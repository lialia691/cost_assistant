import os
import subprocess

def convert_ui_to_py(ui_file, py_file):
    command = f"pyside6-uic {ui_file} -o {py_file}"
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully converted {ui_file} to {py_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {ui_file} to {py_file}: {e}")

if __name__ == "__main__":
    ui_file = "mainwindow.ui"
    py_file = "mainwindow.py"
    convert_ui_to_py(ui_file, py_file)