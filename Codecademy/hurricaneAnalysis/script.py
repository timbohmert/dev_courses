#Project goals (supplied by Codecademy)

#You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

#Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occurred.

# names of hurricanes (supplied by Codecademy)
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes (supplied by Codecademy)
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes (supplied by Codecademy)
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes (supplied by Codecademy)
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane (supplied by Codecademy)
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes (supplied by Codecademy)
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane (supplied by Codecademy)
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]



##write your update damages function here##:
def str_to_float(arr):
    float_damages = []

    #for loop to iterate through list
    for x in arr:
        
        #takes str ending with 'M' and changes it to float * 1000000
        if x[-1] == 'M':
            new_damage = float(x[:-1]) * 1000000
            float_damages.append(new_damage)
        
        #takes str ending with 'B' and changes it to float * 1000000000
        elif x[-1] == 'B':
            new_damage = float(x[:-1]) * 1000000000
            float_damages.append(new_damage)
        
        #appends str that do not follow above conditions
        else:
            float_damages.append(x)

    return float_damages
            


##write your construct hurricane dictionary function here##:
def data_to_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_dict = {}
    for i in range(len(names)):
        hurricane_dict.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': str_to_float(damages)[i], 'Death': deaths[i]}})
    return hurricane_dict


new_dict = data_to_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)



##write your construct hurricane by year dictionary function here##:

def year_dict(dict):
    hurricane_years = {}
    
    #for loop that checks if year in hurricane_years, and adds data 
    for name, data in dict.items():
        for year, lst in hurricane_years.items():
            if data['Year'] == year:
                lst.append(data)

        hurricane_years.update({data['Year']: [data]})
    
    return hurricane_years



##write your count affected areas function here##:

def area_count(dict):
    affected_count = {}

    for name, data in dict.items():
        for area in data['Areas Affected']:
            if area not in affected_count:
                affected_count[area] = 1
            else:
                affected_count[area] += 1 

    return affected_count



##write your find most affected area function here##:

def max_count(dict):
    
    #uses area_count function to determine the count each area was affected and saves as areas
    areas = area_count(dict)

    #uses max(dict_name.items(), key=lambda x: x[1])
    return max(areas.items(), key=lambda x: x[1])



##write your greatest number of deaths function here##:

def greatest_deaths(dict):
    max_death = max(dict.items(), key=lambda x: x[1]['Death'])
    return {max_death[0]: max_death[1]['Death']}



###write your catgeorize by mortality function here##:

#mortality_scale provided by Codecademy
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000
    }

def mortality_rating(dict):
    rating_dict = {}

    #for loop that iterates through list of hurricanes and related data
    for name, data in dict.items():

        #for loop that iterates through list of items in mortality scale and associated death count
        for rating, deaths in mortality_scale.items():

            #condition statement that determines the rating for each hurricane based on data['Death'] and adds name and mortality rating to rating_dict
            if data['Death'] <= deaths:
                if rating not in rating_dict:
                    rating_dict.update({rating: [data]})
                else:
                    rating_dict[rating].append(data)

    return rating_dict



##write your greatest damage function here##:

def greatest_damage(dict):
    max_damage = 0
    max_damage_cane = ''

    #for loop that iterates through dict
    for name, data in dict.items():
        
        #try/except block that tests if data[damage] is greater than max_damage and updates max_damage and max_damage_cane if it is, if dat[damage] is str then block continues
        try:
            if data['Damage'] > max_damage:
                max_damage = data['Damage']
                max_damage_cane = name
        except:
            continue

    return {max_damage_cane: max_damage}



##write your catgeorize by damage function here##:

#damage_scale provided by Codecademy

damage_scale = {
    0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000,
}

def damage_rating(dict):
    rating_dict = {}

    #for loop that iterates through dict of hurricanes with temp variable for cane name and associated data
    for name, data in dict.items():

        #for loop that iterates through dict of damage_scale
        for rating, damage in damage_scale.items():
            
            #try/except block with condition to check if data['Damage'] is <= against damage from damage_scale, if it is, then that key is the damage rating, updates rating_dict with name and rating. If 'Damages not recorded', block throws error and updates rating_dict with name and 'Damages not recorded'
            try:
                if data['Damage'] <= damage:
                    if rating not in rating_dict:
                        rating_dict.update({rating: [data]})
                    else:
                        rating_dict[rating].append(data)
            except:
                if 'Damages not recorded' not in rating_dict:
                    rating_dict.update({'Damages not recorded': [data]})
                else:
                    rating_dict['Damages not recorded'].append(data)

    return rating_dict



