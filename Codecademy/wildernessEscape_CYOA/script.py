#Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose. Let’s get started!

#mission provided by Codecademy


print('Once upon a time... ')


######
# TREENODE CLASS
######


#treenode class that will keep track of portion of the story and choices user can make to progress story
class TreeNode:

    #constructor for declaring story_piece that will be placed into each node and empty list of choices
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []


    #method to add additional nodes to the story
    def add_child(self, node):
        self.choices.append(node)


    #method for traversing the tree
    def traverse(self):
        story_node = self
        print(story_node.story_piece)

        #while loop that ensures node has choices in the list and has user chose the path
        while len(story_node.choices) > 0:
            choice = input('What do you do? Enter 1 or 2 to continue the story: ')
            
            #conditional that ensures they are chosing 1 or 2
            if choice not in ['1', '2']:
                print('Please chose 1 or 2 to continue the story: ')

            #condition that allows the user to progress through the story
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child


######
# VARIABLES FOR TREE
######


#Wilderness story_root that describes the start of the story
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1) Roar back!
2) Run to the left...
""")


#choice_a for the story_root
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 'Hooray!'
""")


#choice_b for story_root
choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1) Gasp 'A talking bear!'
2) Explain that the bear scared you.
""")


#adding choice_a and choice_b to story_root
story_root.add_child(choice_a)

story_root.add_child(choice_b)


#choice_a_1 for choice_a
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. 
After making peace with a talking bear he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS!!!
""")


#choice_a_2 for choice_a
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.

YOU REMAIN LOST IN THE WILDERNESS!!!
""")


#adding choice_a_1 and choice_a_2 to choice_a
choice_a.add_child(choice_a_1)

choice_a.add_child(choice_a_2)


#choice_b_1 for choice_b
choice_b_1 = TreeNode("""
The bear is unamused.
After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST IN THE WILDERNSS!!!
""")


#choice_b_2 for choice_b
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you.
Your new friend shows you a path leafing out of the forest.

YOU HAVE ESCAPED THE WILDERNESS!!!
""")


#adding choice_b_1 and choice_b_2 to choice_b
choice_b.add_child(choice_b_1)

choice_b.add_child(choice_b_2)


######
# TESTING AREA
######

story_root.traverse()