""" import datetime

class Gap:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return str(self.start)
    
a = Gap(datetime.datetime(2022, 11, 18, 7, 30), datetime.datetime(2022, 11, 18, 7, 30))
b = Gap(datetime.datetime(2022, 11, 18, 9), datetime.datetime(2022, 11, 18, 9, 30))
c = Gap(datetime.datetime(2022, 11, 18, 7, 30), datetime.datetime(2022, 11, 18, 8, 30))
d = Gap(datetime.datetime(2022, 11, 18, 7), datetime.datetime(2022, 11, 18, 8, 30))
e = Gap(datetime.datetime(2022, 11, 18, 8, 30), datetime.datetime(2022, 11, 18, 8, 30))
f = Gap(datetime.datetime(2022, 11, 18, 10), datetime.datetime(2022, 11, 18, 10, 30))
g = Gap(datetime.datetime(2022, 11, 18, 6), datetime.datetime(2022, 11, 18, 9, 30))
h = Gap(datetime.datetime(2022, 11, 18, 9), datetime.datetime(2022, 11, 18, 9, 30))

day = [a, b, c, d, e, f, g, h]

def get_earliest_datetime(gaps):  # returns datetime.datetime
    # gaps is a list with all the gaps in a day. Every gap has a datetime like attribute called start
    l = [(gap.start.time().hour*60+gap.start.time().minute)/60 for gap in gaps]
    m = min(l)
    index = l.index(m)
    return day[index].start

# print(type(get_earliest_datetime(day)))
# print(get_earliest_datetime(day))    


def get_latest_datetime(gaps):  # returns datetime.datetime
    # gaps is a list with all the gaps in a day. Every gap has a datetime like attribute called start
    l = [(gap.end.time().hour*60+gap.end.time().minute)/60 for gap in gaps]
    m = max(l)
    index = l.index(m)
    return day[index].end

# print(type(get_latest_datetime(day)))
# print(get_latest_datetime(day))


for i in range(12):
    for j in range(3):
        if i == 10 and j == 2:
            value =(i, j)
            lueva = (j, i)
            print(value)
            break
            
print(value)
print(lueva) """

import time






def timer(function):
    def wrapper(*args, **kwargs):
        beginning = time.time()
        function(*args, **kwargs)
        end = time.time()
        print('Function took', end-beginning, 'seconds')
    return wrapper

@timer
def counter(n):
    counter = 0
    for i in range(n):
        counter += 1
        
counter(n=1000000000)