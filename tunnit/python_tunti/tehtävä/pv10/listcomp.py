from pathlib import Path

# with open('./input_2015_2.txt', 'r') as file:
#     content = (tuple(map(int,line.rstrip().split('x'))) for line in file.readlines if line)

# lista = []
# for i in range(10):
#     for j in range(10):
#         lista.append((i,j))

# LIST COMPREHENSION
# lista = [(i,j) for i in range(10) for j in range(10)]
# print(lista)

# SET COMPREHENSION
# set = {(i,j) for i in range(10) for j in range(10)}
# print(set)

# DICT COMPREHENSION
# dict = {i: i**2 for i in range(10) }
# print(dict)

# GENERATOR
# lista = ((i,j) for i in range(10) for j in range(10))
# print(dict(lista))


size = sum(item.stat().st_size for item in Path(r'C:/Windows').glob('*') if item.is_file())
print(f'{size/1024/1024:.2f} MiB')


