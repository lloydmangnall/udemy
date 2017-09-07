# shoppingList = ["milk","pasta","eggs","spam","bread","rice"]
# for item in shoppingList:
#     if item == 'spam': # check for the string 'spam'
#         # continue # jump to next for loop item
#         break # break out of the for loop altogether
#     print("Buy " + item)

meal = ["egg", "bacon", "tomato", "sausages", "rice"]
nastyFoodItem = ''

for item in meal:
    if item == 'spam': # if 'spam' not in list,
        nastyFoodItem = item
        break
else: # if 'spam' not in list, then this executes
    print("I'll have a plate of that please")

if nastyFoodItem:
    print("Can't I have anything without spam in it?")
