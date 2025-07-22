from Chef import Chef
from Chinese_Chef import Chinese_Chef

myChef = Chef()
myChef.make_special_dish()

myChinese_Chef = Chinese_Chef()
myChinese_Chef.make_chicken()
myChinese_Chef.make_special_dish()   # Overridden: orange chicken
myChinese_Chef.make_fried_rice()   


