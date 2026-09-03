product = []
prize = []

while True:
    print("----product management-----")
    print("1.Add product: ")
    print("2.Display Products: ")
    print("3.Update products: ")
    print("4.Delete product: ")
    print("5.Search product: ")
    print("6.Sort : ")
    print("7.Exit: ")


    choice = int(input("Enter your Choice : "))

    if choice == 1:
        product1 = input("Enter Adding Product :")
        prize1 = input("Enter product prize : ")
        product.append(product1)
        prize.append(prize1)
        print("Product Inserted Successfully....")

    elif choice == 2:
        if len(product) == 0:
            print("product is not available ")
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
            


        



                
                
    

        
        


