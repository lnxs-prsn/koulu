data1 = []
num = 0
pos1 = 0
neg1 = 0
passed = 0
def is_ok(report):
    nope = False
    pos = 0
    neg = 0 
    diff_list = []
    ok = 0
    for index in range(len(report)):
        if index+1 < len(report):
            diff =report[index+1]-report[index]

            if diff > 3 or diff < -3 or diff == 0:
                nope = True
                diff_list = []
                ok = 0
                
                break
                
            else:
                diff_list.append(diff)
                if len(diff_list) == len(report)-1:
                    for index1 in range(len(diff_list)):
                        if diff_list[index1] < 0:
                            neg += 1 
                        elif diff_list[index1] < 0:
                            pos += 1 
                        elif diff_list[index1] == 0:
                            print('whyyyyyyy')
                    if pos > 0:
                        pos = 1
                    elif neg > 0:
                        neg = 1
                    else:
                        print('nut working')


        else:
            pass
    if nope == False:
        print(neg, pos)
        ok += 1
    return pos, neg, ok

with open('input_2024_2.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    for report in data:
        pos, neg, ok = is_ok(report)
        pos1 += pos
        neg1 += neg
        passed += ok


        



print(pos1, neg1, passed)






# Teron solution
#     reports = [
#         [
#             int(x) for x in line.split()
#         ] for line in file
#     ]

# for report in reports:
#     deltas = [
#         n - c
#         for c, n in zip(reports, reports[1:])
#     ]
#     if 0 in deltas:
#         print("bad!!!!!!11")