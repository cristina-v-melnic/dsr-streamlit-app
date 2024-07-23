import streamlit as st

def add_2_cols(link1, link2, im=True):
            # Create two columns on the main page
    col1, col2 = st.columns(2)

    # Add an image to the first column
    if im:
        with col1:
            st.image(link1, caption="Image 1")
            
        # Add an image to the second column
        with col2:
            st.image(link2, caption="Image 2")

        st.write("This is the main page content with two images side by side.")

    else:
        with col1:
            st.video(link1)
        # Add an image to the second column
        with col2:
            st.video(link2)
        
        st.write("This is the main page content with two videos side by side.")

       
def page1():
    st.title("Page 1")
    st.write("This is the page with figs.")
    add_2_cols(link1="https://placekitten.com/300/300",
               link2="https://www.animalfriends.co.uk/siteassets/media/images/article-images/cat-articles/38_afi_article1_caring-for-a-kitten-tips-for-the-first-month.png",
                im=True)


def page2():
    st.title("Page 2")
    st.write("This is the content of the page with videos.")
    add_2_cols(link1='https://www.youtube.com/watch?v=wjZofJX0v4M',
               link2 = 'https://www.youtube.com/watch?v=W3I3kAg2J7w',
               im=False)


def main():
    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

    # Display the selected page
    if page == "Page 1":
        page1()
    elif page == "Page 2":
        page2()

if __name__ == "__main__":
    main()