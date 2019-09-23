from book_list import book_instances
from sorting_rules import SortingAlgorithm


'''
This function appends book ids to a list.
The list is used to compare the numbers with expected result.

'''

def book_ids(book_instances):
        ids_list = []
        for book in book_instances:
            ids_list.append(book['id'])
        return ids_list

   
'''
The following functions sort and compare book ids, 
putting them in the right order.

'''

def test_title_ascending(correct_result):
    rules = [['title',1]]
    books_sorter = SortingAlgorithm()
    books_test = books_sorter.sort(book_instances,rules)
    my_result = []
    
    my_result = book_ids(books_test)
    
    if my_result == correct_result:
        return True

    else:
        return False


def test_author_ascending_title_descending(correct_result):
    rules = [['title',0],['author',1]]
    books_sorter = SortingAlgorithm()
    books_test = books_sorter.sort(book_instances,rules)
    my_result = []
    
    my_result = book_ids(books_test)
    
    if my_result == correct_result:
        return True

    else:
        return False
    

def test_edition_descending_author_descending_title_ascending(correct_result):
    rules = [['author',0],['title',1],['edition_year',0]]
    books_sorter = SortingAlgorithm()
    books_test = books_sorter.sort(book_instances, rules)
    my_result = []
    
    my_result = book_ids(books_test)
    
    if my_result == correct_result:
        return True

    else:
        return False
    

def test_empty_set(correct_result):
    rules = []
    books_sorter = SortingAlgorithm()
    books_test = books_sorter.sort(book_instances, rules)
    my_result = []
    
    my_result = book_ids(books_test)
    
    correct_result = []
    
    if my_result == correct_result:
        return True

    else: 
        return False
        