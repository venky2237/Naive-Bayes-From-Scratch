# 🧠 Naive Bayes Classification from Scratch (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Naive%20Bayes-orange)

A beginner-friendly implementation of the **Naive Bayes Classification Algorithm** from scratch using **Python** and **Pandas**. This project demonstrates how Naive Bayes works internally by manually calculating probabilities instead of using machine learning libraries like Scikit-learn.

---

# 📌 Project Overview

This project uses the classic **Play Tennis** dataset to predict whether a tennis match should be played based on weather conditions.

The implementation covers the complete Naive Bayes workflow:

* 📖 Loading the dataset
* 📊 Calculating Prior Probabilities
* 📈 Calculating Conditional Probabilities
* 📋 Creating a Probability Lookup Table
* 🧮 Applying Bayes' Theorem
* ✅ Predicting the final class using the **Maximum A Posteriori (MAP)** Rule

---

# 🎯 Problem Statement

Given weather conditions such as:

* ☀️ Outlook = Sunny
* 🌡️ Temperature = Hot
* 💧 Humidity = High
* 🌬️ Wind = Weak

Predict whether:

* ✅ Play Tennis = Yes
* ❌ Play Tennis = No

using the **Naive Bayes Algorithm**.

---

# 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 💻 Visual Studio Code

---

# 📂 Project Structure

```text
Naive-Bayes-From-Scratch/
│
├── naive_bayes.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Algorithm Workflow

```text
Training Dataset
        │
        ▼
Calculate Prior Probabilities
        │
        ▼
Calculate Conditional Probabilities
        │
        ▼
Create Lookup Table
        │
        ▼
Receive New Test Sample
        │
        ▼
Calculate Probability for YES
        │
        ▼
Calculate Probability for NO
        │
        ▼
Compare Both Probabilities
        │
        ▼
Apply MAP Rule
        │
        ▼
Final Prediction
```

---

# 🧮 Mathematical Formula

Naive Bayes is based on **Bayes' Theorem**.

[
P(C|X)=\frac{P(X|C)\times P(C)}{P(X)}
]

Since (P(X)) is the same for every class, the classifier predicts using:

[
P(C)\times\prod_{i=1}^{n}P(X_i|C)
]

Where:

* **P(C)** → Prior Probability
* **P(Xᵢ | C)** → Conditional Probability
* **∏** → Product of all conditional probabilities

The class with the **highest probability** is selected.

---

# 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Naive-Bayes-From-Scratch.git
```

### 2️⃣ Open the Project Folder

```bash
cd Naive-Bayes-From-Scratch
```

### 3️⃣ Install the Required Library

```bash
pip install pandas
```

or

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Program

```bash
python naive_bayes.py
```

---

# 📊 Complete Output

```text
Dataset
     Outlook Temperature Humidity    Wind Play
0      Sunny         Hot     High    Weak   No
1      Sunny         Hot     High  Strong   No
2   Overcast         Hot     High    Weak  Yes
3       Rain        Mild     High    Weak  Yes
4       Rain        Cool   Normal    Weak  Yes
5       Rain        Cool   Normal  Strong   No
6   Overcast        Cool   Normal  Strong  Yes
7      Sunny        Mild     High    Weak   No
8      Sunny        Cool   Normal    Weak  Yes
9       Rain        Mild   Normal    Weak  Yes
10     Sunny        Mild   Normal  Strong  Yes
11  Overcast        Mild     High  Strong  Yes
12  Overcast         Hot   Normal    Weak  Yes
13      Rain        Mild     High  Strong   No

Prior Probabilities

P(Yes) = 0.6428571428571429
P(No)  = 0.35714285714285715

Crosstab for Outlook

Play      No  Yes
Outlook
Overcast   0    4
Rain       2    3
Sunny      3    2

Crosstab for Temperature

Play         No  Yes
Temperature
Cool          1    3
Hot           2    2
Mild          2    4

Crosstab for Humidity

Play      No  Yes
Humidity
High       4    3
Normal     1    6

Crosstab for Wind

Play    No  Yes
Wind
Strong   3    3
Weak     2    6

Lookup Table

Outlook
Overcast -> {'Yes': np.float64(0.4444444444444444), 'No': np.float64(0.0)}
Rain -> {'Yes': np.float64(0.3333333333333333), 'No': np.float64(0.4)}
Sunny -> {'Yes': np.float64(0.2222222222222222), 'No': np.float64(0.6)}

Temperature
Cool -> {'Yes': np.float64(0.3333333333333333), 'No': np.float64(0.2)}
Hot -> {'Yes': np.float64(0.2222222222222222), 'No': np.float64(0.4)}
Mild -> {'Yes': np.float64(0.4444444444444444), 'No': np.float64(0.4)}

Humidity
Normal -> {'Yes': np.float64(0.6666666666666666), 'No': np.float64(0.2)}

Wind
Strong -> {'Yes': np.float64(0.3333333333333333), 'No': np.float64(0.6)}
Weak -> {'Yes': np.float64(0.6666666666666666), 'No': np.float64(0.4)}

Probability of YES = 0.007054673721340388
Probability of NO  = 0.02742857142857143

Prediction : NO (Don't Play Tennis)
```

---

# ✨ Features

* ✅ Naive Bayes implemented completely from scratch
* ✅ No Scikit-learn or machine learning libraries used
* ✅ Manual calculation of prior and conditional probabilities
* ✅ Uses `pandas.crosstab()` for frequency tables
* ✅ Lookup table implementation for fast prediction
* ✅ Maximum A Posteriori (MAP) Rule for classification
* ✅ Well-commented and beginner-friendly code

---

# 📚 Learning Outcomes

This project helps in understanding:

* ✔️ Bayes' Theorem
* ✔️ Conditional Probability
* ✔️ Prior Probability
* ✔️ Posterior Probability
* ✔️ Conditional Independence Assumption
* ✔️ Maximum A Posteriori (MAP) Rule
* ✔️ Building a Naive Bayes classifier from scratch
* ✔️ Probability-based classification

---

# 🔮 Future Improvements

* 📈 Add Laplace Smoothing to handle zero probabilities
* 📁 Read the dataset from a CSV file
* 📊 Display probability tables more clearly
* 🤖 Compare the implementation with Scikit-learn's Naive Bayes classifier
* 🌐 Build a simple Flask web application for predictions

---

# 👨‍💻 Author

**Chukkala Venkateswara Rao**

AI & Machine Learning Enthusiast | Python Developer | Machine Learning Learner

---

> **This project is developed for educational purposes to understand the internal working of the Naive Bayes algorithm through manual probability calculations without relying on machine learning libraries.**
