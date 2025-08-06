# Get student details
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Get number of subjects
num_subjects = int(input("Enter number of subjects: "))
marks = []

# Collect marks dynamically
for i in range(num_subjects):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculations
total = sum(marks)
average = total / num_subjects

# Grade logic (twist: A+ if all marks are above 90)
if all(m > 90 for m in marks):
    grade = "A+ (Perfect Streak!)"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F (Uh-oh!)"

# Output
print("\n----- Student Report -----")
print("Name:", name)
print("Roll Number:", roll_number)
for i, m in enumerate(marks, start=1):
    print(f"Subject {i} Marks:", m)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
