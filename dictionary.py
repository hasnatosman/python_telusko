"""
Dictionary is an another data type that has key for any value.

"""

data = {
    'name': 'HASNAT',
    'id': 232323,
    'country': 'Bangladesh'
}
print(data)
print(data.get('id'))
print(data.get('country', 'Not mention'))
print(data.get('city', 'Not mention'))

names = ['Hasnat', 'Sajib', 'Ashik']
job = ['Python Developer', 'Android developer', 'React developer']

data = dict(zip(names, job))
print(data)

data['Kazi'] = 'Front End Developer'
print(data)
del data['Sajib']
print(data)