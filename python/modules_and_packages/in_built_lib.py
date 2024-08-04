import random

# print(dir(random))

# print(random.random())

# print(random.randint(1,100))

# print(random.randrange(1,11,2))

# print(random.choice([1,2,3,4,5]))

# items = ['a','b','c','d','e']

# random.shuffle(items)
# print(items)

import math 

# print(dir(math))

# print(math.factorial(5))

# print(math.pi)

# print(math.sqrt(64))

from datetime import datetime, timedelta

# print(datetime.now())

current_time = datetime.now()
# print(current_time.date())
# print(current_time.weekday())
# print(current_time.day)

past_time = current_time - timedelta(days=1)
# print(past_time)
# print(past_time.date())
# print(past_time.weekday())
# print(past_time.day)

future_time = current_time + timedelta(days=2, hours=12)
# print(future_time)

# print(datetime.strftime(current_time,"%d/%m/%y, %H:%M:%S"))

print(datetime.strftime(current_time,"%d/%m/%y, %I:%M:%S %p"))
