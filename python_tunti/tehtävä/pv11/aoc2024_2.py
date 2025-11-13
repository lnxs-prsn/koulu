data1 = []
num = 0
pos1 = 0
neg1 = 0
passed = []
print(type(passed))
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
                # check if all values are negative or positive
                if max(diff) < 0:
                    pass



        else:
            print(diff_list)
    if nope == False and ( sum(diff_list)<0 or sum(diff_list)>0 ):
        print(diff_list)
        ok += 1
    return pos, neg, ok

with open('input_2024_2.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    for report in data:
        pos, neg, ok = is_ok(report)
        
        pos1 += pos
        neg1 += neg

        if type(ok)== int and ok == 1:
            passed.append(ok)
        else:
            pass #print(report)
        


print(len(passed))

        



# print(pos1, neg1, passed)






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