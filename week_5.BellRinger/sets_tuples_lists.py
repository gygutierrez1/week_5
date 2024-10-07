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
#fruits = {"banana", "coconut","apple", "orange"}
#print(fruits)
#print(dir(fruits))
#print(dir(fruit))
#print(fruits[0])
#fruits.remove("apple")
#fruits. reverse()
#print (fruits)
#fruits.add ("pineapple" in fruits)
#print(fruits)
#fruits. remove("apple")
#print(fruits)
#cars = ("bmw", "maserati", "audi", "mercedes", "ferrari")
#print (f"these are list of cars:",(cars))
#cars.append("buggatti")
#print(cars)
#cars.remove ("maserati")
#print(cars)
#fruits(pop)
#fruits.clear()

#fruits = ("banana", "coconut","apple", "orange")
#print(fruits)
#print(fruits.index("apple"))
#print(fruits.count("coconut"))

# print(fruits)
#for fruit in fruits:
 #   print(fruit)




# dictionary = a collection of{key:value} pairs 
    # ordered and changeable, no duplicates

#capitals = {"USA": "Washingto D.C.",
  #          "India":"New Delhi",
 #          "China": "Beijing",
  #          "Russia":"Moscow" }

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
#capitals.pop("USA")
#print(capitals)
#capitals.clear("India")

#keys = capitals.keys()
#print(keys)

#values = capitals.values()
#for value in values():
 #   print(value)

#items = capitals.items()
#for  key, value in capitals.items():
 #   print(f"{key}: {value}")
    





#for car in cars:
   # print(car)
    #print(len(car))
    #carRequest = input = "add a new car please"
    #cars.append(carRequest)





# challenge 
    #create a list of friends 
    # make sure the ini8tial list is none

#friends = []
#friends.append("lily")
#friends.append("beth")
#friends.append("jennifer")
#friends.append("julie")
#friends.append("abby")
#print(friends)
# add a new friend to the ,list  add at least 5 friends
#remove a a friend
#friends.remove("jennifer")
# insert a friend at specific index maybe 2 
#friends.insert(2, 'ashley')
#print(friends)
#print the list of friends
# loop through the whole
#for friend in friends:
 #   print(len(friends))
  #  print(friend)
































    



















# # Sets##################################
# # Sets are unordered collections of unique elements
# # Sets are mutable
# # Sets are defined by curly braces {}
# #example of sets
# set1 = {1, 2, 3, 4, 5}  # set of integers
# set2 = {'apple', 'banana', 'cherry'}  # set of strings
# set3 = {1, 2, 3, 'apple', 'banana'}  # mixed set
# set4 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}  # duplicate elements are removed


# #access elements in a set
# print(set1)
# print(1 in set1)
# print(6 in set1)
# print("apple" in set2)
# print("banana" in set3)
# # you cannot access elements in a set by index because sets are unordered
# # instead you can convert the set to a list and access elements by index
# #we use sets when we want to store unique elements 
# # and we don't care aboout the order of the elements
# #and we don't want the elements to be changed 


# # add elements to a set
# print(set1.add(6))
# print(set2.add('orange'))
# print(set3.add('coconut'))
# print(set4.add(13))

# #remove elements from a set
# print(set1.remove(6))
# print(set2.remove('orange'))
# print(set3.remove('coconut'))
# print(set4.remove(13))

# #check if an element is in a set
# print(1 in set1)
# print


# #find the length of a set


# #clear a set




# #tuples##################################
# # Tuples are ordered collections of elements
# # Tuples are immutable
# # Tuples are defined by parentheses ()
# #example of tuples
# tuple1 = (1, 2, 3, 4, 5)  # tuple of integers
# tuple2 = ('apple', 'banana', 'cherry')  # tuple of strings
# tuple3 = (1, 2, 3, 'apple', 'banana')  # mixed tuple
# tuple4 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)  # duplicate elements are allowed


# #access elements in a tuple
# print(tuple1)
# print(tuple1[0])
# print(tuple2[1])
# print(tuple3[2])


# #find the length of a tuple
# print(len(tuple1))   #output
# print(len(tuple2))


# #count the number of occurrences of an element in a tuple
# print(tuple4.count(1))   #output 2



# #find the index of an element in a tuple
# print(tuple2.index('banana'))
# print(tuple2.index('cherry'))

# #convert a tuple to a list
# print(list(tuple1))

# #convert a list to a tuple
# print(tuple(list))







#######################tuples challenge#####################
# Challenge: Count the number of occurrences of the character 'v' in the text below.
# The text is converted to a tuple of characters and the target characters are 'v' and 'V'.
# The result is output to the console.
#queue the videos(2)
# text = """Voilà! In view, a humble vaudevillian veteran, cast vicariously as both victim and villain by the vicissitudes of Fate.





# dictionarys Accessing a Value from a Nested List###############################
#Suppose we have a dictionary containing multiple lists as values, and you want to access a specific element from one of these lists.
# Define the dictionary


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# get length of the list

print(len(sample_list))
 # Output: 3
#this is called a nested list
# Extract and print the second element from the first list
print(sample_list[0][1])
print(sample_list[1][2])
print(sample_list[2][0])


sample_list_of_fruit = {"fruits": ["apple", "banana", "cherry"]}
# Extract and print the second fruit from the list
print(sample_list_of_fruit["fruits"][1])
print(sample_list_of_fruit["fruits"][2])
print(sample_list_of_fruit["fruits"][0])

sample_list_of_lists = {"lists": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
# Extract and print the third element from the second list
print (sample_list_of_lists["lists"][1][-1])
print (sample_list_of_lists["lists"][2][1])
print (sample_list_of_lists["lists"][0][-1])
print (sample_list_of_lists["lists"][-1][0])

sample_list_of_dicts = {"dicts": [{"name": "Alice", "age": 25}, 
                                  {"name": "Bob", "age": 30}, 
                                  {"name": "Charlie", "age": 35}]}
# Extract and print the age of the second person

print(sample_list_of_dicts["dicts"][1]["age"])
print(sample_list_of_dicts["dicts"][-1]["name"])
print(sample_list_of_dicts["dicts"][0]["age"])




data = {
    "fruits": {"tropical": ["mango", "pineapple", "banana"], "berries": ["strawberry", "blueberry", "raspberry"]},
    "prices": {"mango": 1.5, "pineapple": 2.5, "banana": 0.5}
}


# Extract and print the second item from the 'tropical' list
print(data["fruits"]["tropical"][1])  # Output: 'pineapple'
print(data["fruits"]["berries"][-1])
print(data["prices"]["mango"])
print(data["prices"]["banana"])



# Define the dictionary
info = {
    "team": {"coach": {"name": "John Doe", "age": 45}, "players": ["Alice", "Bob", "Charlie"]},
    "location": "New York"
}


# Extract and print the coach's name
print(info["team"]["coach"]["name"])  # Output: 'John Doe'
print(info["team"]["coach"]["age"])
print(info["team"]["players"][-1])
print(info["location"])




# Define the dictionary
company = {
    "departments": {
        "HR": {
            "employees": ["Emma", "Oliver", "Sophia"],
            "budget": 50000
        },
        "Engineering": {
            "employees": ["Liam", "Noah", "Ethan"],
            "budget": 120000
        }
    }
}


# Extract and print the second employee from the 'Engineering' department
print(company["departments"]["Engineering"]["employees"][1])  # Output: 'Noah'

print(company["departments"]["Engineering"]["budget"]) 

overall_budget = (company["departments"]["Engineering"]["budget"]) + (company["departments"]["HR"]["budget"])
print(overall_budge)

# Define the dictionary
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


# Print the updated dictionary
print(school)


# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
orange_quantity = product_inventory["warehouse1"]["quantities"][1]
print(f"Total oranges in warehouse1: {orange_quantity}")  # Output: 30




#Define the dictionary
cities = {
    "USA": {
        "New York": {"population": 8000000, "mayor": "John"},
        "Los Angeles": {"population": 4000000, "mayor": "Mike"}
    },
    "Canada": {
        "Toronto": {"population": 2700000, "mayor": "Jane"},
        "Vancouver": {"population": 630000, "mayor": "Emily"}
    }
}


#Extract and print the population of Los Angeles
la_population = cities["USA"]["Los Angeles"]["population"]
print(f"Population of Los Angeles: {la_population}")  # Output: 4000000





