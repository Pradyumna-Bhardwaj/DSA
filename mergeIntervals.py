# solution incompelete do not read


intervals = [[5,6],[4,4],[3,3],[2,2],[5,5]]

intervals.sort(key=lambda x: x[0])
print(intervals)
i=0
while(i<len(intervals)-2):
    if(len(intervals) > 2 and (intervals[i][1] >= intervals[i+1][0])):
        intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
        intervals.pop(i+1)
        print(intervals)
    else:
        i+=1

if(len(intervals)==4 and (intervals[2][1] >= intervals[3][0])):
    intervals[2][1] = max(intervals[2][1], intervals[3][1])
    intervals.pop(3)

if(len(intervals)==3 and (intervals[1][1] >= intervals[2][0])):
    intervals[1][1] = max(intervals[1][1], intervals[2][1])
    intervals.pop(2)

if(len(intervals)==2 and (intervals[0][1] >= intervals[1][0])):
    intervals[0][1] = max(intervals[0][1], intervals[1][1])
    intervals.pop(1)
print(intervals)