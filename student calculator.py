while True:
    print("\nGrade Calculator")

    number = int(input("Enter student number: "))
    name = input("Enter student name: ")
    course = input("Enter student course: ")
    prelim = float(input("Prelim score: "))
    midterm = float(input("Midterm score: "))
    final = float(input("Final score: "))

    average = (prelim * 0.20) + (midterm * 0.30) + (final * 0.50)

    if average >= 75:
        remarks = "Passed"
    else:
        remarks = "Failed"
        
    print("\n--------RESULT--------------")    
    print("student number:", number)
    print("Student:", name)
    print("course", course)
    print("Average:", round(average, 2))
    print("Remarks:", remarks)
    print("------------------------------")

    choice = input("\nDo you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        break
