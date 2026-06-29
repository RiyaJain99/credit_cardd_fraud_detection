import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { background-color: #0e1117; }
    
    .header-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid #e94560;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #0f3460;
        margin-bottom: 1rem;
    }

    .fraud-card {
        background: linear-gradient(135deg, #1a1a2e, #7f1d1d);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #ef4444;
        margin-top: 1rem;
    }

    .safe-card {
        background: linear-gradient(135deg, #1a1a2e, #064e3b);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #10b981;
        margin-top: 1rem;
    }

    .warning-card {
        background: linear-gradient(135deg, #1a1a2e, #713f12);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #eab308;
        margin-top: 1rem;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #e94560, #0f3460);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0f3460, #e94560);
        transform: scale(1.02);
    }

    .upload-box {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 2rem;
        border-radius: 15px;
        border: 2px dashed #e94560;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h1 style='color: #e94560;'>💳 FraudAI</h1>
            <p style='color: #888;'>Transaction Security Platform</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🤖 Model Info")
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Algorithm</p>
            <h3 style='color: #e94560; margin:0;'>Random Forest</h3>
        </div>
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Type</p>
            <h3 style='color: #10b981; margin:0;'>Binary Classification</h3>
        </div>
        <div class='metric-card'>
            <p style='color: #888; margin:0;'>Target</p>
            <h3 style='color: #3b82f6; margin:0;'>Fraud Detection</h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📊 Detection Guide")
    st.markdown("""
        - 🔴 **Fraud** — Suspicious transaction
        - 🟢 **Genuine** — Safe transaction
        - 🟡 **Review** — Needs manual check
    """)

    st.markdown("---")
    st.markdown("### 📋 How to Use")
    st.markdown("""
        1. Upload your CSV file
        2. Click Detect Fraud button
        3. View results and download report
    """)

# Header
st.markdown("""
    <div class='header-box'>
        <h1 style='color: white; font-size: 2.5rem; margin:0;'>
            💳 AI Credit Card Fraud Detection
        </h1>
        <p style='color: #888; margin-top: 0.5rem; font-size: 1.1rem;'>
            Detect fraudulent transactions instantly using Machine Learning
        </p>
    </div>
""", unsafe_allow_html=True)

# Stats Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Dataset</p>
            <h3 style='color: white; margin:0;'>Credit Card</h3>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Model</p>
            <h3 style='color: #e94560; margin:0;'>Random Forest</h3>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Problem Type</p>
            <h3 style='color: #10b981; margin:0;'>Classification</h3>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class='metric-card'>
            <p style='color: #888; margin:0; font-size:0.9rem;'>Detection</p>
            <h3 style='color: #3b82f6; margin:0;'>Real-time</h3>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Upload Section
st.markdown("### 📂 Upload Transaction Data")
st.markdown("""
    <div class='upload-box'>
        <h3 style='color: #e94560; margin:0;'>📁 Drop your CSV file here</h3>
        <p style='color: #888; margin-top: 0.5rem;'>
            Supported format: CSV with transaction features
        </p>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"],
    help="Upload a CSV file containing transaction data"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown("---")
    st.markdown("### 📊 Uploaded Transaction Data")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class='metric-card'>
                <p style='color: #888; margin:0;'>Total Transactions</p>
                <h2 style='color: #e94560; margin:0;'>{len(df):,}</h2>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class='metric-card'>
                <p style='color: #888; margin:0;'>Total Features</p>
                <h2 style='color: #10b981; margin:0;'>{len(df.columns)}</h2>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class='metric-card'>
                <p style='color: #888; margin:0;'>File Status</p>
                <h2 style='color: #3b82f6; margin:0;'>✅ Loaded</h2>
            </div>
        """, unsafe_allow_html=True)

    st.dataframe(df.head(), use_container_width=True)

    if "Class" in df.columns:
        X = df.drop("Class", axis=1)
    else:
        X = df

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_btn = st.button("🚀 Detect Fraud Transactions")

    if predict_btn:
        with st.spinner("🔍 Analyzing transactions for fraud..."):
            predictions = model.predict(X)

        result = df.copy()
        result["Prediction"] = predictions
        result["Status"] = result["Prediction"].map(
            {0: "✅ Genuine", 1: "🚨 Fraud"}
        )

        fraud = int((predictions == 1).sum())
        genuine = int((predictions == 0).sum())
        fraud_pct = (fraud / len(predictions)) * 100

        st.markdown("---")
        st.markdown("### 🎯 Detection Results")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
                <div class='metric-card'>
                    <p style='color: #888; margin:0;'>Total Analyzed</p>
                    <h2 style='color: white; margin:0;'>{len(predictions):,}</h2>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='metric-card'>
                    <p style='color: #888; margin:0;'>Fraud Detected</p>
                    <h2 style='color: #ef4444; margin:0;'>{fraud:,}</h2>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class='metric-card'>
                    <p style='color: #888; margin:0;'>Genuine</p>
                    <h2 style='color: #10b981; margin:0;'>{genuine:,}</h2>
                </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
                <div class='metric-card'>
                    <p style='color: #888; margin:0;'>Fraud Rate</p>
                    <h2 style='color: #eab308; margin:0;'>{fraud_pct:.2f}%</h2>
                </div>
            """, unsafe_allow_html=True)

        if fraud_pct > 10:
            st.markdown("""
                <div class='fraud-card'>
                    <h2 style='color: #ef4444;'>🚨 HIGH FRAUD ALERT!</h2>
                    <p style='color: #888;'>
                        High number of fraudulent transactions detected.
                        Immediate action required!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif fraud > 0:
            st.markdown(f"""
                <div class='warning-card'>
                    <h2 style='color: #eab308;'>⚠️ FRAUD DETECTED</h2>
                    <p style='color: #888;'>
                        {fraud} suspicious transactions found. Please review immediately.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class='safe-card'>
                    <h2 style='color: #10b981;'>✅ ALL TRANSACTIONS SAFE</h2>
                    <p style='color: #888;'>
                        No fraudulent transactions detected. All clear!
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📋 Business Recommendations")
            if fraud > 0:
                recommendations = [
                    "Block flagged accounts immediately",
                    "Notify customers of suspicious activity",
                    "Escalate to fraud investigation team",
                    "Review recent transaction patterns",
                    "Strengthen authentication for flagged users"
                ]
            else:
                recommendations = [
                    "Continue monitoring transactions",
                    "Update fraud detection model regularly",
                    "Maintain security protocols",
                    "Run periodic fraud audits",
                    "Keep customer verification active"
                ]

            for rec in recommendations:
                color = "#ef4444" if fraud > 0 else "#10b981"
                st.markdown(f"""
                    <div class='metric-card' style='margin-bottom: 0.5rem;'>
                        <p style='color: {color}; margin:0;'>✓ {rec}</p>
                    </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("### 📊 Transaction Summary")
            summary_data = pd.DataFrame({
                "Category": ["Total Transactions", "Genuine", "Fraud", "Fraud Rate"],
                "Value": [
                    f"{len(predictions):,}",
                    f"{genuine:,}",
                    f"{fraud:,}",
                    f"{fraud_pct:.2f}%"
                ]
            })
            st.dataframe(summary_data, use_container_width=True)

        st.markdown("---")
        st.markdown("### 📥 Download Results")
        csv = result.to_csv(index=False).encode("utf-8")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                "⬇️ Download Fraud Detection Report",
                csv,
                "fraud_detection_report.csv",
                "text/csv",
                use_container_width=True
            )

else:
    st.markdown("""
        <div style='text-align: center; padding: 3rem;'>
            <h2 style='color: #888;'>👆 Upload a CSV file to get started</h2>
            <p style='color: #555;'>
                Your transaction data will be analyzed instantly for fraud detection
            </p>
        </div>
    """, unsafe_allow_html=True)