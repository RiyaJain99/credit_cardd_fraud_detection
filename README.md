# 💳 AI Credit Card Fraud Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge\&logo=python)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge\&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)

</p>

---

# 📌 Overview

This project is an **AI-powered Credit Card Fraud Detection System** developed to identify fraudulent financial transactions using Machine Learning.

The system analyzes transaction data and predicts whether a transaction is **Fraudulent** or **Genuine**, helping financial institutions reduce monetary losses and improve customer security.

---

# 🎯 Business Problem

Banks process millions of credit card transactions every day.

Manual fraud detection is impossible at this scale, making it essential to build an intelligent system that can automatically identify suspicious transactions in real time.

---

# 🚀 Features

* 💳 Credit Card Fraud Prediction
* 🤖 Machine Learning Powered
* 📂 CSV File Upload
* ⚡ Instant Fraud Detection
* 📊 Interactive Streamlit Dashboard
* 📥 Download Prediction Results
* 📈 Business Insights

---

# 🧠 Machine Learning Workflow

```text
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Train-Test Split
      │
      ▼
Random Forest Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Save Model
      │
      ▼
Streamlit Deployment
```

---

# 📊 Dataset

**Credit Card Fraud Detection Dataset**

Dataset includes:

* 284,807 Transactions
* 31 Features
* Binary Classification
* Highly Imbalanced Dataset

Target Variable:

* **0 → Genuine Transaction**
* **1 → Fraudulent Transaction**

---

# 🤖 Machine Learning Model

Algorithm Used:

* Random Forest Classifier

Why Random Forest?

* High Accuracy
* Robust against Overfitting
* Handles Complex Data Patterns
* Suitable for Classification Problems

---

# 📈 Model Performance

Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* Precision
* Recall
* F1-Score

These metrics provide a more complete evaluation than accuracy alone, especially for imbalanced datasets.

---

# 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Git
* GitHub

---

# 📂 Project Structure

```text
Credit Card Fraud Detection/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── Credit Card Fraud Detection.ipynb
```

> Note: The original dataset (`creditcard.csv`) is not included because it exceeds GitHub's file size limit.

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/RiyaJain99/credit_cardd_fraud_detection.git
```

Go to the project folder

```bash
cd credit_cardd_fraud_detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 💼 Business Impact

This solution can help organizations:

* Detect fraudulent transactions faster
* Reduce financial losses
* Improve customer trust
* Support fraud investigation teams
* Strengthen financial security

---

# 🚀 Future Enhancements

* Real-Time Fraud Monitoring
* Probability Scores for Predictions
* Interactive Analytics Dashboard
* Email & SMS Fraud Alerts
* Explainable AI (Feature Importance)
* Cloud Deployment
* API Integration

---

# 👩‍💻 Author

**Riya Jain**

🎓 B.Tech CSE (IoT)
Vellore Institute of Technology (VIT), Vellore

GitHub: **https://github.com/RiyaJain99**

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

### Made with ❤️ using Python, Machine Learning, Streamlit & Scikit-Learn
