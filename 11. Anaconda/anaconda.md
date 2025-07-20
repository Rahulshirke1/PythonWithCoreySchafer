
# 🐍 What is Anaconda?

### Anaconda is a Python distribution that comes bundled with:

#### * **Python** and **conda** (a package and environment manager)
* Useful tools like **Jupyter Notebook**, **Spyder**, and **Anaconda Navigator**
* Hundreds of popular data science libraries like **NumPy**, **pandas**, **scikit-learn**, etc.

#### It’s mainly used for:

* **Data science** & **machine learning**
* **Scientific computing**
* Creating **isolated environments** for different projects


---

<br>

# 🚀 Flask + SQLAlchemy Starter Project (with Anaconda)

This project demonstrates a clean Flask + SQLAlchemy setup using **Anaconda**, ideal for web development, APIs, and backend projects.

---

## 📦 Project Requirements

* Python (via Anaconda)
* Flask
* SQLAlchemy
* python-dotenv (for environment variables)

---

## 🧱 Project Structure

```
flask_app_project/
├── app.py
├── .env
├── requirements.txt
├── environment.yml  # optional (for conda)
├── README.md
├── .gitignore
└── ...
```

---

## ⚙️ Setup Instructions

### 1. 📁 Create and Move into the Project Directory

```bash
mkdir flask_app_project
cd flask_app_project
```

### 2. 🐍 Create and Activate a Conda Environment

```bash
conda create --name flask_app_env flask sqlalchemy
conda activate flask_app_env
```

### 3. 📦 Install Additional Packages

```bash
pip install python-dotenv
```

---

## 🧪 Optional: Jupyter Notebook Support

```bash
conda install jupyter
jupyter notebook
```

---

## 🧾 Environment Variables Setup

Create a `.env` file in the root:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///mydatabase.db
```

---

## 🧊 Freeze Dependencies

### Option A: Using pip

```bash
pip freeze > requirements.txt
```

### Option B: Using Conda

```bash
conda env export > environment.yml
```

---

## 🔁 Restoring Dependencies

### From requirements.txt

```bash
pip install -r requirements.txt
```

### From environment.yml

```bash
conda env create -f environment.yml
```

---

## ❌ Deactivate Conda Environment

```bash
conda deactivate
```

---

## 📂 .gitignore File Example

```gitignore
__pycache__/
*.pyc
.env
*.sqlite3
```

---

## ✅ Summary Table

| Task                | Command                                               |
| ------------------- | ----------------------------------------------------- |
| Create Conda Env    | `conda create --name flask_app_env flask sqlalchemy`  |
| Activate Conda Env  | `conda activate flask_app_env`                        |
| Install dotenv      | `pip install python-dotenv`                           |
| Freeze Dependencies | `pip freeze > requirements.txt` or `conda env export` |
| Deactivate Env      | `conda deactivate`                                    |

---

## ✨ Happy Coding!

This boilerplate gives you a clean and reproducible starting point for Flask development with Anaconda and SQLAlchemy. You can now focus on writing your app! ✨
