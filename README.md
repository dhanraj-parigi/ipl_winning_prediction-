# 🏏 IPL Winning Team Predictor 🎯

This is a Machine Learning + Streamlit-based web app that predicts the **likely winning team** in an IPL (Indian Premier League) match based on input like batting team, bowling team, venue, and current score.


<br>

## 💡 Features

- 🔢 Predict match winner based on:
  - Batting team
  - Bowling team
  - Venue
  - Current 1st innings score
- 🎨 Streamlit UI with IPL banner background
- 💾 Trained using RandomForestClassifier
- 🧠 Encodes team/venue using LabelEncoding
- 📊 Easy to extend with more match features

<br>

## 🛠 Technologies Used

- 🐍 Python 3.12
- 📦 pandas, scikit-learn, joblib
- 🌐 Streamlit
- 📁 Git & GitHub

<br>

## 🚀 How to Run Locally

1. 📥 Clone this repo:
    ```bash
    git clone https://github.com/your-username/ipl_winning_prediction.git
    cd ipl_winning_prediction
    ```

2. 🛠 Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. ▶️ Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 🧠 Model Training Overview

- Dataset: `ipl_colab.csv`
- Selected Columns: `batting_team`, `bowling_team`, `venue`, `total`
- Label: Winner (batting_team wins → 1, else 0)
- Algorithm: `RandomForestClassifier`
- Evaluation: Train-test split + prediction

---

## 🎯 Sample Screenshot

> Add screenshot later (optional)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Made with ❤️ by [Your Name]  
📧 Email: you@example.com  
🌐 [Portfolio/LinkedIn]

---

## 🏁 License

This project is open-source and available under the [MIT License](LICENSE).


