import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ================= Load Model / Scaler / Columns =================
model = joblib.load("Heart-Disease_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")  # List of feature columns

# ================= Streamlit Config =================
st.set_page_config(page_title="Heart Disease Prediction",
                   page_icon="❤️",
                   layout="wide")

# ================= Custom CSS =================
page_bg = """
<style>
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#1d2671,#c33764);
}
.title {
color:white;
text-align:center;
font-size:45px;
font-weight:900;
}
.sub {
color:#f1f1f1;
text-align:center;
font-size:18px;
}
.result-card {
padding:25px;
border-radius:20px;
text-align:center;
font-size:22px;
font-weight:700;
}
.safe {
background:#d4edda;
color:#155724;
}
.danger {
background:#f8d7da;
color:#721c24;
}
table {
background:white;
border-radius:10px;
padding:10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ================= UI Title =================
st.markdown('<p class="title">❤️ Heart Disease Prediction System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Provide patient details in the panel to check risk of heart disease</p>',
            unsafe_allow_html=True)

st.write("")

# ================= Sidebar Inputs =================
st.sidebar.header("🩺 Patient Details Input")

age = st.sidebar.slider("Age", 15, 100, 45)

sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

cp = st.sidebar.selectbox("Chest Pain Type", [0,1,2,3])

bp = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)

chol = st.sidebar.slider("Cholesterol", 100, 600, 200)

fbs = st.sidebar.selectbox("FBS > 120 mg/dl", ["No","Yes"])
fbs = 1 if fbs == "Yes" else 0

ekg = st.sidebar.selectbox("EKG Results", [0,1,2])

max_hr = st.sidebar.slider("Max Heart Rate", 60, 220, 150)

ex_angina = st.sidebar.selectbox("Exercise Angina", ["No","Yes"])
ex_angina = 1 if ex_angina == "Yes" else 0

st_depression = st.sidebar.number_input("ST Depression", 0.0, 10.0, 1.0)

slope = st.sidebar.selectbox("Slope of ST", [0,1,2])

vessels = st.sidebar.selectbox("Number of vessels fluro", [0,1,2,3])

thallium = st.sidebar.selectbox("Thallium", [3,6,7])

# ================= Prepare Input Data =================
input_data = pd.DataFrame([[age, sex, cp, bp, chol, fbs,
                            ekg, max_hr, ex_angina,
                            st_depression, slope, vessels, thallium]],
                          columns=columns)

scaled = scaler.transform(input_data)

# ================= Predict Button =================
center = st.columns(3)[1]
with center:
    predict_btn = st.button("🔍 Predict Heart Disease Risk", use_container_width=True)

if predict_btn:
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1] * 100

    if pred == 1:
        st.markdown(
            f'<div class="result-card danger">⚠️ High Risk Detected<br>Probability: {prob:.2f}%</div>',
            unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="result-card safe">✅ No Heart Disease Detected<br>Probability: {prob:.2f}%</div>',
            unsafe_allow_html=True)

# ================= Feature Explanation Table =================
st.markdown("### 📝 Feature Description")
feature_expl = {
    "Age":"Patient's age in years",
    "Sex":"1 = Male, 0 = Female",
    "Chest pain type":"0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic",
    "BP":"Resting Blood Pressure (mmHg)",
    "Cholesterol":"Serum cholesterol in mg/dl",
    "FBS over 120":"Fasting blood sugar > 120 mg/dl: 1 = True, 0 = False",
    "EKG results":"0 = Normal, 1 = ST-T abnormality, 2 = Left ventricular hypertrophy",
    "Max HR":"Maximum heart rate achieved",
    "Exercise angina":"1 = Yes, 0 = No",
    "ST depression":"ST depression induced by exercise",
    "Slope of ST":"0 = Upsloping, 1 = Flat, 2 = Downsloping",
    "Number of vessels fluro":"Number of major vessels colored by fluoroscopy (0-3)",
    "Thallium":"3 = Normal, 6 = Fixed defect, 7 = Reversible defect"
}

feature_df = pd.DataFrame(list(feature_expl.items()), columns=["Feature", "Description"])
st.table(feature_df)
