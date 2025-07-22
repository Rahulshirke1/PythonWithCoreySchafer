# 🧠 Getting Started with Jupyter Notebook

Jupyter Notebook is a powerful, interactive web-based environment that helps you:

* 🧶 Write and run **Python** (and other languages) code
* 📈 Visualize data using **plots** and **tables**
* 📝 Add **Markdown** notes for headings, bullet points, equations, etc.
* 🎯 Mix **code** and **rich text** in one place

> It’s widely used in:
>
> * 📈 Data Analysis
> * 🤖 Machine Learning
> * 🎓 Teaching & Documentation

---

## 🚀 Step 1: Install Jupyter Notebook

### ✅ Recommended:

If you’re using **Anaconda**, Jupyter is already installed.

### 💡 Alternatively:

Install using pip:

```bash
pip install notebook
```

---

## ⚙️ Step 2: Launch Jupyter

In your terminal or Anaconda Prompt, run:

```bash
jupyter notebook
```

This opens Jupyter in your browser at:
**[http://localhost:8888](http://localhost:8888)**

---

## 📝 Step 3: Create Your First Notebook

1. Click `New → Python 3 (ipykernel)`
2. A new notebook interface will open with **cells**

### ▶️ Types of Cells

* **Code Cell** – Write and execute Python code
* **Markdown Cell** – Write formatted text, headings, lists, links, etc.

### 🔁 Switch Cell Type

* `Esc + M` → Markdown
* `Esc + Y` → Code

---

## ✅ Step 4: Run Python Code

In a code cell, type:

```python
print("Hello, Jupyter!")
```

Then run it with:
**Shift + Enter**

---

## 💋 Step 5: Write Markdown Notes

Example in a Markdown cell:

````markdown
# This is a heading
## This is a sub-heading

- Bullet 1
- Bullet 2

**Bold Text**  
_Italic Text_  

`inline code`

```python
# code block
print("Hello!")
````

````

---

## 📊 Step 6: Create a Simple Plot

First, install `matplotlib`:

```bash
pip install matplotlib
````

Then, in a code cell:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.show()
```

---

## 💾 Step 7: Save and Export Your Notebook

* 📀 **Save**:
  Go to `File → Save and Checkpoint`

* 📄 **Export**:
  Go to `File → Download As → PDF / HTML / etc.`

---

## 🙌 Why Use Jupyter?

Jupyter Notebooks make it easy to combine **executable code**, **visuals**, and **formatted notes** — perfect for:

* Learning
* Prototyping
* Sharing research
* Creating tutorials

---

> 🔗 You’re now ready to explore data, write code, and tell stories — all in one place. Happy Jupyter-ing! 🎉
