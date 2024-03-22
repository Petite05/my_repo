


                          # MAP


menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "petite"]

def find_cofffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_cofffee, menu)
print(map_coffee)
for x in map_coffee:
print(x)



            # Filter

def find_cofffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = filter(find_cofffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

