# Student Performance Analytics Dashboard


import pandas as pd


data = pd.read_csv(
    "student_data.csv"
)


print("==============================")
print("STUDENT PERFORMANCE ANALYSIS")
print("==============================")


print("\nStudent Records:")
print(data)



# Average scores

average_exam = data["Exam"].mean()

average_assignment = data["Assignment"].mean()

average_attendance = data["Attendance"].mean()


print("\nAverage Exam Score:")
print(round(average_exam,2))


print("\nAverage Assignment Score:")
print(round(average_assignment,2))


print("\nAverage Attendance:")
print(round(average_attendance,2))


# Highest performer

top_student = data.loc[
data["Exam"].idxmax()
]


print("\nBest Performing Student:")

print(top_student["Student"])
