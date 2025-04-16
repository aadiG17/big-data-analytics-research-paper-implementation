import streamlit as st
import pickle
import numpy as np

# Load the trained models
models = {
    "Logistic Regression": pickle.load(open("log_reg.pkl", "rb")),
    "Decision Tree": pickle.load(open("dt.pkl", "rb")),
    "Random Forest": pickle.load(open("rf.pkl", "rb")),
    "SVM": pickle.load(open("svm.pkl", "rb")),
    "KNN": pickle.load(open("knn.pkl", "rb")),
    "XGBoost": pickle.load(open("xgb.pkl", "rb"))
}

# Streamlit UI
st.title("Chronic Kidney Disease Prediction")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=50)
bp = st.number_input("Blood Pressure", min_value=50, max_value=180, value=80)
sg = st.number_input("Specific Gravity", min_value=1.0, max_value=1.05, value=1.01, step=0.01)
al = st.number_input("Albumin", min_value=0, max_value=5, value=0)
su = st.number_input("Sugar", min_value=0, max_value=5, value=0)
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["present", "not present"])
ba = st.selectbox("Bacteria", ["present", "not present"])
bgr = st.number_input("Blood Glucose Random", min_value=70, max_value=500, value=120)
bu = st.number_input("Blood Urea", min_value=1, max_value=200, value=40)
sc = st.number_input("Serum Creatinine", min_value=0.1, max_value=15.0, value=1.2, step=0.1)
sod = st.number_input("Sodium", min_value=100, max_value=160, value=140)
pot = st.number_input("Potassium", min_value=2.0, max_value=10.0, value=4.5, step=0.1)
hemo = st.number_input("Hemoglobin", min_value=5.0, max_value=20.0, value=13.5, step=0.1)
pcv = st.number_input("Packed Cell Volume", min_value=10, max_value=60, value=40)
wc = st.number_input("White Blood Cell Count", min_value=2000, max_value=20000, value=8000)
rc = st.number_input("Red Blood Cell Count", min_value=2.0, max_value=8.0, value=5.0, step=0.1)
htn = st.selectbox("Hypertension", ["yes", "no"])
dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["yes", "no"])
ane = st.selectbox("Anemia", ["yes", "no"])

# Encoding categorical variables
binary_map = {"yes": 1, "no": 0, "normal": 1, "abnormal": 0, "present": 1, "not present": 0, "good": 1, "poor": 0}

input_data = np.array([
    age, bp, sg, al, su, binary_map[rbc], binary_map[pc], binary_map[pcc], binary_map[ba], bgr,
    bu, sc, sod, pot, hemo, pcv, wc, rc, binary_map[htn], binary_map[dm], binary_map[cad],
    binary_map[appet], binary_map[pe], binary_map[ane]
]).reshape(1, -1)

# Predict button
if st.button("Predict CKD Status"):
    predictions = {model: clf.predict(input_data)[0] for model, clf in models.items()}
    
    # Display results
    st.subheader("Model Predictions")
    for model, result in predictions.items():
        st.write(f"{model}: {'CKD' if result == 1 else 'Not CKD'}")
