list = ["Gururaj", "shahid", "yash", "azar"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])  #assenssing

list[2]=10   #updated
print(list) 

list.append("harsh")  #adding
print(list)

list.insert(3,"Akash") #adding index wise
print(list)

list.extend([86,75,82,81])  #butch of elements adding
print(list)

list.remove(10)  #removing element
print(list)

list.pop(0)   #removing element index wise
print(list)

del list[3]    #removing element index wise
print(list)

print(len(list))  #calculate length of list

if 6 in list:
    print("Element is present")
else:
    print("Element is not present")
    

for i in list:
    print(i)  #list traverse
    
    
print(list.count("azar"))  #counting

print(list.index("shahid")) #index finding
    
    
        
list1 = [2,22,76,62,82,12,]
list1.sort(reverse=True)  
print(list1)


list1.sort()
print(list1)


list1.reverse()
print(list1)

list2 = []
list2 = list1.copy()
print(list2)


list2.clear()
print(list2)


print("------------------------------------------------------------------------------------------------------------")






student = [["English-",89],["Marathi-",90],["maths-",86],["science-",82],["hindi-",88]]
print(student)

 
student.append(["history-",77]) 
print(student)
    
for i in student:
    print(i[0],i[1])
    