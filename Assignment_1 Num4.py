print("Lets check to see if your words are anagrams")
s = input("What is you first word to check? ")
t = input("What is your second word to check? ")

my_dict = dict()
anagram = True

for letter in s:
    my_dict[letter] = my_dict.get(letter, 0) + 1

#print(my_dict)
#print(my_dict.__contains__('n'))

for letter in t:
    if my_dict.__contains__(letter) is False:
        print("This is not an anagram - One of the letters from 2nd string doesnt exist in 1st one")
        exit()
    else:
        #value = int(my_dict.get(letter))
        #print(my_dict.get(letter))
        my_dict[letter] = my_dict.get(letter) - 1  #update(letter, int(value - 1))

for letter in my_dict:
    if my_dict.get(letter) == 0:
       continue
    else:
       anagram = False
       break

if anagram is True:
   print("That is a anagram")
else:
   print("This is not an anagram - Total count between 2 string dont match")


#print(my_dict)


#anagram = True
'''
for char in s:
    if char in t:
        continue
    else:
        anagram = False
        break
if anagram is True:
    print("That is a anagram")
else:
    print("This is not an anagram")
'''
#anagrams = {}
