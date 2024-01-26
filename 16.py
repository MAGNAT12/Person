class Person:
    
    def  init(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        
        
a = Person("Magnat", "15")
a.print_info()