product = []
prize = []

while True:
    print("----product management-----")
    print("1.Add product ")
    print("2.Display Products ")
    print("3.Update products ")
    print("4.Delete product ")
    print("5.Search product ")
    print("6.Sort ")
    print("7.Exit ")


    choice = int(input("Enter your Choice : "))

    if choice == 1:
        product1 = input("Enter Adding Product :")
        prize1 = input("Enter product prize : ")
        product.append(product1)
        prize.append(prize1)
        print("Product Inserted Successfully....")

    elif choice == 2:
        if len(product) == 0:
            print("Product is Not Available ")
        else:
            print("product\tprize")
            for i in range(len(product)):
                
                print(product[i],"\t",prize[i])

    elif choice == 3:
        product2 = input("Enter product name to update prize:")
        if product2 in product:
            product.index(product2) 
            index = product.index(product2) 
            new_prize = input("Enter updated prize : ")
            prize[index] = new_prize
            print("Prize Update is Successful")
        else:
            print("New Prize is Not Found")

    elif choice == 4:
        product3 = input("Enter product name for delete: ")
        if product3 in product:
            index = product.index(product3)
            product.pop(index)
            prize.pop(index)
            print("Product Deleted Successfully...")
        else:
            print("Product is Not Found...")

    elif choice == 5:
        product4 = input("Enter product name for search : ")
        if product4 in product:
            index = product.index(product4)
            print("Your Search Product is Here,,")
            print("product\tprize")
            print(product[index],"\t",prize[index])
             
        else:
            print("Product is Not Available")

    elif choice == 6:
            for i in range(len(product)):
                for j in range(i + 1, len(product)):
                    if prize[i] > prize[j]:
                        prize[i], prize[j] = prize[j], prize[i]
                        product[i], product[j] = product[j], product[i]

            print("Sorted Successfully")
            print("Products:", product)
            print("Prices:", prize)


    elif choice == 7:
        print("Thank You......")
        break

    else:
        print("Invalid choice..")

        




