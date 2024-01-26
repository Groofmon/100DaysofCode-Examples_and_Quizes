# Input a Python list of student heights
student_heights = input("Enter each height you would like to and Ensure there is a gap between each number you enter!\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students_num = 0
total_height = 0
for i in student_heights:
  total_height += i
  students_num+=1

print(f"total height = {total_height}\nnumber of students = {students_num}\naverage height = {total_height/students_num}")
