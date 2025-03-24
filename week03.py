from traceback import print_tb


def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: #중복된 값이 들어오는 걸 확인함
            result.append(city)
    return result

cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# cities = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
# cities = set(cities)
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(duplicate_city(cities))