import os
import subprocess
import time

mylist = []

with open ('covid_output.txt', 'r') as myfile:
    for x in myfile:
        if 'DEATHS:' in x:
            mylist.append(x)


num_us_deaths = mylist[0].replace(' ', '').replace('DEATHS:', '')

print(num_us_deaths)






