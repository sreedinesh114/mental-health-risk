import streamlit as st
from src.predict import predict_risk

# App Config
st.set_page_config(
    page_title="🧠 Mental Health Risk Predictor",
    layout="wide",
    page_icon="💡"
)

# === HEADER ===
st.markdown("""
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
    }
    .subtle {
        font-size: 16px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🧠 Mental Health Risk Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtle">Predict the likelihood of mental health risk based on digital behavior inputs like age, stress level, and sleep quality.</p>', unsafe_allow_html=True)
st.markdown("---")

# === INPUT LAYOUT ===
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider(
            "🎂 Age", 
            min_value=18, max_value=65, value=30,
            help="User's age in years"
        )
        
    with col2:
        stress_level = st.slider(
            "😓 Stress Level (1-10)", 
            min_value=1, max_value=10, value=5,
            help="Self-reported stress level"
        )

    with col3:
        sleep_quality = st.slider(
            "😴 Sleep Quality (1-10)", 
            min_value=1, max_value=10, value=5,
            help="How well you sleep, 10 = very restful"
        )

# === PREDICTION ===
st.markdown("## 🔍 Prediction Result")

if st.button("🚀 Predict Mental Health Risk", use_container_width=True):
    result = predict_risk(age, stress_level, sleep_quality)

    if result == 1:
        st.error("⚠️ High Mental Health Risk Detected\n\nPlease consider speaking to a mental health professional or counselor.")
    else:
        st.success("✅ Low Mental Health Risk\n\nYou're doing well based on your input patterns!")

# === FOOTER ===
with st.expander("ℹ️ About This App"):
    st.markdown("""
    - This application uses a machine learning model trained on anonymized mental health data.
    - Inputs are not stored or sent anywhere.
    - Model predicts likelihood of being at mental health risk based on behavior indicators.
    
    Built with ❤️ using [Streamlit](https://streamlit.io).
    """)
