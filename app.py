import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
import folium
from streamlit_folium import st_folium

# -----------------------------------------------
# Load model
MODEL_PATH = "wildfire_model_cleaned2.h5"
model = load_model(MODEL_PATH)

# -----------------------------------------------
# Streamlit UI
st.set_page_config(page_title="Wildfire Detection App", layout="centered")
st.title("🔥 Wildfire Detection System")
st.sidebar.title("🚨 Emergency Info")
st.sidebar.write("📞 Fire Dept: 101")
st.sidebar.write("🌐 Forest Services: forest-authority@example.com")
st.sidebar.write("📍 Location: India")

# -----------------------------------------------
# Upload image
uploaded_file = st.file_uploader("Upload a satellite image or forest photo...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = img.resize((128,128))
    img_array = np.array(img) / 255.0
    img_tensor = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_tensor)[0][0]

    if prediction > 0.5:
        st.error("🔥 Wildfire Detected!")

        with st.expander("🚒 Emergency Actions"):
            st.markdown("""
            - ✅ Notified Local Forest Authorities
            - ✅ Fire Department on Alert
            - ✅ Evacuation Protocol Initiated
            - ✅ Monitoring via Satellite
            """)
            st.markdown("📍 **Estimated Coordinates (simulated):** `Lat: 19.07, Lon: 73.02`")

        st.toast("🔥 Emergency Protocol Activated!", icon="🚨")
        st.markdown("<h4 style='color:red;'>Simulated Emergency Response Triggered</h4>", unsafe_allow_html=True)

        # ------------------------
        # Display emergency location map
        st.subheader("🗺️ Affected Zone (Simulated Disaster Area)")
        m = folium.Map(location=[19.07, 73.02], zoom_start=8)
        folium.Marker(
            [19.07, 73.02],
            tooltip="Wildfire Detected",
            popup="🔥 Simulated Disaster Zone",
            icon=folium.Icon(color="red", icon="fire"),
        ).add_to(m)
        st_folium(m, width=700, height=400)

        # ------------------------
        st.info("ℹ️ This is a simulation. To implement real alerts, see below:")

        with st.expander("💡 Upgrade to Real Alerts"):
            st.markdown("""
            #### Send Real Alerts:
            1. **Email Fire Dept (Python `smtplib`)**
            2. **Send SMS via Twilio API**
            3. **Trigger Webhook (IFTTT, Zapier, Custom APIs)**
            4. **Push alerts to Cloud Dashboard**
            
            ✅ Requires:
            - Authentication (API keys, OAuth)
            - Authority Permissions
            - Logging and monitoring system
            """)
    else:
        st.success("✅ No wildfire detected.")
        st.markdown("The uploaded image appears safe. No emergency action is required.")

# Footer
st.markdown("---")
st.caption("Developed as a capstone project for wildfire detection. Not for real emergency use.")