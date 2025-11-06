import json
import csv
from pathlib import Path 
import asyncio
"""with open('json_test.json', 'r+') as f:
    data = json.load(f)
    data1 = json.dumps(data)
    data2 = json.loads(data1)
    print(data2)"""


"""with open('data.csv', 'a+') as f:
    ff = csv.reader(f)
    print(ff)
    for x in ff:
        print(x, end='')
    writer = csv.writer(ff)
    writer.writerow(['Nimi,Ikä,Kaupunki'])"""


"""with open('customers-1000.csv', 'r', encoding='utf-8') as f:
    file = csv.reader(f)
    for x in file:
        print(x)"""
"""
p = Path(r'C:\Users\sa056287\OneDrive - Taitotalo\course\python\python_tunti\tehtävä\päivä9')
#if p.is_file
for x in p.glob(r'*'):
    print(x.stat().st_mode)

print()
#print('stats',p.stat())
#print('directory of path',dir(p))
"""

a = asyncio()