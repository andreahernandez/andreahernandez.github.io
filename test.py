
# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and see a person inside a car") # Update to match your story.
print("Type 'yes' to go inside the car or 'no' to walk past the car")
user_input = input()
if user_input == "yes":
    print("You decided to go inside the car and you end up getting kidnapped ")    
if user_input == "no":
    print("You decided to not go inside the car and you survived")

elif user_input == "right":
    print("You choose to go right and you see a candy store") # Update to match your story.
print("Type 'yes' to go inside the candy store or 'no' to not go in")
user_input = input()
if user_input == "yes":
    print("You decided to go inside the candy store and you ate all the candy and you had a huge stomach ache")
if user_input == "no":
    print("You decided to no go inside the candy store and you survived")
    # Continue code to finish story.
