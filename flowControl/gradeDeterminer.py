grade = float(input("Type the student's grade."))

if grade >= 60:
    if grade >= 70:
        if grade >= 80:
            if grade >= 90:
                print("Grade A")
            else:
                print("Grade B")
        else:
            print("Grade C")
    else:
        print("Grade D")
else:
    print("Grade F")
