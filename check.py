# Python program to check if a student can enrol based on age criteria

def check_age_eligibility(age):
    if 10 <= age <= 20:
        return "Eligible for enrolment."
    else:
        return "Not eligible for enrolment."

# Example usage
try:
    student_age = int(input("Enter the student's age: "))
    eligibility = check_age_eligibility(student_age)
    print(eligibility)
except ValueError:
    print("Invalid input! Please enter a valid age.")
