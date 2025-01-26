#Asking users for list & target
string = input("Enter the your list: ")
target1 = int(input("Enter the target number: "))
#Replacing the brackets with nothing
string1 = string.replace("[","")
string1 = string1.replace("]","")
#We format the list
list1 = string1.split(",")
#We set the times we iterate through
iterations = -1
#We check for each number and add 1 iteration every time
for number in list1:
    iterations += 1
    #If the number doesn't equal target 1 we continue
    if int(number) != int(target1):
        continue
    else:
        #If the number equals target 1 we print what iteration we found it on and then break
        print(iterations)
        break
'''This happens if we continue, and then we find the length of the list1 and then we minus 1 because
we need to check if it checked the whole list because we started at 0 for our index
'''
if iterations == len(list1) -1:
    print(-1)


