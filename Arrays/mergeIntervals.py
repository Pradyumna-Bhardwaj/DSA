intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key = lambda i : i[0])
output = [intervals [0]]
for start, end in intervals [1: ]: #2 elements in each entry will be parsed into [start, end]
    lastEnd = output[-1] [1] #storing the 2nd element of last entry
    if start <= lastEnd:
        output[-1][1] = max(lastEnd, end)
    else:
        output.append([start, end])