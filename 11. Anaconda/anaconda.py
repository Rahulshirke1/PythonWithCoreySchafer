# 🐍 What is Anaconda?
# Anaconda is a Python distribution that comes bundled with:

# Python and conda (a package and environment manager),

# Useful tools like Jupyter Notebook, Spyder, and Anaconda Navigator,

# And hundreds of popular data science libraries (NumPy, pandas, scikit-learn, etc.).

# Things i did in Anaconda Prompt

# It’s mainly used for:

# Data science & machine learning,

# Scientific computing,

# Creating isolated environments for different projects.



# 1. python
# output:
# Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>


# 2. pip list
# output:pip list
# Package                  Version
# ------------------------ ---------
# anaconda-anon-usage      0.7.1
# annotated-types          0.6.0
# archspec                 0.2.3
# boltons                  25.0.0
# brotlicffi               1.0.9.2
# certifi                  2025.7.14
# cffi                     1.17.1
# charset-normalizer       3.3.2
# colorama                 0.4.6
# conda                    25.5.1
# conda-anaconda-telemetry 0.2.0
# conda-anaconda-tos       0.2.1
# conda-content-trust      0.2.0
# conda-libmamba-solver    25.4.0
# conda-package-handling   2.4.0
# conda_package_streaming  0.12.0
# cryptography             45.0.3
# distro                   1.9.0
# frozendict               2.4.2
# idna                     3.7
# jsonpatch                1.33
# jsonpointer              2.1
# libmambapy               2.0.5
# markdown-it-py           2.2.0
# mdurl                    0.1.0
# menuinst                 2.3.0
# packaging                24.2
# pip                      25.1
# platformdirs             4.3.7
# pluggy                   1.5.0
# pycosat                  0.6.6
# pycparser                2.21
# pydantic                 2.11.7
# pydantic_core            2.33.2
# Pygments                 2.19.1
# PySocks                  1.7.1
# requests                 2.32.4
# rich                     13.9.4
# ruamel.yaml              0.18.10
# ruamel.yaml.clib         0.2.12
# setuptools               78.1.1
# tqdm                     4.67.1
# truststore               0.10.0
# typing_extensions        4.12.2
# typing-inspection        0.4.0
# urllib3                  2.5.0
# wheel                    0.45.1
# win_inet_pton            1.1.0
# zstandard                0.23.0


# 3. conda --version

# 4. conda --help

# 5. conda list

# 6. Using Conda with Flask & SQLAlchemy

# -> Create a Project Folder First
#    Organize your project code and environment in one place:
#    mkdir flask_app_project
#    cd flask_app_project

# -> Use Descriptive Environment Names
#    Use a name related to your project:
#    conda create --name flask_app_env flask sqlalchemy
#    Avoid names like my_app, env1, etc. Use meaningful names like flask_blog_api, ecom_backend, etc.

# -> Activate the Environment
#    conda activate flask_app_env
#    You should always activate the environment before running code or installing packages.

# ->  Use a requirements.txt or environment.yml File
#     This helps share your project with others (or for yourself in the future).
#     Option A: For pip-based projects (more common for Flask)
#               pip freeze > requirements.txt
#               Then in another machine:
#               pip install -r requirements.txt
#     Option B: For conda-based projects
#               conda env export > environment.yml
#               Then recreate with:
#               conda env create -f environment.yml

# -> Never Install Globally
#    Avoid installing packages globally or in the base environment. Always work inside project-specific environments to avoid version conflicts.
    
# -> Use Git for Version Control
#    Create a .gitignore and ignore files like:
#           __pycache__/
#           *.pyc
#           .env
#           *.sqlite3

# -> Use a .env File for Secrets
#    Don’t hardcode secrets (e.g., DB passwords) in Python code
#           # .env
#           SECRET_KEY=my-secret-key
#           DATABASE_URL=sqlite:///mydb.sqlite3
#           Load it using python-dotenv.

# -> Deactivate When Done
#    After working, deactivate the environment:
#       conda deactivate

# -> Install Only What You Need
#    Don’t bloat your environment with unnecessary packages. Install only what's required for the project.

# -> Use Jupyter for Testing (Optional)
#    If you’re exploring code:
#       conda install jupyter
#       jupyter notebook
#    Use it in your flask_app_env.


# ⚡ Example Workflow (Quick Summary)
# mkdir flask_api
# cd flask_api
# conda create --name flask_api_env flask sqlalchemy
# conda activate flask_api_env
# Start coding app.py, models.py, etc.
# Later:
# pip freeze > requirements.txt
# git init
