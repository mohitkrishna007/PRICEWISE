
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PRICEWISE",
    page_icon="💻",
    layout="wide"
)

# ============================================================
# CUSTOM CSS - EXISTING DARK DESIGN
# ============================================================

st.markdown("""
<style>

    .stApp {
        background-color: #0e1117;
        color: white;
    }

    .main-title {
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
        color: white;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #b8b8b8;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 15px;
        color: white;
    }

    div.stButton > button {
        width: 100%;
        height: 55px;
        font-size: 20px;
        font-weight: 600;
        border-radius: 10px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #1b1f2a;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #444;
    }

    .price {
        font-size: 40px;
        font-weight: 700;
        color: #00ff9d;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

MODEL_PATH = "laptop_price_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(
        f"Model file not found at:\n{MODEL_PATH}\n\n"
        "Please make sure laptop_price_model.pkl is present in that location."
    )
    st.stop()

try:
    pipe = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">💻 PRICEWISE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Laptop Price Estimation</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">Laptop Specifications</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# COLUMN 1
# ------------------------------------------------------------

with col1:

    Company = st.selectbox(
        "Company",
        [
            "Acer",
            "Apple",
            "Asus",
            "Chuwi",
            "Dell",
            "Fujitsu",
            "Google",
            "HP",
            "Huawei",
            "Lenovo",
            "LG",
            "MSI",
            "Microsoft",
            "Mediacom",
            "Razer",
            "Samsung",
            "Toshiba",
            "Vero",
            "Xiaomi"
        ]
    )

    TypeName = st.selectbox(
        "TypeName",
        [
            "2 in 1 Convertible",
            "Gaming",
            "Netbook",
            "Notebook",
            "Ultrabook",
            "Workstation"
        ]
    )

    CPU_Company = st.selectbox(
        "CPU Company",
        [
            "Intel",
            "AMD",
            "Samsung"
        ]
    )

    CPU_Type = st.selectbox(
        "CPU Type",
        [
            "Celeron Dual Core",
            "Celeron Quad Core",
            "Core M",
            "Core i3",
            "Core i5",
            "Core i7",
            "Core i9",
            "Pentium Dual Core",
            "Pentium Quad Core",
            "Ryzen 3",
            "Ryzen 5",
            "Ryzen 7",
            "Ryzen 9"
        ]
    )

    CPU_Frequency = st.number_input(
        "CPU Frequency (GHz)",
        min_value=0.5,
        max_value=5.0,
        value=2.5,
        step=0.1
    )



# ------------------------------------------------------------
# COLUMN 2
# ------------------------------------------------------------

with col2:

    RAM = st.number_input(
        "RAM (GB)",
        min_value=2,
        max_value=64,
        value=8,
        step=2
    )

    GPU_Company = st.selectbox(
        "GPU Company",
        [
            "Intel",
            "AMD",
            "Nvidia",
            "ARM"
        ]
    )

    GPU_Type = st.selectbox(
        "GPU Type",
        [
            "Intel HD Graphics",
            "Intel UHD Graphics",
            "Intel Iris Plus Graphics",
            "Intel Iris Xe Graphics",
            "Nvidia GeForce MX150",
            "Nvidia GeForce MX250",
            "Nvidia GeForce MX330",
            "Nvidia GeForce GTX 1050",
            "Nvidia GeForce GTX 1060",
            "Nvidia GeForce GTX 1070",
            "Nvidia GeForce GTX 1080",
            "Nvidia GeForce GTX 1650",
            "Nvidia GeForce GTX 1660 Ti",
            "Nvidia GeForce RTX 2060",
            "Nvidia GeForce RTX 2070",
            "Nvidia GeForce RTX 2080",
            "AMD Radeon",
            "AMD Radeon RX 540",
            "AMD FirePro",
            "Intel HD Graphics 4000"
        ]
    )

    OpSys = st.selectbox(
        "Operating System",
        [
            "Windows 10",
            "Windows 11",
            "Windows 7",
            "macOS",
            "Mac OS X",
            "Linux",
            "Chrome OS",
            "Android",
            "No OS"
        ]
    )

    Weight = st.number_input(
        "Weight (kg)",
        min_value=0.5,
        max_value=6.0,
        value=2.0,
        step=0.1
    )



# ------------------------------------------------------------
# COLUMN 3
# ------------------------------------------------------------

with col3:

    Touchscreen = st.selectbox(
        "Touchscreen",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    IPS = st.selectbox(
        "IPS Display",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    ppi = st.number_input(
        "PPI",
        min_value=50.0,
        max_value=500.0,
        value=141.0,
        step=1.0
    )

    SSD = st.number_input(
        "SSD (GB)",
        min_value=0,
        max_value=2048,
        value=256,
        step=128
    )

    HDD = st.number_input(
        "HDD (GB)",
        min_value=0,
        max_value=2048,
        value=0,
        step=128
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

predict_button = st.button(
    "💰 Predict Laptop Price"
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # IMPORTANT:
    # These column names MUST exactly match the trained model.

    input_data = pd.DataFrame({
        "Company": [Company],
        "TypeName": [TypeName],
        "CPU_Company": [CPU_Company],
        "CPU_Type": [CPU_Type],
        "CPU_Frequency (GHz)": [CPU_Frequency],
        "RAM (GB)": [RAM],
        "GPU_Company": [GPU_Company],
        "GPU_Type": [GPU_Type],
        "OpSys": [OpSys],
        "Weight (kg)": [Weight],
        "Touchscreen": [Touchscreen],
        "IPS": [IPS],
        "ppi": [ppi],
        "SSD": [SSD],
        "HDD": [HDD]
    })

    # Force the exact order expected by the model
    expected_columns = [
        "Company",
        "TypeName",
        "CPU_Company",
        "CPU_Type",
        "CPU_Frequency (GHz)",
        "RAM (GB)",
        "GPU_Company",
        "GPU_Type",
        "OpSys",
        "Weight (kg)",
        "Touchscreen",
        "IPS",
        "ppi",
        "SSD",
        "HDD"
    ]

    input_data = input_data[expected_columns]

    # ========================================================
    # PREDICT
    # ========================================================

    try:

        prediction = pipe.predict(input_data)

        predicted_price = float(np.exp(prediction[0]))

        st.markdown(
            f"""
            <div class="result-box">
                <div style="font-size:22px;">
                    Estimated Laptop Price
                </div>
                <div class="price">
                    ₹{predicted_price:,.0f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Optional debugging information
        with st.expander("🔍 View input data sent to model"):
            st.dataframe(input_data)

    except Exception as e:

        st.error(f"Prediction Error: {e}")

        st.write("Columns sent to the model:")
        st.write(input_data.columns.tolist())
