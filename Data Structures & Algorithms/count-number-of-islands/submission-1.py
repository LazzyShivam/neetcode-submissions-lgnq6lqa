from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                print(i,j,n,m)
                if grid[i][j] == "1":
                    count+=1
                    st =[(i,j)]
                    while st:
                        p,q = st.pop()
                        if p < 0 or q < 0 or p >= n or q >= m or grid[p][q]=="0":
                            continue
                        grid[p][q] = "0"

                        st.append((p+1,q))
                        st.append((p-1,q))
                        st.append((p,q-1))
                        st.append((p,q+1))
        return count            




        