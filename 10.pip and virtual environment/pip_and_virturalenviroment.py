# ------------------pip--------------------

# 0. 

# 1. pip help :pip is the package installer for Python. It lets you install and manage libraries that are not included with the standard Python installation.

# 2. pip help install : -
#ou are asking pip to show you help specifically for the install command. It displays a detailed explanation of how to use pip install, including its:
# Syntax
# Description
# List of all available options and flags
# Common usage examples

# 3. pip install <package-name> :-
# This is the most basic and essential pip command. It tells Python to:
# 📥 Download and install a package from PyPI (Python Package Index) into your system or virtual environment.
# example : pip install Pympler

# 4. pip list :- Displays a list of all Python packages currently installed in your environment, along with their versions.

# 5. pip uninstall <package-name> :- This command is used to remove/uninstall a Python package from your system or virtual environment.
# example: pip uninstall Pympler

# 6. pip list -o :- This command shows a list of all outdated packages — i.e., packages that have a newer version available on PyPI than the one installed on your system.

# 7. pip install -U <package-name> :- It upgrades the given package to the latest version available on PyPI.

# 8. pip freeze :- pip freeze outputs a list of all installed Python packages in the current environment in a format suitable for a requirements.txt file.

# 9. pip freeze > requirements.txt :- This command creates a requirements.txt file containing a list of all installed Python packages in your current environment with exact versions.

# 10. cat requirements.txt :- The cat command is used in Unix/Linux/macOS (and in Git Bash or WSL on Windows) to display the contents of a file.

# 11. pip install -r <file> :- This command installs all Python packages listed in a file, typically requirements.txt.
# example: pip install -r requirements.txt

# 12. pip list --outdated :- This command shows you a list of installed Python packages that have newer versions available.

# ------------------------------------------virtual evironment-----------------------------------------------------

# virtualenv
# virtualenv is a third-party Python package that helps you create isolated environments for your Python projects. It's similar to venv (which is built into Python 3.3+), but with more features and Python 2 compatibility.

#  1. Install virtualenv
# pip install virtualenv 

# 2. Create a Virtual Environment
# virtualenv myenv

# 3. Activate the Virtual Environment
# ✅ On Windows (CMD or PowerShell):
# myenv\Scripts\activate
# ✅ On Git Bash (Windows):
# source myenv/Scripts/activate
# ✅ On Linux/macOS:
# source myenv/bin/activate

# 4. which python :- The command which python (or which python3) is used to find the path of the Python interpreter currently being used in your terminal.
# or
# 5. which pip :- The command which pip tells you where the pip executable is located — i.e., which version of pip is currently being used.

#  6. Freeze and Reinstall Requirements 
# Save current dependencies:
# pip freeze > requirements.txt

# Reinstall them later:
# pip install -r requirements.txt

# 7. Deactivate the Environment
# to go to the global state
# deactivate

# 8. rm -rf myenv/ :- is used to forcefully delete the myenv directory and everything inside it, including hidden files.
