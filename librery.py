librery = {}

while True:

    print("-------Welcome to Librery------")
    print("1.Add Books")
    print("2.Diplay Books")
    print("3.Search Book")
    print("4.Update Books")
    print("5.Exit")

    choice = int(input("Enter your Choice :"))

    if choice == 1:
        book_id = int(input("Enter Book ID : "))
        book_name = input("Enter Book Name : ")
        author_name = input("Enter Author Name :")
        book_price = int(input("Enter Book Price :"))

        librery[book_id]={"book_name":book_name,
                            "author_name":author_name,
                            "book_price":book_price}
        print("Book Added Successfully..")


    elif choice == 2:
        print(librery)


    elif choice == 3:
        search = int(input("Enter Book ID for Search: "))
        if search in librery:
            print(librery[search])
        else:
            print("invalid ID")


    elif choice == 4:
        Id = int(input("Enter Book ID for Update : "))
        if book_id == Id:
            new_book_name = input("Enter Updated Book Name : ")
            new_author_name = input("Enter Updated Author Name :")
            new_book_price = int(input("Enter Updated Book Price :"))

            librery[Id]={"book_name":new_book_name,
                            "author_name":new_author_name,
                            "book_price":new_book_price}

            print("New Book Updated Successfully..")
        else:
            print("Invalid Id")

        
    
        
    elif choice == 5:
        
        print("Thank you..")
        break




         




    

    

    




    
