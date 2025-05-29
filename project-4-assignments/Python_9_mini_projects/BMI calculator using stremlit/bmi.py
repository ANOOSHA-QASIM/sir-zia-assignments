import streamlit as st  # Streamlit ko import kar rahe hain

# Web App ka Title
st.title("BMI Calculator")

# User se Weight aur Height ka input lena
weight = st.number_input("Apna wazan likho (kg):", min_value=1.0)
height = st.number_input("Apni height likho (meters):", min_value=0.5)

# BMI Calculate karne ka tareeqa
if height > 0:
    bmi = weight / (height ** 2)  # BMI ka formula
    st.write(f"Apka BMI hai: **{bmi:.2f}**")  # BMI dikhayega

    # BMI category batana
    if bmi < 18.5:
        st.warning("Aap Underweight hain! Zyada khana khayein.")
    elif 18.5 <= bmi < 24.9:
        st.success("Aapka wazan bilkul normal hai! 👍")
    elif 25 <= bmi < 29.9:
        st.warning("Aap Overweight hain! Exercise karein.")
    else:
        st.error("Aap Obese hain! Diet aur workout zaroori hai.")
else:
    st.write("Meharbani kar ke sahi height likhein.")
