input = open('input/day2.txt')
file = input.readlines()

aim = 0
depth = 0
horizontal = 0

for line in file:
    str, value = line.split()
    value = int(value)
    if str == 'forward':
        horizontal += value
        depth += value * aim
    if str == 'up':
        aim -= value
    if str == 'down':
        aim += value

answer = horizontal * depth
print (answer)
