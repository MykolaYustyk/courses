'''
3. Створіть клас в якому буде атрибут який буде рахувати кількість створених екземплярів класів.
'''

class ClassInstancesCounter():
    count = 0
   
    def __init__(self):
        self.__class__.count = self.add_count()
    
    
    @classmethod
    def add_count(cls):
        cls.count += 1
        return cls.count
    

if __name__ == "__main__":
    instance_1 = ClassInstancesCounter()
    print(instance_1.count)
    instance_2 = ClassInstancesCounter()
    print(instance_1.count)
    print(instance_2.count)
    instance_3 = ClassInstancesCounter()
    print(instance_1.count)
    print(instance_2.count)       
    print(instance_3.count)    
    