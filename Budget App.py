
class Category :
    

    def __init__ (self,category,amount):
        self.category = category
        self.amount = amount 
        pass 

               
      #methods
    def deposit(self):
        self.amount += self.amount
        return "You have successfully deposited: {} in {} category".format(self.amount,self.category)

    def check_balance ():
        #this should return a true or false, it checks if amount is less or greater than self.amount
        return False 

    def budget_balance(self):

        return "your current balance is: {}".format(self.amount)
    
    
    def withdrawal (self):
       # reverse of deposit
        self.amount - self.amount 
        return " you have successfully withdrew {} in {} category".format(self.amount, self.category)

    def transfer (self,amount,deposit):
        #transfer between two instantiated categories
        return self.withdrawal (amount) + " " + self.deposit(amount)
        

food_category = Category("Food", 1000)
clothing_category = Category("Clothing", 20)
car_expenses_category = Category("Car expenses", 75000)
appliances_category = Category("Appliances", 6000)

print(food_category.deposit())
print(food_category.withdrawal())
print(food_category.budget_balance())
#print(food_category.transfer(5000,appliances_category)) 
#print(food_category.check_balance( 30000000))
        
