## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(l))
print(type(s))
print(type(d))



## 3. Defining a Class ##

class NewList():
    pass

## 4. Instantiating a Class ##

class NewList(DQ):
    pass

newlist_1 = NewList()

print(type(newlist_1))





## 5. Creating Methods ##

class NewList(DQ):
    
    def first_methode():
        return "This is my first method"
    
newlist = NewList()


    
    

## 6. Understanding 'self' ##

class NewList(DQ):
    def first_method(self):
        return "This is my first method"
 
newlist = NewList()

result = newlist.first_method()


    

## 7. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    
    def return_list(self,input_list):
        return input_list
    
newlist = NewList()

result = newlist.return_list([1,2,3])



## 8. Attributes and the Init Method ##

class NewList(DQ):
    def __init__(self,initial_state):
        self.data = initial_state
        
my_list = NewList([1,2,3,4,5])  

print(my_list.data)




## 9. Creating an Append Method ##

# The NewList definition from the previous
# screen is copied here for your convenience

class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        
    def append(self,arg):
        self.data.append(arg)
        
my_list = NewList([1,2,3,4,5])    

my_list.append(6)

print(my_list.data)





## 10. Creating and Updating an Attribute ##

# The NewList definition from the previous
# screen is copied here for your convenience

class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()
        
    def calc_length(self):
        """
        Calculate the length the list stored in the attribute data
        """
        length_item=0
        for item in self.data:
            length_item+=1
        self.length = length_item
        
fibonacci = NewList([1,1,2,3,5])
fibonacci.append(8)

print(fibonacci.length)

