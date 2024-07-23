import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Interactive Streamlit Page")

    # Text input
    user_name = st.text_input("Enter your name", "")
    if user_name:
        st.write(f"Hello, {user_name}!")

    # Numeric input
    number = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
    
    # Slider
    power = st.slider("Power", min_value=1, max_value=5, value=2)

    # Computation based on user input
    result = number ** power
    st.write(f"{number} raised to the power of {power} is: {result}")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Summary:")
        st.write(df.describe())

        # Plot
        st.line_chart(df)

    # Button to trigger computation
    if st.button("Generate Random Data"):
        data = np.random.randn(100, 2)
        st.write("Generated Random Data:")
        st.dataframe(data)

if __name__ == "__main__":
    main()