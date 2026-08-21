marks = []

while True:
    print("----------Student Marks Management---------")
    print("1.Insert Marks")
    print("2.Diplay Marks")
    print("3.Delete Marks")
    print("4.Update Marks")  
    print("5.Exit")


    choice = int(input("Enter your choice :"))


    if choice == 1:
        mark =int(input("Enter your marks : "))
        marks.append(mark)
        print("Marks inserted successfully")


    elif choice == 2:
        if  len(marks) == 0:
            print("Empty Marks...")
        else:
            print("Student Marks-")
            for i in range(len(marks)):
                print("Student", i + 1 , "=", marks[i])
            


    elif choice == 3:
        student = int(input("Enter Student number for delete :"))
        if 1 <= student <= len(marks):
            marks.pop(student - 1)
            print("Deleted successfully")
        else:
            print("Invalid Number")


    elif choice == 4:
        student = int(input("Enter Student number for update : "))
        if 1 <= student <= len(marks):
            new_marks = int(input("Enter Marks :"))
            marks[student - 1]=new_marks
            print("Marks updated successfully")
        else:
            print("Invalid Student Number")


    elif choice == 5:
        print("Thank You...")
        breaks
    else:
        print("Invalid Choice")


    