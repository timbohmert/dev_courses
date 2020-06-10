# The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.

# In this project, we are going to implement a hash map to relate the names of flowers to their meanings. In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. We will implement the Linked List data structure for each of these separate chains.

#goal and objective provided by Codecademy.


#importing Node and LinkedList classes from linked_list dictionary
from linked_list import Node, LinkedList

#importing flower_definitions from blossom_lib
from blossom_lib import flower_definitions

#creating HashMap class with linked lists for handling collisions
class HashMap:

    #hash map constructor for declaring the array size and the empty array of length size
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]


    #hash function to take key and arrive at key value
    def hash(self, key):
        hash_code = sum(key.encode())
        return hash_code


    #compression function that mods hash_code with array_size into hash index
    def compress(self, hash_code):
        hash_index = hash_code % self.array_size
        return hash_index


    #setter method that assigns in key and value
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))

        #creating node for linked list
        payload = Node([key, value])

        #accesing the list at that array index
        list_at_array = self.array[array_index]

        #iterating through the list at the array to check if the key is present
        for x in list_at_array:
            
            #when the key is present, overwriting the value with the given value
            if x[0] == key:
                x[1] = value
                return

        #inserting payload at the end of the linked list at the array index
        list_at_array.insert(payload)    
        return


    #getter method that retrieves value with given key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))

        #getting the linked list at array_index in our array
        list_at_index = self.array[array_index]        

        #iterating through linked list at array_index
        for x in list_at_index:

            #if key at node is equal to input key, return the value
            if x[0] == key:
                return x[1]

        #if key did not match saved keys in the linked list, then return None
        else:
            return None



#instantiation of blossom HashMap with length of array equal to flower_definitions list
blossom = HashMap(len(flower_definitions))

#function for assigning list of keys and values to HashMap
def list_assignment(obj, lst):
    for x in lst:
        obj.assign(x[0], x[1])

list_assignment(blossom, flower_definitions)

daisy_value = blossom.retrieve('daisy')
print(blossom.retrieve('rose'))
print(blossom.retrieve('dandelion'))


print(daisy_value)
