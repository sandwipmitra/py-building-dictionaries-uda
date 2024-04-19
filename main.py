#Method 1: Using a for loop to create a set of counters

book_title =  ['great', 'great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin', 'gasby']

word_counter = {}
for word in book_title:
  if word not in word_counter:
    word_counter[word] = 1
  else:
    word_counter[word] = word_counter[word] + 1

print(word_counter)


#Method 2: Using the get method