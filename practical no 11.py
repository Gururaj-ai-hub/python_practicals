bus = [["a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a"]]


for i in range(5):
    print(bus[i])

row = int(input("Enter your row number: "))
seat = int(input("Select your seat: "))

if bus[row - 1][seat - 1] == "a":
    bus[row - 1][seat - 1] = "r"
    print("Your seat is reserved!")
else:
    print("Seat is already booked!")


print("\nUpdated bus:")
for i in range(5):
    print(bus[i])
