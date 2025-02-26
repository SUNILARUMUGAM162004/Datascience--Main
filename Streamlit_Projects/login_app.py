import streamlit as st
st.set_page_config(page_title="Login Page", layout="centered")
def set_bg_hack_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://img.freepik.com/free-photo/futuristic-metaverse-empty-room-product-display-presentation-abstract-technology-scifi-with-neon-light-3d-background_56104-2314.jpg?semt=ais_hybrid");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
set_bg_hack_url()
st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
col1, col2 = st.columns(2)
with col1:
    submit_button = st.button("Submit")
with col2:
    cancel_button = st.button("Cancel")
# Logic for Submit and Cancel buttons
if submit_button:
    if username == "Sunil" and password == "Sunilarumugam":  # Replace with your authentication logic
        st.success("Login Successful!")
    else:
        st.error("Invalid Username or Password")
if cancel_button:
    st.warning("Login Cancelled")
