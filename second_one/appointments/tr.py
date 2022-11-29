import datetime

# dict = {'_state': <django.db.models.base.ModelState object at 0x0000011E1162C220>, 'id': 1, 'minutes_per_appointment': 25, 'start_date': datetime.date(2022, 11, 7), 'monday_start': datetime.time(7, 0), 'monday_end': datetime.time(22, 0), 'tuesday_start': datetime.time(7, 0), 'tuesday_end': datetime.time(22, 0), 'wednesday_start': None, 'wednesday_end': None, 'thursday_start': datetime.time(7, 0), 'thursday_end': datetime.time(22, 0), 'friday_start': datetime.time(7, 0), 'friday_end': datetime.time(22, 0), 'saturday_start': None, 'saturday_end': None, 'sunday_start': datetime.time(7, 0), 'sunday_end': datetime.time(22, 0)}

# dict = Week.objects.last().__dict__
""" 
dict = {
    'minutes_per_appointment': 30, 
    'id': 2, 
    'start_date': datetime.date(2022, 11, 14), 
    'monday_start': datetime.time(7, 0), 
    'monday_end': datetime.time(20, 0), 
    'tuesday_start': datetime.time(9, 0), 
    'tuesday_end': datetime.time(22, 0), 
    'wednesday_start': datetime.time(7, 0), 
    'wednesday_end': datetime.time(22, 0), 
    'thursday_start': datetime.time(7, 0), 
    'thursday_end': datetime.time(22, 0), 
    'friday_start': None,
    'friday_end': None, 
    'saturday_start': datetime.time(7, 0), 
    'saturday_end': datetime.time(22, 0), 
    'sunday_start': datetime.time(7, 0), 
    'sunday_end': datetime.time(17, 0),
    }

    
minutes_per_appointment = dict['minutes_per_appointment']
start_date = dict['start_date']
monday = [dict['monday_start'], dict['monday_end'], 0]
tuesday = [dict['tuesday_start'], dict['tuesday_end'], 1]
wednesday = [dict['wednesday_start'], dict['wednesday_end'], 2]
thursday = [dict['thursday_start'], dict['thursday_end'], 3]
friday = [dict['friday_start'], dict['friday_end'], 4]
saturday = [dict['saturday_start'], dict['saturday_end'], 5]
sunday = [dict['sunday_start'], dict['sunday_end'], 6]

gap_duration = datetime.timedelta(minutes=minutes_per_appointment)


week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
# for day in week:
#     print(day)
    
    
class SemiGap:
    def __init__(self, beginning, end, index, state=False):
        self.beginning = beginning
        self.end = end
        self.index = index
        self.state = state
    
    def __str__(self):
        return str(self.beginning)

gaps_of_week = []

for day in week:
    gaps_of_day = []
    try:
        beginning = datetime.datetime(start_date.year, start_date.month, start_date.day, day[0].hour, day[0].minute) + datetime.timedelta(days=day[2])
        end = beginning + gap_duration
        n_of_gaps = 15
    except:
        gaps_of_week.append(gaps_of_day)
        continue
    for i in range(n_of_gaps): 
        end = beginning + gap_duration
        semigap = SemiGap(beginning, end, i)
        gaps_of_day.append(semigap)               
        beginning = end
    gaps_of_week.append(gaps_of_day)
    
for day in gaps_of_week:
    for gap in day:
        print(gap)
    print('='*15)

def timedelta_to_int(a):
    pieces = str(a).split(":")
    return int(pieces[0])*60 + int(pieces[1])
num_gaps = timedelta_to_int(end-start) // timedelta_to_int(g_t)
 """

# a = datetime.time(7)
# b = datetime.time(22)
# c = datetime.timedelta(minutes=30)
# d = datetime.datetime(2022, 11, 11, 7)
# e = datetime.datetime(2022, 11, 11, 10, 10)

# result = e-d
# print(type(result.seconds))

# datetime-timedelta
# datetime+timedelta


# datetime (+)
# timedelta (+-)


# dict = {
#     'csrfmiddlewaretoken': ['fbKxOjuLoGRf2LAJCxZuA3VxsAS0JqZn5L3VSkIWaVRv3CRiXp1DaSuwgnUTOSLE'],
#     'indexes': ['0:0', '0:1', '2:0', '2:1', '3:0', '3:1', '4:0', '4:1']
#  }

# print(dict['indexes'])
# if '3:1' in dict['indexes']:
#     print('whatdafak')
# print(type(dict['indexes']))
