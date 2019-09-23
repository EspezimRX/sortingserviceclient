import os.path, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '/src')

from book_list import book_instances
from tests import test_title_ascending, test_author_ascending_title_descending, test_edition_descending_author_descending_title_ascending, test_empty_set 


'''
Interactive part of the code. Shows user options
to sort the books.
 
'''
print('Books added:')
for i in range(len(book_instances)):
    print(book_instances[i])

print(
    '\n'
    '\n'
    'Scenarios:\n'
    'Type 1 to: title ascending\n'
    'Type 2 to: author ascending/title descending\n'
    'Type 3 to: edition descending/author descending/title ascending'
    '\n'
    '\n'
    )

rule = input('Type HERE: ')



correct_result1 = [3, 4, 1, 2]
correct_result2 = [1, 4, 3, 2]
correct_result3 = [4, 1, 3, 2]
empty_set = []



'''
Conditionals that return a result, according to the user input.

'''

if rule == '1' and test_title_ascending(correct_result1) == True:
    print('Books: ', correct_result1)

elif rule == '2' and test_author_ascending_title_descending(correct_result2) == True:
    print('Books: ', correct_result2)

elif rule == '3' and test_edition_descending_author_descending_title_ascending(correct_result3) == True:
    print('Books: ', correct_result3)

elif rule == '' and test_empty_set(empty_set) == True:
    print(empty_set)

else:
    print(Exception)





   





