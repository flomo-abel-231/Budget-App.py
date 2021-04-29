
class Budget :
    

    def __init__ (self,category,amount):
        self.category = category
        self.amount = amount 
        pass 

               
      #methods
    def deposit(self):
        import datetime
        today = datetime.datetime.now()
        print("Welcome to the deposit method")
        food = 50000
        clothing = 250000
        car_expenses = 756000
        print(today)
        print (" Total deposit is",food + clothing + car_expenses )

        pass

    def check_balance(self):
        import datetime
        today = datetime.datetime.now()
        print ( 'Welcome to the the check balance entry' )
        print(today)
        pass

    def withdrawal (self):
        import datetime
        today = datetime.datetime.now()
        print(today)
        print ('Welcome to the withdrawal section')
        pass

    def transfer (self):
        import datetime
        today = datetime.datetime.now()
        print(today)
        print ('Welcome to the transfer section')
        pass
        




        
budget1 = Budget("food", 50000)

budget2 = Budget ("clothing", 250000)

budget3 = Budget("car_expenses", 756000)
    
print(budget1.deposit())    





