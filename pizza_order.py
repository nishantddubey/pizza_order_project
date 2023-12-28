menu = '''------- Menu ---------
Small Pizza  - Rs 200
Medium Pizza - Rs 350
Large Pizza  - Rs 500 
----------------------\n'''
print(menu)
bill = 0
order = input("Select the order S - Small,M-medium,L-Large Pizza: ")
if order=="S" or order =="s":
    bill+=200
    pepperoni = input("Do you want Pepperoni (Y/N): ")
    if pepperoni == "Y" or pepperoni == "y":
            bill += 20
    extra_cheese = input("Do you want extra cheese: (Y/N)")
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 50
elif order=="M" or order =="m":
    bill+= 350
    pepperoni = input("Do you want Pepperoni (Y/N): ")
    if pepperoni == "Y" or pepperoni == "y":
            bill += 50
    extra_cheese = input("Do you want extra cheese: (Y/N)")
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 50
elif order=="L" or order=="l":
    bill+=500
    pepperoni = input("Do you want Pepperoni (Y/N): ")
    if pepperoni == "Y" or pepperoni == "y":
            bill += 50
    extra_cheese = input("Do you want extra cheese: (Y/N)")
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 50
else:
    print("This size is not available!!")
print("\n")

print(f"Your Total Bill is Rs:{bill}")
print("THANKS FOR USING OUR PLATFORM!!!")
