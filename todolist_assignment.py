def menu():
    print("""
Menu:
    1- Press 1 for adding a single item in the list
    2- Press 2 for updating a single item in the list
    3- Press 3 for removing a single item from the list
    4- Press 4 to mark an item as complete
    5- Press 5 to mark an item as incomplete
    6- Press 6 to display current todo list
    7- Press 7 to Exit the program
    """)


def populate_list():
    total_items = int(input('Please enter how many items you want to list?\n'))
    print('Please enter the items')
    for i in range(0, total_items):
        items = input()
        list_items = {
            'item name': items,
            'status': 'incomplete'
        }
        todo_list.append(list_items)
    return todo_list


def add_single_item(itm, indx):
    todo_list.insert(indx, itm)
    return todo_list


def update_single_item(crrnt_indx, updtd_indx):
    todo_list[crrnt_indx] = updtd_indx
    return todo_list


def remove_single_item(rmv_item):
    todo_list.remove(rmv_item)
    return todo_list


# This function will delete the item from the todo list
# def mark_as_complete(c):
#    todo_list.remove(c)
#    return todo_list

# This function will add the item again in the todo list
def mark_as_incomplete(inc):
    todo_list.append(inc)
    return todo_list


todo_list = []
populate_list()
print(f'Your entered list is as follows: \n {todo_list}')

user_selected_option = 0

while user_selected_option != '7':
    menu()
    user_selected_option = input('Selection an option to continue \n> ')

    if user_selected_option == '1':
        item = input('Please enter an item to add to the list: ')
        index = int(
            input(f'\n Please enter the "index" where you want to add the item in this list \n {todo_list} \n> '))
        add_single_item(item, index)
        print(f'The updated todo list is as: {todo_list}')

    elif user_selected_option == '2':
        current_index = int(
            input(f'Please select the index of item you want to update from the list \n {todo_list} \n>'))
        updated_item = input('Please enter the new item: ')
        update_single_item(current_index, updated_item)
        print(f'The updated todo list is as: {todo_list}')

    elif user_selected_option == '3':
        item_to_be_removed = input(f'Enter the item to remove \n{todo_list} \n>')
        remove_single_item(item_to_be_removed)
        print(f'The updated todo list is as: {todo_list}')

    elif user_selected_option == '4':
        mark_item_as_complete = input(f'Which item you want to mark as complete? \n {todo_list} \n>')
        remove_single_item(mark_item_as_complete)
        print(f'"{mark_item_as_complete}" is marked as complete')
        print(f' The updated todo list is: \n {todo_list}')

    elif user_selected_option == '5':
        mark_item_as_incomplete = input(f'Which item you want to mark as incomplete? \n {todo_list} \n>')
        mark_as_incomplete(mark_item_as_incomplete)
        print(f'"{mark_item_as_incomplete}" is marked as incomplete')
        print(f'The updated todo list is: \n {todo_list}')

    elif user_selected_option == '6':
        print(f'The current todo list is as follows: \n {todo_list}')

    elif user_selected_option == '7':
        print('Thank you for using the program')
        break
    else:
        print('Incorrect option, please enter the right option from the menu ')
