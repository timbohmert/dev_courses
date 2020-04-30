#Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.

#The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

#The game follows three rules:

#1. Only one disk can be moved at a time.
#2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
#3. No disk may be placed on top of a smaller disk.

#In this project, we are going to use our knowledge of stacks to implement this game! Let’s get started!


#using stack.py with class for Stack with methods for push(), pop(), peek(), has_space(), is_empty(), get_size(), get_name(), print_items()



#creating stacks

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

#instantiation of stack class for left, middle and right stacks
left_stack = Stack('Left')

middle_stack = Stack('Middle')

right_stack = Stack('Right')

stacks.append(left_stack)

stacks.append(middle_stack)

stacks.append(right_stack)


#Set up the Game

#input asking the user to input the number of disks they want to play with, with a while loop that requires the user to input at least three disks
num_disks = int(input("\nHow many disks do you want to play wth?\n"))

while num_disks < 3:
    num_disks = int(input('Enter a number greater than or equal to 3.\n'))


#for loop that iterates through the list of range of disks and pushes them to the left stack

for i in range(num_disks, 0, -1):
    left_stack.push(i)


#calculate the number of optimal moves. towers of hanoi, number of optimal moves is alwayy (2^number of disks) - 1

num_optimal_moves = 2 ** num_disks - 1

print('\nThe fastest you can solve this game is in {0} moves'.format(str(num_optimal_moves)))




#Get User Input

#helper function that prompts users to choose a stack. User will decide on the stack with the first letter of the desired stack to place the item (L for Left)

def get_input():

    #list of the first letter in each of the stack names (L for Left)
    choices = [stack_name.get_name()[0] for stack_name in stacks]
    
    
    while True:

        #relate the name of the stack (Left) to the choice letter (L) and relay these to the user
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {0} for {1}'.format(letter, name))
        
        #user inputs on the stack options with first letter of the stack name (L, R, M)
        user_input = input('')

        #conditional statement to check the stack that the user chose based on user_input
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


        
#Play the Game

num_user_moves = 0


#loop that allows the user to continue playing until all of the disks are on the right stack
while right_stack.get_size() != num_disks:
    
    #code to print the stacks and the disks that are on each of the stacks
    print('\n\n\n...Current Stacks...')
    for i in stacks:
        i.print_items()

    
    while True:

        #asking the user which stack they want to move a disk from
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()

        #asking a user which stack they want to move a disk to
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()


        #determines if the stack that the user chose to move a disk from is empty
        if from_stack.is_empty():
            print('\n\nInvalid Move. Try Again.')


        #determines that it is valid and pops the disk from the from_stack and pushes it to the to_stack
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        #statement that prints if trying to move a disk larger than the disk on the to_stack
        else:
            print('\n\nInvalid Move. Try Again.')


#statement that prints once the user has successfully put all of the disks on the right stack. Compares the number of moves made compared to the optimal moves that could be made.
print('\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}.'.format(num_user_moves, num_optimal_moves))











           

