class Warehouse:
    purpose = 'Storage'
    region = 'West'


w1 = Warehouse()
print(w1.purpose, w1.region)


w2 = Warehouse()
w2.region = 'East'
print(w2.purpose, w2.region)
