class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        n,m=len(matrix),len(matrix[0])
        l,h=0,(n*m)-1
        if not matrix or not matrix[0]:
            return False
        while(l<=h):
            mid=l+(h-l)//2
            mid_row, mid_col = divmod(mid, m)
            val=matrix[mid_row][mid_col]
            if val==target:
                return True
            elif val<=target:
                l=mid+1
            else:
                h=mid-1
        return False