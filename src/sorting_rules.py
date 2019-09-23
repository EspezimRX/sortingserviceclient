from operator import itemgetter

class SortingAlgorithm():
   
    def sort(self,books,rules):
        """
        This method sorts a list of books according to the rules described.
        The rules can be ascending or descending.

        """
        
        if not rules:
            return []
       
        else:
            for rule in rules:
                if rule[1] == 0:
                    descending = True
                else:
                    descending = False
                books = sorted(books, key=itemgetter(rule[0]), reverse=descending)

        return books




