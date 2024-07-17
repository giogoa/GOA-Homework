#ნომერი1 დავალება
for i in range (30):
    print("GOA BEST")
    
#ნომერი2 დავალება
for numbers in range (5 , 150):
    print(numbers)
    
#ნომერი3 დავალება
for numbers in range (2 , 50 , 4):
    print(numbers)
    
#ნომერი4 დავალება
for i in range(10):
    print(f"{i} --------- GOA")
    
#ნომერი5 დავალება
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd") 
        
#ნომერი6 დავალება
number = int(input("შეიყვანეთ რიცხვი: "))
while number < 100:
    print(f"შეყვანილი რიცხვია {number}")
    number = int(input("შეიყვანეთ რიცხვი: "))
print("რიცხვი მეტია 100-ზე!")