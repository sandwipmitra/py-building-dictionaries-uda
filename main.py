#Method 1: Using a for loop to create a set of counters

book_title =  ['great', 'great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin', 'gasby']

word_counter = {}
for word in book_title:
  if word not in word_counter:
    word_counter[word] = 1
  else:
    word_counter[word] = word_counter[word] + 1

# print(word_counter)
# for word in book_title:
#   if word not in word_counter:
#     word_counter[word] = 1
#   else:
#     word_counter[word] += 1

# print(word_counter)



#Method 2: Using the get method
for word in book_title:
  word_counter[word] = word_counter.get(word, 0) + 1
#Syntax
#dictionary.get(keyname, value)

# print(word_counter)

#more examples
cast = {
     "Jerry Seinfeld": "Jerry Seinfeld",
     "Julia Louis-Dreyfus": "Elaine Benes",
     "Jason Alexander": "George Costanza",
     "Michael Richards": "Cosmo Kramer",
      "Michael Richards": "Cosmo Kramer"
 }
print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
  print("{}, {}".format(key, value))