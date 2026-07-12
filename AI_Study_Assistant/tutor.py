import streamlit as st


def tutor():

    st.subheader(
    "Ask AI Tutor"
    )


    question = st.text_input(
    "Enter your question"
    )


    if st.button("Ask"):

        st.write(
        "AI Response:"
        )

        st.write(
        "This is where ChatGPT response appears."
        )
