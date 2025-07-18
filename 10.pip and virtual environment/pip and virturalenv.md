# 📦 Python Package Management: pip & virtualenv

This guide contains essential commands and concepts you’ve learned about Python's `pip` and `virtualenv`, which help manage packages and isolated environments for your projects.

---

## 🔹 pip (Python Package Installer)

### 1. What is `pip`?

* `pip` is the package installer for Python. It lets you install and manage libraries that are not included with the standard Python installation.

### 2. `pip help`

* Shows help for pip including all available commands and options.

### 3. `pip help install`

* Displays help specifically for the `install` command.
* Includes syntax, options, and usage examples.

### 4. `pip install <package-name>`

* Installs the specified package from PyPI.
* Example: `pip install Pympler`

### 5. `pip list`

* Lists all installed packages and their versions.

### 6. `pip uninstall <package-name>`

* Uninstalls the specified package.
* Example: `pip uninstall Pympler`

### 7. `pip list -o`

* Shows outdated packages (i.e., newer versions available).

### 8. `pip install -U <package-name>`

* Upgrades the specified package to the latest version.

### 9. `pip freeze`

* Outputs installed packages in `requirements.txt` format.

### 10. `pip freeze > requirements.txt`

* Saves the current environment's dependencies to a file.

### 11. `cat requirements.txt`

* Displays the contents of the `requirements.txt` file.
* Note: This is a Unix/Linux/macOS command (also works in Git Bash/WSL on Windows).

### 12. `pip install -r <file>`

* Installs all packages listed in the given file.
* Example: `pip install -r requirements.txt`

### 13. `pip list --outdated`

* Lists all installed packages that have newer versions available.

---

## 🛠️ Virtual Environments with `virtualenv`

### What is `virtualenv`?

* `virtualenv` is a third-party tool that creates isolated Python environments.
* Useful for managing dependencies separately for each project.
* More flexible than `venv` and compatible with Python 2.

### 1. Install `virtualenv`

```bash
pip install virtualenv
```

### 2. Create a Virtual Environment

```bash
virtualenv myenv
```

### 3. Activate the Virtual Environment

* **Windows (CMD/PowerShell):**

```bash
myenv\Scripts\activate
```

* **Git Bash (Windows):**

```bash
source myenv/Scripts/activate
```

* **Linux/macOS:**

```bash
source myenv/bin/activate
```

### 4. Check Python/Pip Path

* To verify which Python or pip is being used inside the virtual environment:

```bash
which python
which pip
```

### 5. Save & Reinstall Dependencies

* **Save dependencies:**

```bash
pip freeze > requirements.txt
```

* **Reinstall later:**

```bash
pip install -r requirements.txt
```

### 6. Deactivate the Environment

* Returns to global Python environment:

```bash
deactivate
```

### 7. Delete the Environment

* Removes the virtual environment completely:

```bash
rm -rf myenv/
```

---

You're now equipped to manage Python projects like a pro 💪
Let me know if you'd like a script or alias to automate this workflow!
