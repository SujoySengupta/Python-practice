'''
An ATM contains Indian Currency notes of 100,200,500 and 2000. Write a 
python program which calculates and displays the minimum number of notes 
required to be dispensed to meet the user’s requirement.

notes=[100,200,500,2000]
n2=[]
def amount(n1):
    for i in notes:
        count=0
        if n1>=i:
            count=n1//i
            n1=n1%i
            return n1
            
n1=int(input("enter amount "))
for i in notes:
    print(i,":",amount(n1))

'''
# Define the available notes
notes = [2000, 500, 200, 100]

# Define a function to calculate the minimum number of notes
def min_notes(amount):
  # Initialize a dictionary to store the number of notes for each denomination
  note_count = {}
  # Loop through the notes from highest to lowest
  for note in notes:
    # If the amount is greater than or equal to the note value
    if amount >= note:
      # Divide the amount by the note value and store the quotient as the number of notes
      note_count[note] = amount // note
      # Update the amount by taking the remainder of the division
      amount = amount % note
  # Return the note count dictionary
  return note_count

# Ask the user to enter the amount they want to withdraw
amount = int(input("Enter the amount you want to withdraw: "))

# Call the function and print the result
result = min_notes(amount)
print("The minimum number of notes required are:")
for note, count in result.items():
  print(f"{note} : {count}")
  