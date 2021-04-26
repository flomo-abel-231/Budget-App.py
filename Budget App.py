class Budget :
    def __init__ (self):
        pass
        
        
        
budget1 = Budget()
budget1.food = {
    'Rice':'1500usd',
    'Beans':'1000usd',
    'Fish':'2000usd',
    'Meat': '3000usd',
    'Greens': '4000usd'
    }

budget2 = Budget ()
budget2.clothing = {
    'Shirts':'4000usd',
    'Trousers': '2000usd',
    'Boxers': '2000usd',
    'Sneakers': '3000usd'
    }    

budget3 = Budget()
budget3.car_expenses = {
    'Engine oil': '2000usd',
    'Gasoline': '3000usd',
    'Shock absorber': '3000usd',
    'Tyres': '4000usd',
    'Car wash': '2000usd',
    'Other services': '5000usd' 
    }
    

print(budget1.food["Rice"])
print(budget2.clothing["Trousers"])
print(budget3.car_expenses["Other services"])





