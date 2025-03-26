import streamlit as st

# Page Config
st.set_page_config(page_title="BMI CALCULATOR", page_icon="⚖️", layout="centered")

# Title
st.title("⚖️ BMI CALCULATOR")
st.markdown("""
## 🏋️‍♂️ This BMI calculator helps you assess if you are underweight, normal weight, overweight, or obese.
""")

# Input Fields for Weight and Height
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("🔢 Enter your weight in kg:", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("📏 Enter your height in m:", min_value=1.0, format="%.2f")

# Ensure valid height is provided
if height > 0:
    height_in_meters = height / 100  # Convert cm to meters
    bmi = weight / (height_in_meters ** 2)  # Correct BMI formula

    st.subheader("📊 Your BMI is:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)

    # Display BMI category with emojis
    if bmi < 18.5:
        st.error("⚠️ You are underweight! 🍽️ Try to maintain a balanced diet.")
    elif bmi < 25:
        st.success("🎉 You have a normal weight! 🥗 Keep up the good work! 💪")
    elif bmi < 30:
        st.warning("⚠️ You are overweight! 🚴 Consider regular exercise and a healthy diet.")
    else:
        st.error("⚠️ You are obese! 🏥 Consult a doctor for guidance on a healthier lifestyle.")
else:
    st.info("ℹ️ Please enter a valid height and weight.")
