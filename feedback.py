feedback = input("Enter Your Feedback : ")
print("Feedback Formated Report".center(120).upper())
print("---------------------------------".center(120))

print("Original Feedback : ".title())
print(feedback)
print("------------------------------------------------------------")

print("feedback summary-".title())
print("Total Character Count : ".title(),len(feedback))
print("Total Words Count     : ".title(),len(feedback.split()))
spaces = feedback.count(" ")

print("Total spaces count    :".title(), spaces)
print("Total exlamation marks count :".title(),(feedback.count("!")))

print("-------------------------------------------------------------")

print("formated feedback :-".title())

print("Lower Case Feedback : ".title(),feedback.lower())
print("upper case feedback : ".title(),feedback.upper())
print("capitalize feedback : ".title(),feedback.capitalize())
print("title feedback : ".title(),feedback.title())
print("swapcase feedback : ".title(),feedback.swapcase())

print("----------------------------------------------------------------")

print("profissional feedback : ".title())
print(feedback.capitalize())


print("----------------------------------------------------------------")

print("word list: ".title())
print(feedback.split())

print("----------------------------------------------------------------")


print("-------Thank you for your valuable feedback---------".title().center(120))




