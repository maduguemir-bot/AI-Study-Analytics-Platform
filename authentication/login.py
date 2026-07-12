import streamlit as st


def login():

    st.subheader(
    "User Login"
    )


    username = st.text_input(
    "Username"
    )


    password = st.text_input(
    "Password",
    type="password"
    )


    if st.button("Login"):

        if username=="teacher":

            st.success(
            "Welcome Teacher"
            )

        else:

            st.error(
            "Invalid Login"
            )
