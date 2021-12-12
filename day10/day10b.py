input = open('input', 'r')
input = input.readlines()
input = [x.replace('\n','') for x in input]

points = 0
list = []

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
                if not (line.__contains__(")") or
                    line.__contains__("]") or
                    line.__contains__("}") or
                    line.__contains__(">")):
                        goodline = line
                        reversedline = goodline[:: -1]
                        points = 0
                        for x in (reversedline):
                            if '(' in x:
                                points = (points * 5 + 1)
                            if '[' in x:
                                points = (points * 5 + 2)
                            if '{' in x:
                                points = (points * 5 + 3)
                            if '<' in x:
                                points = (points * 5 + 4)
                        list.append(points)
                        sortedlist = sorted(list)
print(sortedlist[23])



