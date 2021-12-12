input = open('test', 'r')
input = input.readlines()
input = [x.replace('\n','') for x in input]

points = 0

for line in input:
    contain = True
    while contain == True:
        contain = False
        if (line.__contains__("()") or
            line.__contains__("[]") or
            line.__contains__("{}") or
            line.__contains__("<>")):
                contain = True
                line = line.replace("()", "")
                line = line.replace("[]", "")
                line = line.replace("{}", "")
                line = line.replace("<>", "")
    if (line.__contains__("(") or
        line.__contains__("[") or
        line.__contains__("{") or
        line.__contains__("<")):
            line = line.replace("(", "")
            line = line.replace("[", "")
            line = line.replace("{", "")
            line = line.replace("<", "")
    if not line:
        pass
    else:
        if(line[0].__contains__(")")):
            points += 3
        if(line[0].__contains__("]")):
            points += 57
        if(line[0].__contains__("}")):
            points += 1197
        if(line[0].__contains__(">")):
            points += 25137
print(points)




