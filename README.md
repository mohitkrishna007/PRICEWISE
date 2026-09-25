# 💻 PriceWise – Laptop Price Prediction

PriceWise is an end-to-end Machine Learning web application that predicts the estimated price of a laptop based on its hardware and configuration specifications.

The project covers the complete Machine Learning workflow — from data preprocessing and exploratory data analysis to feature engineering, model training, hyperparameter tuning, model serialization, and deployment through Streamlit.

---

## 🚀 Project Overview

Buying a laptop can be difficult when comparing different combinations of processors, RAM, storage, GPU, display features, and other specifications.

**PriceWise** provides an interactive way to estimate a laptop's price by allowing users to enter its specifications and receive a predicted price instantly.

### 🔍 Input Features

The model considers specifications such as:

- 🏢 Company
- 💻 Laptop Type
- ⚙️ CPU Company & Type
- ⚡ CPU Frequency
- 🧠 RAM
- 🎮 GPU Company & Type
- 💾 SSD Storage
- 💽 HDD Storage
- 🖥️ Operating System
- ⚖️ Weight
- 📱 Touchscreen
- 🖼️ IPS Display
- 📐 Pixel Density (PPI)

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical computations
- **Scikit-learn** – Machine Learning and preprocessing
- **Random Forest Regressor** – Price prediction
- **GridSearchCV** – Hyperparameter optimization
- **Joblib** – Model serialization
- **Streamlit** – Interactive web application
- **Git & GitHub** – Version control

---

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Feature Preprocessing
     ↓
Random Forest Regression
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Web Application
     ↓
Real-Time Price Prediction
