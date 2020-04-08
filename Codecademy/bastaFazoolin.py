#menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} is available from {start_time} to {end_time}.".format(self.name, self.start_time, self.end_time)

    #method for calculating a individual bill
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total


#brunch menu
brunch = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, '11am', '4pm')


#early bird menu
early_bird = Menu('Early-bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, '3pm', '6pm')


#dinner menu
dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, '5pm', '11pm')


#kids menu
kids = Menu('Kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, '11am', '9pm')


#class for franchises
class Franchise:
    #class constructor
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    #string representation of the object
    def __repr__(self):
        return 'This franchise is located at {address}.'.format(address = self.address)

    
    #method describing the available menus (need to determine how to input time to show available menus - import datetime as alias to shorten syntax and then us strptime or strftime to create range)
    def available_menus(self, time):
        list_avail_menus = []

        #import datetime as dt and put time in 24 hour clock
        from datetime import datetime as dt
        time_24time = dt.strptime(time, '%I%p')
        time_24hr = time_24time.hour
        
        #iterate through the list of the menus available at that franchise
        for item in self.menus:

            #put start time and end time in 24 hour clock and get the hour of the time
            st_24time = dt.strptime(item.start_time, '%I%p')
            end_24time = dt.strptime(item.end_time, '%I%p')
            st_24hr = st_24time.hour
            end_24hr = end_24time.hour

            #if statement that appends menu to the available menu list with the conditional that it falls within available time
            if st_24hr <= time_24hr <= end_24hr:
                list_avail_menus.append(item.name)

        return list_avail_menus
    



# flaship store: 1232 West End Road franchise
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

# new installment: 12 east mulberry street franchise
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])


#test on the available_menus method
print(flagship_store.available_menus('12pm'))

print(new_installment.available_menus('5pm'))



#class for business
class Business:

    #class constructor for instance variables of name and franchise
    def __init__(self, name, franchise):
        self.name = name
        self.franchise = franchise



#basta fazoolin' with my heart business object
basta_fazoolin = Business('''Basta Fazoolin' with my Heart''', [flagship_store, new_installment])



#take a' arepa menu object
arepas_menu = Menu('Arepas', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, '10am', '8pm')

#take a' arepa franchise object
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

#take a' arepa business object
take_a_arepa = Business("Take a' Arepa", [arepas_place])