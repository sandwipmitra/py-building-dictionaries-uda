#Method 1: Using a for loop to create a set of counters

# book_title =  ['great', 'great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin', 'gasby']

# word_counter = {}
# for word in book_title:
#   if word not in word_counter:
#     word_counter[word] = 1
#   else:
#     word_counter[word] = word_counter[word] + 1

# print(word_counter)
# for word in book_title:
#   if word not in word_counter:
#     word_counter[word] = 1
#   else:
#     word_counter[word] += 1

# print(word_counter)



#Method 2: Using the get method
# for word in book_title:
#   word_counter[word] = word_counter.get(word, 0) + 1
#Syntax
#dictionary.get(keyname, value)

# print(word_counter)

#more examples
# cast = {
#      "Jerry Seinfeld": "Jerry Seinfeld",
#      "Julia Louis-Dreyfus": "Elaine Benes",
#      "Jason Alexander": "George Costanza",
#      "Michael Richards": "Cosmo Kramer",
#       "Michael Richards": "Cosmo Kramer"
#  }
# print("Iterating through keys:")
# for key in cast:
    # print(key)

# print("\nIterating through keys and values:")
# for key, value in cast.items():
  # print("{}, {}".format(key, value))


#more examples
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

# result = 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# #Iterate through the dictionary
# for object, count in basket_items.items():
#   if object in fruits:
#     result += count 

# # if the key is in the list of fruits, add the value (number of fruits) to result

# print(result)

#example 2
# result = 0
# basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# for object, count in basket_items.items():
#   if object in fruits:
#     result += count 
# print(result)

##example 3

# result = 0
# basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# for object, count in basket_items.items():
#   if object in fruits:
#     result += count

# print(result)

##example 4
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
  
#if the key is in the list of fruits, add to fruit_count.
  if object in fruits:
    fruit_count += count

#if the key is not in the list, then add to the not_fruit_count
  elif object not in fruits:
    not_fruit_count += count

print(fruit_count, not_fruit_count)
