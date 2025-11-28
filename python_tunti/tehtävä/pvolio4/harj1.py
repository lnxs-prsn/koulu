# def recursive(alist: list, num: int):
#     new_list = []
#     if num == 0:
#         return alist
#     else:
#         for element in alist:
            
#             if element == 0:
#                 new_list.append(element +1)
#             elif len(str(element)) % 2 == 0:
#                 index = int(len(str(element))/2)
#                 txt = str(element)
#                 sto1 = txt[:index]
#                 sto2 = txt[index:]
#                 new_list.append(int(sto1))    
#                 new_list.append(int(sto2))
#             else:
#                 new_list.append(element*2024)    
#         print(new_list)
#         return recursive(new_list, num-1)


# txt = '5688 62084 2 3248809 179 79 0 172169'
# alist1 = [int(element) for element in txt.split()]
# alist = [125, 17]
# num = 2

# print(recursive(alist, num))


# import math
# def recursive(alist: list, num: int):
#     new_list = []
#     if num == 0:
#         return alist
#     else:
#         for element in alist:
#             if element == 0:
#                 new_list.append(element +1)
#             elif (int(math.log10(element)) + 1) % 2 == 0:

#                 digits = int(math.log10(element)) + 1
#                 half = digits // 2
#                 left = element // (10 ** half)
#                 right = element % (10 ** half)
#                 new_list.append(left)
#                 new_list.append(right)

#             else:
#                 new_list.append(element*2024)    
#         return recursive(new_list, num-1)


# txt = '5688 62084 2 3248809 179 79 0 172169'
# alist1 = [int(element) for element in txt.split()]
# alist = [125, 17]
# num = 75

# print(recursive(alist, num))
from functools import cache

@cache
def blink(stone: str, count: int) -> int:
    if count == 0:
        return 1
    if stone == '0':
        return blink('1', count-1) 
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        part1 = str(int(stone[:middle]))
        part2 = str(int(stone[middle:]))
        return blink(part1, count-1) + blink(part2, count-1)
    else:
        return blink(str(int(stone) * 2024), count-1)

stones = '5688 62084 2 3248809 179 79 0 172169'
print(sum(blink(stone, 25) for stone in stones.split()))
print(sum(blink(stone, 900) for stone in stones.split()))
