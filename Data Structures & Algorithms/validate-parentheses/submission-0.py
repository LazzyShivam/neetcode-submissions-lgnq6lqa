class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if st and (st[-1]+i == "[]" or st[-1]+i == "()" or st[-1]+i == "{}"):
                st.pop()
                continue
            st.append(i)
        return len(st) == 0        
        