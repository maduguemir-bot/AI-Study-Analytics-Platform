import streamlit as st


st.title(
"AI Learning Management System"
)


st.write(
"""
Welcome to the AI Education Platform.

Features:

- AI Tutor
- Student Analytics
- Performance Reports

"""
)
import streamlit as st


page = st.sidebar.selectbox(

"Choose Module",

[
"Home",
"AI Tutor",
"Analytics Dashboard",
"Reports"
]

)


if page=="Home":

    st.title(
    "AI Learning Platform"
    )


elif page=="AI Tutor":

    st.title(
    "AI Study Assistant"
    )


elif page=="Analytics Dashboard":

    st.title(
    "Student Analytics"
    )


elif page=="Reports":

    st.title(
    "AI Reports"
    )
