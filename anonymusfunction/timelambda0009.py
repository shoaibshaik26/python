"""
8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""

import os
import datetime

now = datetime.datetime.now()
print(now)
value1 = lambda now : now.year
values=value1(now)
print(values)