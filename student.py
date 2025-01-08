students = []
student_append= input("enter student or type stop:\n")
while student_append != "stop":
    students.append(student_append)
    student_append = input("enter student or type stop:\n")

print(students)
