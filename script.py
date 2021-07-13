from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
# stacks.append(left_stack)
# stacks.append(middle_stack)
# stacks.append(right_stack)
# instead of doing append 3 times, do below:
stacks += [left_stack, middle_stack, right_stack]

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))
#Get User Input: helper function to prompt users to choose a stack
def get_input():
  #choices = [left_stack.get_name(), middle_stack.get_name(), right_stack.get_name()]
# instead of the above
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
#Play the Game
