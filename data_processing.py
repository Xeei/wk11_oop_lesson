import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

x = filter(lambda x: float(x['latitude']) >= 60.0, cities)
for item in x:
    print(item)

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    """For agreate data"""
    data_list = [float(x[aggregation_key]) for x in dict_list]
    print(aggregation_function(data_list))


# Let's write code to
# - print the average temperature for all the cities in Italy
aggregate('temperature', lambda x: sum(x)/len(x), filter(lambda x: x['country'] == 'Italy', cities))

# - print the average temperature for all the cities in Sweden
aggregate('temperature', lambda x: sum(x)/len(x), filter(lambda x: x['country'] == 'Sweden', cities))

# - print the min temperature for all the cities in Italy
aggregate('temperature', lambda x: min(x), filter(lambda x: x['country'] == 'Italy', cities))

# - print the max temperature for all the cities in Sweden
aggregate('temperature', lambda x: max(x), filter(lambda x: x['country'] == 'Sweden', cities))

class CitiesDB:
    def __init__(self, cities=[]) -> None:
        self.cities = cities


    def filter(self, condition, key=None):
        if key is None:
            return  [x for x in self.cities if condition(x)]
        return [x[key] for x in self.cities if condition(x)]
    
    def aggregate(self, key, function, dict_list):
        data_list = [float(x[key]) for x in dict_list]
        return function(data_list)
        
class CountriesDB:
    def __init__(self, countries=[]) -> None:
        self.countries = countries

    def filter(self, condition, key=None):
        if key is None:
            return  [x for x in self.countries if condition(x)]
        return [x[key] for x in self.countries if condition(x)]

city = CitiesDB(cities)
country = CountriesDB(countries)

country_in_EU_no_coastlines = country.filter(lambda x: x['coastline'] == 'no' and x['EU'] == 'yes', 'country')
# print(country_in_EU_no_coastlines)
city_in_country = city.filter(lambda x: x['country'] in country_in_EU_no_coastlines, 'temperature')
print('Min:', min(city_in_country))
print('Max:', max(city_in_country))

list_lat = city.filter(lambda x: x, 'latitude')
list_lon = city.filter(lambda x: x, 'longitude')
print('Max lat:', max(list_lat))
print('Min lat:', min(list_lat))
print('Max lon:', max(list_lon))
print('Min lon:', min(list_lon))



# TODO wk11 assignment


class Table:
    def __init__(self, table_name="Table", table=[]) -> None:
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        """Filter data"""
        return [x for x in self.table if condition(x)]
    
    def aggregate(self, aggregation_function, aggregation_key):
        """For aggregate data"""
        data_list = [x[aggregation_key] for x in self.table]
        return aggregation_function(data_list)
    
    def __str__(self) -> str:
        msg = f'{self.table_name}\n'
        msg += f'Total row: {len(self.table)}'
        return msg

class TableDB:
    def __init__(self) -> None:
        self.__table_list = []

    def insert(self, table: Table) -> None:
        if not isinstance(table, Table):
            raise TypeError
        
        self.__table_list.append(table)

    def search(self, table_name: str) -> Table:
        pass
