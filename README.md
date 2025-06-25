🧠 Mental Health Risk Forecasting Using Digital Activity Patterns

This project uses digital behavioral indicators like sleep quality, stress level, and age to forecast a student's mental health risk using machine learning. It leverages the **StudentLife dataset** and features a clean, responsive **Streamlit UI** for user interaction.


Try the interactive app locally:
```bash
streamlit run app.py
📁 Dataset
Source: MIT StudentLife Dataset

Sample Features:

age

stress_level (1-10)

sleep_quality (1-10)

Target:

mental_risk (yes = at risk, no = not at risk)

🛠 Features
✅ Predict mental health risk from behavioral patterns

🧠 Trained Random Forest model (85%+ accuracy)

📈 Streamlit web app with responsive UI

💬 Intuitive sliders and user-friendly messages

📦 Fully packaged for GitHub & deployment

🧪 Tech Stack
Component	Description
Streamlit	For responsive web-based UI
scikit-learn	ML training and prediction
Pandas	Data loading and preprocessing
Joblib	Model persistence
VS Code	Development environment

📂 Folder Structure
bash
mental-health-risk/
├── app.py                      # Streamlit UI
├── models/
│   └── model.joblib            # Trained ML model
├── src/
│   ├── preprocess.py           # Data preprocessing
│   ├── train.py                # Model training
│   └── predict.py              # Prediction function
├── data/
│   └── mental_health_risk_prediction.csv
├── requirements.txt
└── README.md

⚙️ Setup Instructions
bash
# Clone the repo
git clone https://github.com/your-username/mental-health-risk.git
cd mental-health-risk

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # (or source venv/bin/activate on Mac/Linux)

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train.py

# Launch the web app
streamlit run app.py
📊 Sample Prediction Logic
The model uses 3 features to make a binary prediction (0 = Low Risk, 1 = High Risk). Example:

python
predict_risk(age=24, stress_level=8, sleep_quality=3)  # Output: 1 (High Risk)
🔒 Disclaimer
This app is for educational and research purposes only. It does not provide professional medical advice or diagnosis.

📬 Contact
Author: Dinesh
Email: dsakthivel114@gmail.com
LinkedIn: www.linkedin.com/in/dinesh-s-802183258

⭐️ Show your support
If you found this helpful, give it a ⭐️ on GitHub and share it with others!

yaml

---

📝 Next Steps

- Replace `"your-email@example.com"` and GitHub URL with your actual links.
- Add a real screenshot or demo GIF if you'd like.
- Push to GitHub:

```bash
git init
git add .
git commit -m "Initial commit: Mental Health Risk Prediction Project"
git remote add origin https://github.com/your-username/mental-health-risk.git
git push -u origin main