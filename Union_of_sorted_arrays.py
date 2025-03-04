# CODE LINK : https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        return sorted(set(a) | set(b))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends
