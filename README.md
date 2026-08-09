# 🎬 MovieIQ – Movie Success Prediction Using Machine Learning

## 📌 Overview

MovieIQ is a Machine Learning web application that predicts whether a movie is likely to be **Successful** or **Unsuccessful** based on its characteristics. The application uses a **Random Forest Classifier** trained on historical movie data and is deployed using **Streamlit**. Users can enter movie details such as budget, popularity, runtime, vote average, and genre to receive an instant prediction along with a confidence score. The application also includes an interactive analytics dashboard for visualizing movie trends.

---

## 🚀 Features

- 🎯 Predict Movie Success using Machine Learning
- 📊 Interactive Analytics Dashboard
- 📈 Dynamic Plotly Charts
- 💯 Confidence Score for Predictions
- 🎬 User-Friendly Streamlit Interface
- 📱 Responsive and Interactive Design

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib
- Matplotlib

---

## 📂 Dataset Features

The prediction model uses the following features:

- 💰 Budget
- ⭐ Popularity
- ⏱ Runtime
- ⭐ Vote Average
- 🎭 Genre

---

## 🤖 Machine Learning Model

**Algorithm Used**
- Random Forest Classifier

**Data Preprocessing**
- Removed duplicate records
- Handled missing values
- Cleaned and extracted movie genres
- One-Hot Encoding for categorical features
- Feature preprocessing using Scikit-learn Pipeline

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | **80.49%** |
| Algorithm | Random Forest Classifier |

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

- 🎬 Movie Success Prediction
- 📊 Success Distribution
- 💰 Budget Analysis
- ⭐ Popularity Analysis
- ⏱ Runtime Distribution
- 🎭 Genre Distribution
- 📈 Revenue Analysis
- 💯 Prediction Confidence Score

---

## 📁 Project Structure

MovieIQ/

├── app.py

├── model.pkl

├── movies.csv

├── requirements.txt

├── assets/

└── README.md

---

## ▶️ Run the Project Locally

### Clone the Repository

```bash
git clone https://github.com/hemapriya04-05-06/MovieIQ.git
```

### Navigate to the Project Folder

```bash
cd MovieIQ
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

**Streamlit Application**

https://movieiq-2eyjwgsrjwj7otdmrv957v.streamlit.app/

---

## 🎯 Future Enhancements

- Improve prediction accuracy using advanced ML algorithms.
- Include additional features such as cast, director, production company, and release date.
- Predict box office revenue instead of binary success.
- Integrate recommendation systems.
- Deploy using Docker and Cloud services.

---

## 👩‍💻 Developer

**Hemapriya**

Final Year – B.Tech Information Technology

---

## ⭐ Support

If you found this project useful, please consider giving this repository a ⭐ on GitHub.

Thank you for visiting **MovieIQ – Movie Success Prediction Using Machine Learning**!
