import streamlit as st

# Set page title
st.set_page_config(page_title="My Landing Page", page_icon=":house:")


def test_app():
    st.title("Test Page")

    # Add link to go to App page
    st.markdown("[Go to App Page](http://localhost:8502)")
# Add custom HTML and CSS
st.markdown("""
    <style>
        .header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .container {
            margin: 0 auto;
            max-width: 600px;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Header section with custom HTML
st.markdown("""
    <div class="header">
        <h1>Welcome to my Landing Page!</h1>
    </div>
""", unsafe_allow_html=True)
test_app()
# Container section with images and text
st.markdown("""
    <div class="container">
        <h2>About Me</h2>
        <img src="https://cdn.pixabay.com/photo/2023/04/06/10/22/earth-day-7903523_960_720.png" alt="Earth Day Image">
        <p>I'm a web developer with over 5 years of experience. I specialize in creating custom websites and web applications for businesses of all sizes.</p>
        <h2>Services</h2>
        <ul>
            <li>Website design and development</li>
            <li>Web application development</li>
            <li>E-commerce solutions</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Footer section with custom HTML
st.markdown("""
    <hr>
    <div class="container">
        <p>Thanks for visiting my landing page. Contact me at <a href="mailto:me@example.com">me@example.com</a> for more information.</p>
    </div>
""", unsafe_allow_html=True)
