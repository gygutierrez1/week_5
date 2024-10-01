#collection = single "variable" used to store multiple values
# list = [] ordered and changeable duplicates OK
# set = [] unordered and immutable, but ADD/REMOVE OK, NO duplicates
# Tuple = () ordered ab=nd unchangeable , Duplicates OK 

#fruits = ["apple", "orange", "banana" ,"coconut"]
# print(fruits{0:3})
#for fruit in fruits:
 #   print(fruit)

#help(fruits)
#print(help(fruits))
#print(len(fruits))
#list = []
#Set = {}
#Tuple = ()
# you can reassign value using this:
#print (fruit)
fruits = {"banana", "coconut","apple", "orange"}
print(fruits)
#print(dir(fruits))
#print(dir(fruit))
#print(fruits[0])
#fruits.remove("apple")
#fruits. reverse()
#print (fruits)
#fruits.add ("pineapple" in fruits)
#print(fruits)
fruits. remove("apple")
print(fruits)
#cars = ("bmw", "maserati", "audi", "mercedes", "ferrari")
#print (f"these are list of cars:",(cars))
#cars.append("buggatti")
#print(cars)
#cars.remove ("maserati")
#print(cars)
#fruits(pop)
#fruits.clear()

fruits = ("banana", "coconut","apple", "orange")
print(fruits)
print(fruits.index("apple"))
print(fruits.count("coconut"))

# print(fruits)
for fruit in fruits:
    print(fruit)




# dictionary = a collection of{key:value} pairs 
    # ordered and changeable, no duplicates

capitals = {"USA": "Washingto D.C.",
            "India":"New Delhi",
           "China": "Beijing",
            "Russia":"Moscow" }

#print(dir(capitals))
#print(help(capitals))
#capitals.get("USA")

#if capitals.get("USA"):
 #   print("That capital exists")
#else:
 #   print("That capital doesn't exist")    


##capitals.update({"Germany":"Berlin"})
#capitals.pop("China")
#print(capitals)
#capitals.popitem()
#print(capitals)
#capital.clear()

keys = capitals.keys()
print(keys)

values = capitals.values()
for value in values():
    print(value)

items = capitals.items()
for  key, value in capitals.items():
    print(f"{key}: {value}")
    





#for car in cars:
   # print(car)
    #print(len(car))
    #carRequest = input = "add a new car please"
    #cars.append(carRequest)





# challenge 
    #create a list of friends 
    # make sure the ini8tial list is none

friends = []
friends.append("lily")
friends.append("beth")
friends.append("jennifer")
friends.append("julie")
friends.append("abby")
print(friends)
# add a new friend to the ,list  add at least 5 friends
#remove a a friend
friends.remove("jennifer")
# insert a friend at specific index maybe 2 
friends.insert(2, 'ashley')
print(friends)
#print the list of friends
# loop through the whole
for friend in friends:
    print(len(friends))
    print(friend)


    