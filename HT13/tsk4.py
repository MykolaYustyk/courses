'''
4. Створіть клас, який буде повністю копіювати поведінку list, за виключенням того, що індекси в ньому мають починатися з 1,
а індекс 0 має викидати помилку (такого ж типу, яку кидає list якщо звернутися до неіснуючого індексу)
'''

class MyList:
    
    def __init__(self, *args):
        self.items = list(args)        
        
    def __len__(self):
        return len(self.items)        
    
    def __getitem__(self, item):
        if 0 < item < len(self.items): 
            return self.items[item-1]
        elif -len(self.items) < item < 0:
            return self.items[item]
        else:
            raise IndexError('Індекс за межами списку')        
    
    def __repr__(self):
        return str(self.items)    
    
    def __setitem__(self, item, value):
        if 0 < item < len(self.items): 
            self.items[item-1] = value
        elif -len(self.items) < item < 0:
            self.items[item] = value
        else:
            raise IndexError('Індекс за межами списку')        
        
    def __delitem__(self, item):
        if 0 < item < len(self.items):            
            del(self.items[item-1])
        elif -len(self.items) < item < 0:
            del(self.items[item])
        else:
            raise IndexError('Індекс за межами списку')        
        
    def append(self, item):
        return self.items.append(item)    
    
    def extend(self, *items):
        return self.items.extend(items)    
    
    def pop(self, item=None):
        if item is None:
            item = 0
        else:
            item -= 1
        return self.items.pop(item)
    
    def clear(self):
        return self.items.clear()
    
    def count(self, value):
        return self.items.count(value)    
    
    def index(self, value):
        return self.items.index(value) + 1    
    
    def insert(self, item, value):
        return self.items.insert(item - 1, value)    
    
    def remove(self, value):
        return self.items.remove(value)
    
    def reverse(self):
        return self.items.reverse()    
    
    def sort(self, reverse=None):
        if reverse is None:
            reverse = False
        else:
            reverse = True               
        self.items = list(map(str, self.items))
        return self.items.sort(reverse=reverse)     
    
    def __add__(self, other):
        return self.items + other.items     
  
if __name__ == "__main__":   
    list1 = MyList(100, 200, 300, 400, 5, 'abracadabra')
    list2 = MyList(1, 3, 5, 7)
    print(list1)
    print(list1[1])
    list1[2] = 14
    print(list1)
    list1.append(100)
    print(list1)
    list1.extend([12, 14, 16], 12)
    print(list1)
    print(list1[-3])
    del list1[-2]
    print(list1)
    del list1[2]
    print(list1)
    print(len(list1))
    print(list1.index(100))
    list1.remove(100)
    print(list1)
    list1.reverse()
    print(list1)
    list1.sort(reverse=1)
    print(list1)
    print(list1 + list2)
