data1 = []
num = 0
ok = []

def is_ok(report):
    nope = False
    num = 0
    diff_list = []
    for index in range(len(report)):
        if index+1 < len(report):
            diff =report[index+1]-report[index]
            if diff > 3 or diff < -3 or diff == 0:
                nope = True
                diff = []
                break
                
            else:
                diff_list.append(diff)
                if len(diff_list) >1:
                    print(diff_list[1])
                    if diff_list[index] > diff_list[index+1] and index+1 <= len(diff_list):
                        ok.append(1)
                    if diff_list[index] < diff_list[index+1]and index+1 <= len(diff_list):
                        ok.append(2)


        else:
            #print(diff)
            #num += 1
            pass

    if nope== False:
        if len(set(ok)) == 1:
            num += 1
    else:
        pass
    return num  

with open('input_2024_2.txt', 'r') as file:
    data = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    for report in data:
        num2 = is_ok(report)
        num += num2



print(num)






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