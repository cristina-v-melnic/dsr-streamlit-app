import streamlit as st

def main():
    st.title("My Basic Streamlit Page")
    
    # Adding some text
    st.write("Welcome to my Streamlit page! This is a demonstration of text, image, and video elements.")
    
    # Adding a picture
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
             caption="Streamlit Logo")
    
    # Adding a video
    st.video("https://www.youtube.com/watch?v=ZK3O402wf1c")

    st.write("That's it! A simple Streamlit page with text, an image, and a video.")

if __name__ == "__main__":
    main()