'''
You have to organize meetings today. There are  meetings for today. Meeting  must start at time  and end at time . Unfortunately, there are only two meeting rooms available today. Consider meetings  and  intersecting in time if .

You cannot conduct two meetings in the same room at the same time.

Your task is to determine whether it is possible to hold all meetings using only two rooms. If yes, then print . Otherwise, print .

Function description

Complete the isPossible function in the editor. It contains the following parameters:

Parameter name: 
Type: INTEGER
Description: Number of meetings
Parameter name: 
Type: INTEGER ARRAY
Description: Start time of meetings
Parameter name: 
Type: INTEGER ARRAY
Description: End time of meetings
Return
The function must return an INTEGER denoting the answer to the problem. 
If it is possible to hold all the meetings using only two rooms, then it is . Otherwise, it is .
Input format 

The first line contains an integer  denoting the number of elements in .
Each line  of  subsequent lines (where ) contains an integer describing .
Each line  of  subsequent lines (where ) contains an integer describing .
Constraints


SAMPLE INPUT 
3
1
2
4
2
3
5

SAMPLE OUTPUT 
1
Explanation
Hold the first ([1; 2]) and the third ([4; 5]) meetings in the first room.

Hold the second meeting ([2; 3]) in the second room.
'''


def isPossible(n,s,e):
    # Write your code here
    for i in range(n):
        if max(s)>=min(e):
            return 1
        else:
            return 0    

    return # Write your code here

n = int(input())
start = []
end = []
for _ in range(n):
    start.append(int(input()))
for i in range(n):
    end.append(int(input()))

out_ = isPossible(n, start, end)
print(out_)