############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Hannes Meyer-Rahlfs

def grade_to_numeric(course_name):
   
    print(f"\nEnter your grade for {course_name}:")
    letter_grade = input("Letter grade (A, B, C, D, F): ").upper().strip()
    modifier = input("Modifier (+, -, or leave blank): ").strip()

    if letter_grade == "A":
        grade = 4.0
    elif letter_grade == "B":
        grade = 3.0
    elif letter_grade == "C":
        grade = 2.0
    elif letter_grade == "D":
        grade = 1.0
    elif letter_grade == "F":
        grade = 0.0
    else:
        print("Invalid grade.")
        return None

    if modifier == "+" and letter_grade != "A" and letter_grade != "F":
        grade += 0.3
    elif modifier == "-" and letter_grade != "F":
        grade -= 0.3
    elif modifier == "+" or modifier == "-":
        print("Modifier not valid for this grade.")

    if grade > 4.0:
        grade = 4.0

    return grade


def main():
    print("Welcome to the Grade Point Average (GPA) Calculator!")
    print("please enter final letter grades for six courses in the promted area below.")
    print("Valid letter grades are A, B, C, D, and F.")
    print("Modifiers can only be +, - or no modifier at all.\n")
    
    courses = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1001"]
    total = 0
    grades = []

    for course in courses:
        grade = grade_to_numeric(course)
        if grade is not None:
            grades.append((course, grade))
            total += grade
    if grades:
        print("\nHere's a summary of your grades:")
        print("=" * 40)
        print(f"{'Course':<15}{'Numeric Grade':>15}")
        print("-" * 40)

        for course, grade in grades:
            print(f"{course:<15}{grade:>15.1f}")

        print("=" * 40)
        gpa = total / len(courses)
        print(f"\nYour GPA is: {gpa:.1f}")
        print("=" * 50)
    else:
        print("Error with input. Please try again.")


# PROGRAM EXECUTION STARTS HERE
main()
