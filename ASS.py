
def check_exam_eligibility(attendance_percentage):
    if attendance_percentage >= 75:
        print("You are eligible to attend the exam.")
    else:
        print("You are not eligible to attend the exam due to insufficient attendance.")

attendance = float(input("Enter your attendance percentage: "))


check_exam_eligibility(attendance)
