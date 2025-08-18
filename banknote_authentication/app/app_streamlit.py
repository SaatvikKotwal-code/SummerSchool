import streamlit as st
import joblib

# Load model
MODEL_PATH = "models/best_model.joblib"
clf = joblib.load(MODEL_PATH)

# Apply custom CSS
with open('app/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# App header
st.markdown("""
    <div class="header">
        <h1>💵 Banknote Authentication App</h1>
        <p>Advanced AI-powered detection for genuine vs fake banknotes</p>
    </div>
""", unsafe_allow_html=True)

# Create a container for the form
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.markdown("### 🔍 Enter Banknote Features")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        variance = st.number_input("Variance", value=0.0, help="Measure of data spread")
        skewness = st.number_input("Skewness", value=0.0, help="Measure of data asymmetry")
    
    with col2:
        curtosis = st.number_input("Curtosis", value=0.0, help="Measure of tail heaviness")
        entropy = st.number_input("Entropy", value=0.0, help="Measure of randomness")
    
    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Prediction button
    if st.button("🔍 Check Banknote Authenticity", use_container_width=True):
        features = [[variance, skewness, curtosis, entropy]]
        prediction = clf.predict(features)[0]
        
        # Display results with enhanced styling
        if prediction == 0:
            st.success("✅ **Genuine Banknote Detected** - This banknote appears to be authentic")
        else:
            st.error("⚠️ **Fake Banknote Alert** - This banknote appears to be counterfeit")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Add footer
st.markdown("""
    <div style='text-align: center; margin-top: 2rem; color: #e0e7ff;'>
        <p>Powered by Machine Learning • Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True)
