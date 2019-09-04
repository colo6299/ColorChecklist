
# Apologies for the quality, proceed with caution.

# print('Hello_world')

checklist = []

def my_func(say_this):
    print(say_this)

# my_func('Hello world')

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    return checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + ') ' + list_item)
        index += 1

def toggle_complete(index):

    if '[:D] ' in checklist[index]:
        checklist[index].replace('[:D] ', '')
    else:
        checklist[index] = '[:D] ' + checklist[index] # Next time I'll use emojis in my variables

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input.lower()

def select(function_code):

    # Create item
    if function_code == "c":
        input_item = user_input("Input item: \n")
        create(input_item)

    # Read item
    elif function_code == "r":
        user_index = int(user_input('Index? \n'))
        if user_index not in range(len(checklist)):
            print(':(')
        else: 
            print(read(user_index))

    elif function_code == 'u':
        user_index = int(user_input('Index? \n'))
        if user_index not in range(len(checklist)):
            print(':(\n')
        else: 
            update(user_index, user_input('Item? \n'))

    elif function_code == 'd': 
        user_index = int(user_input('Index? \n'))
        if user_index not in range(len(checklist)):
            print(':(')
        else: 
            destroy(user_index)
    
    elif function_code == 'q':
        print("Have a nice day :) ")
        return False

    elif function_code == 'm':
        user_index = int(user_input('Index? \n'))
        if user_index not in range(len(checklist)):
            print(':(')
        else: 
            toggle_complete(user_index)

    # Print all items
    elif function_code == "p":
        list_all_items()

    # Catch all
    else:
        print("pls no")
    return True

def test():

    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    
    toggle_complete(0)
    print(read(0))
    toggle_complete(0)
    print(read(0))
    # Call your new function with the appropriate value
    select("c")
    # View the results
    list_all_items()
    # Call function with new value
    select("r")
    # View results

    list_all_items()

running = True
while running:
    selection = user_input(
        """

        Create new item ----- c
        Read item ----------- r
        Update item --------- u
        Destroy item -------- d

        Print list ---------- p
        Mark item complete -- m
        Quit program -------- q

        """)
    running = select(selection)
