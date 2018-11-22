"""
This is not
going to be
read!
"""
print("This is read")  # This will not be read as.
"""
This is not
going to be
read as well!
"""










































number = 10

floating = 0.35

booleon = True

word = "Chicken"

listOfItems = ["Apple", word, "Milk", "Cake"]

dictionary = {
    "Chicken": 10.60,
    "Apple": 5.99,
    "Milk": 2.99,
    "Cake": 25
}




print("In the list we got:")
for item in listOfItems:
    print("> " + item)




item = "Cake"

print("Welcome, " + item + " will cost £" + str(dictionary[item]))




























number = input("Change the number to:")
number = int(number)


for x in range(0, number):
    print("Boom number " + str(x))


































def autoPoof(aWord):
    print("I must say that I will POOF the " + aWord)
    print("Also I love Chicken")
    print("It is tasty")




x = 0
while x != 10:
    autoPoof("Minecraft")
    x = x + 1





x += 1






























class Cat:
    def __init__(self):
        self.name = "(No name)"

    def changeName(self, name):
        self.name = name

    def sayName(self):
        print("My name is " + self.name)

    def attack(self):
        print(self.name + " attacks")



josh = Cat()

josh.changeName("Bob")

josh.sayName()



noNameCat = Cat()

noNameCat.sayName()


























class Store:
    def __init__(self):
        self.prices = {}

    def addItem(self, item, price):
        self.prices[item] = price

    def buyItem(self, item):
        if item in self.prices:
            print("You have purchesed " + item + " for " + str(self.prices[item]) + "!")
        else:
            print("Sorry we don't have " + item + " in the store.")

    def removeItem(self, item):
        if item in self.prices:
            print("Removed " + item + "from the store!")
            del self.prices[item]
        else:
            print("This item does not existed in the store!")

    def printItems(self):
        print("We have these items currently in the store:")
        for item in self.prices.items():
            print("> " + item[0] + " for £" + str(item[1]))



















