previouslist3 = []
previous = None
options = ['>','<', '', '^','v']
lines = '^v^v^v^v^v'
house_count = 0
# test assumptions first in small scale

for direction in lines:

    if abs(options.find(previous)-options.find(direction)) != 1:
        if len(previouslist3) == 8
        house_count += 1
        previous = direction
        previouslist3.append(options.find(direction))
        if len(previouslist3) == 4:
            previouslist3.pop(0)
            
    elif abs(options.find(previous)-options.find(direction)) == 1:
        previouslist3 = [options.find(direction)]
        previous = direction
        continue
