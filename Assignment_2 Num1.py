# Initialize an empty list to store the results
result = []

# Loop through the range from 2000 to 3200
for number in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if number % 7 == 0 and number % 5 != 0:
        result.append(number)
print(result)

