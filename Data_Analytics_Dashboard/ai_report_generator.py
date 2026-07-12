import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)
data = pd.read_csv(
    "student_data.csv"
)
average_exam = data["Exam"].mean()

average_attendance = data["Attendance"].mean()

average_study = data["Study_Hours"].mean()


summary = f"""

Student Performance Summary:


Number of students:
{len(data)}


Average examination score:
{average_exam:.2f}


Average attendance:
{average_attendance:.2f}%


Average weekly study hours:
{average_study:.2f}


Students below 60 marks:

{data[data["Exam"] < 60]["Student"].tolist()}

"""
response = client.chat.completions.create(

model="gpt-4.1-mini",

messages=[

{
"role":"system",
"content":
"""
You are an educational data analyst.
Analyse student performance data.
Provide recommendations for teachers.
"""
},

{
"role":"user",
"content":summary
}

]

)
report = response.choices[0].message.content


print(
"AI EDUCATIONAL REPORT"
)


print(report)
