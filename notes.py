'''
#An ATM contains Indian Currency notes of 100,200,500 and 2000. Write a 
#python program which calculates and displays the minimum number of notes 
#required to be dispensed to meet the user’s requirement

notes=[2000, 500, 200, 100]
amt=int(input("Enter amount to be withdrawn: "))
for i in notes:
    if i<=amt:
        #print(i)
        #i+=i
        amt-=i
        if amt==0:
            break
        print(i)

# Define a list of available notes in the ATM
notes = [2000, 500, 200, 100]

# Ask the user to enter the amount they want to withdraw
amount = int(input("Enter the amount you want to withdraw: "))

# Initialize a variable to store the total number of notes
total_notes = 0

# Print a message to indicate the start of the calculation
print("The minimum number of notes required are:")

# Loop through the notes list from highest to lowest
for note in notes:
  # Find the number of notes of the current denomination that can be dispensed
  num_notes = amount // note
  # Update the amount by subtracting the value of the dispensed notes
  amount = amount - (num_notes * note)
  # Update the total number of notes by adding the number of notes of the current denomination
  total_notes = total_notes + num_notes
  # Print the number of notes of the current denomination if it is positive
  if num_notes > 0:
    print(f"{num_notes} notes of Rs. {note}")

# Print the total number of notes
print(f"Total number of notes: {total_notes}")

# Given data: grocery items and their costs
price = [('item1', '17.20'), ('item2', '15.10'), ('item3', '24.5')]

# Sort the items based on price (convert prices to float for sorting)
sorted_items = sorted(price, key=lambda x: float(x[1]))

# Display the sorted items
for item, cost in sorted_items:
    print(f"{item}: ${cost}")

# The second costliest item
second_costliest_item = sorted_items[1][0]
print(f"\nThe second costliest item is {second_costliest_item}.")
'''
# Given data: list of tuples containing 2D coordinates
data = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Separate x and y coordinates into separate lists
x_list = []
y_list = []

for x, y in data:
    x_list.append(x)
    y_list.append(y)

# Display the separated coordinates
print(f"X_list: {x_list}")
print(f"Y_list: {y_list}")
