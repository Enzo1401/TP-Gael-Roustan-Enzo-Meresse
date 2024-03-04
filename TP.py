class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class StackNoeud:
    def __init__(self, item, next_noeud=None):
        self.item = item
        self.next_noeud = next_noeud
 
class MyStack:
    def __init__(self, max_taille):
        self.top = None
        self.taille = 0
        self.max_taille = max_taille

    def add_to_stack(self, item):
        if self.taille >= self.max_taille:
            raise MyOutOfSizeException("Impossible d'ajouter à une pile pleine")
        nv_noeud = StackNoeud(item, self.top)
        self.top = nv_noeud
        self.taille += 1

    def pop_from_stack(self):
        if self.taille == 0:
            raise MyEmptyStackException("Impossible de dépiler d'une pile vide")
        item = self.top.item
        self.top = self.top.next_noeud
        self.taille -= 1
        return item

    def is_full(self):
        return self.taille >= self.max_taille

    def is_empty(self):
        return self.taille == 0


if __name__ == '__main__':
    myStack = MyStack(3)

    myStack.add_to_stack('hello')
    myStack.add_to_stack('hello')
    print(myStack.is_full()) 
    myStack.add_to_stack('hello')
    print(myStack.is_full()) 
    
    try:
        myStack.add_to_stack('hello') 
    except MyOutOfSizeException as e:
        print(e)
    
    print(myStack.pop_from_stack()) 
    print(myStack.pop_from_stack()) 
    print(myStack.is_empty()) 
    print(myStack.pop_from_stack()) 
    print(myStack.is_empty())
    
    try:
        print(myStack.pop_from_stack()) 
    except MyEmptyStackException as e:
        print(e)