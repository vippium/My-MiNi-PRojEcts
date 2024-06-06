
'''
Author: Vipin Prajapat 
Date:  05 October, 2022
Purpose: Practice Problem

'''

print('\t\t<-- WELCOME TO XYZ KIRANA STORE -->\t\t')
sum = 0
user_bill_list = []
while True:

    user_input = input('Enter your Product price or \'q\' to quit.\n')

    if user_input != 'q':
        sum = sum + int(user_input)
        user_bill_list.append(user_input)

        print(f'\nYour Current Bill is {sum}.')

    else:
        break

    print("")
    print(f"Total Things you bought are: ", len(user_bill_list))
    
    for i in range(len(user_bill_list)):
        print(f"{i+1}: {user_bill_list[i]}")

print(f"\nYour Final Billing Amount is {sum}.")
print('Thank You!!.Come Soon Again!.\n')
