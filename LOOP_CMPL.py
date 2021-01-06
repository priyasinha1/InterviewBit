#Input Format
#Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
#Output Format
#Return an Integer, i.e minimum number of steps.
#Example Input
#Input 1:

# A = [0, 1, 1]
# B = [0, 1, 2]


#Example Output
#Output 1: 2



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        pre_x, pre_y, total = A[0], B[0], 0
        for cur_x, cur_y in zip(A, B):
            dx, dy = abs(cur_x - pre_x), abs(cur_y - pre_y)
            if dx < dy:
                total += dy
            else:
                total += dx
            pre_x, pre_y = cur_x, cur_y
        return total
