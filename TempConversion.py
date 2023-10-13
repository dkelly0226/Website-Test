user = str(input("Please enter your name: "))
print(f"Hello {user}")
tempType = str(input("Please select an initial temperature type, F or C: "))
initialTemp = float(input("Please enter a temperature for conversion: "))

def toC():
    finalTemp = (initialTemp - 32)/1.8
    print(f"{finalTemp} degrees C")

def toF():
    finalTemp = (initialTemp * 1.8) + 32
    print(f"{finalTemp} degrees F")


if tempType == 'F' or tempType == 'f':
    toC()

elif tempType == 'C' or tempType == 'c':
    toF()

else:
    print("Sorry, please try again.")
