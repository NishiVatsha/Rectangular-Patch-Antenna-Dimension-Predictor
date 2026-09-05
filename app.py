import streamlit as st
import joblib
import pandas as pd

MODEL_PATH = "antenna_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


st.set_page_config(page_title="Rectangular Patch Antenna Predictor")

st.title("📡 Rectangular Patch Antenna Dimension Predictor")
st.write("Enter the antenna specifications below.")

try:
    model = load_model()
except FileNotFoundError:
    st.error(
        f"Couldn't find '{MODEL_PATH}'. Make sure it's in the same folder as app.py."
    )
    st.stop()
except Exception as e:
    st.error(
        "Failed to load the model. This usually means the scikit-learn / "
        "xgboost / joblib versions installed here don't match the versions "
        "used when the model was trained. Re-check requirements.txt.\n\n"
        f"Details: {e}"
    )
    st.stop()

frequency = st.number_input("Frequency (GHz)", min_value=0.1, value=2.4, step=0.1)
dielectric = st.number_input("Dielectric Constant", min_value=1.0, value=4.4, step=0.1)
height = st.number_input("Substrate Height (mm)", min_value=0.1, value=1.6, step=0.1)
loss = st.number_input(
    "Loss Tangent", min_value=0.0, value=0.02, step=0.001, format="%.4f"
)
copper = st.number_input(
    "Copper Thickness (mm)", min_value=0.001, value=0.035, step=0.001, format="%.3f"
)

if st.button("Predict Dimensions"):
    input_data = pd.DataFrame(
        [[frequency, dielectric, height, loss, copper]],
        columns=[
            "Frequency_GHz",
            "Dielectric_Constant",
            "Height_mm",
            "Loss_Tangent",
            "Copper_Thickness_mm",
        ],
    )

    prediction = model.predict(input_data)

    st.success("Prediction Complete!")
    st.subheader("Predicted Dimensions")
    st.write(f"**Patch Width:** {prediction[0][0]:.3f} mm")
    st.write(f"**Patch Length:** {prediction[0][1]:.3f} mm")
    st.write(f"**Ground Width:** {prediction[0][2]:.3f} mm")
    st.write(f"**Ground Length:** {prediction[0][3]:.3f} mm")
