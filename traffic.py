print("---------Traffic Signals---------")

signal = input("Enter a Signal color : ").lower()

if signal == "red":
    print("The signal is red")
    print("Stop")
    
elif signal == "yellow":
    print("The signal is yellow")
    print("Ready to Go")
    
elif signal == "green":
    print("The signal is green")
    print("Go")
    
else:
    print("Invalid color!!..enter red,green or yellow")
    