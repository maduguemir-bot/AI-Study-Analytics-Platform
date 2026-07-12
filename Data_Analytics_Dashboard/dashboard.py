import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Title

st.title(
"AI Student Performance Analytics Dashboard"
)


st.write(
"This dashboard analyses student academic performance."
)


# Load data

data = pd.read_csv(
"student_data.csv"
)


# Display data

st.subheader(
"Student Records"
)

st.dataframe(data)



# Average exam score

average_exam = data["Exam"].mean()


st.metric(
"Average Exam Score",
round(average_exam,2)
)
st.subheader(
"Student Exam Performance"
)


chart = plt.figure(figsize=(8,4))


plt.bar(
data["Student"],
data["Exam"]
)


plt.xticks(
rotation=45
)


plt.xlabel(
"Students"
)


plt.ylabel(
"Exam Score"
)


plt.title(
"Examination Results"
)


st.pyplot(chart)
st.subheader(
"Attendance Analysis"
)


chart2 = plt.figure(figsize=(8,4))


plt.scatter(
data["Attendance"],
data["Exam"]
)


plt.xlabel(
"Attendance Percentage"
)


plt.ylabel(
"Exam Score"
)


plt.title(
"Attendance vs Academic Performance"
)


st.pyplot(chart2)
st.subheader(
"Search Student"
)


student = st.selectbox(
"Select Student",
data["Student"]
)


student_record = data[
data["Student"] == student
]


st.write(
student_record
)
st.subheader(
"Students Needing Support"
)


weak_students = data[
data["Exam"] < 60
]


st.warning(
"Students requiring academic support"
)


st.dataframe(
weak_students
)
st.subheader(
"AI Recommendations"
)


st.write(
"""
Based on the analysis:

1. Students with low attendance need monitoring.

2. Students with low study hours require mentoring.

3. Additional revision support should be provided.

"""
)
from ai_report_generator import generate_report
if st.button(
"Generate AI Report"
):

    report = generate_report()

    st.subheader(
    "AI Teacher Report"
    )

    st.write(report)
with open(
"AI_Performance_Report.txt",
"w"
) as file:

    file.write(report)
