from datetime import date
from datetime import datetime
# d = date.today()
# print(d)
# print(datetime.combine(d, datetime.min.time()))
s = "2018-06-28"
print(datetime.strptime(s,'%Y-%m-%d'))

# today  = datetime.now()


# print(today)

# # print(datetime.strptime(s,'%Y-%m-%d'))