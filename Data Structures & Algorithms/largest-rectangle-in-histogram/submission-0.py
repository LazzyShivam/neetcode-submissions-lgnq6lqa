class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        L = [-1]*n
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            L[i] = st[-1] if st else -1    
            st.append(i)
        st = []
        R = [n]*n
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            R[i] = st[-1] if st else n    
            st.append(i) 
        max_area = 0
        for i in range(n):
            width = R[i] - L[i] - 1
            area = heights[i] * width
            if max_area < area:
                max_area = area
        return max_area               



