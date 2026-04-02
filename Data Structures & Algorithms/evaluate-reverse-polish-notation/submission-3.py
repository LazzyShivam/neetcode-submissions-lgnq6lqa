class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(b,a,o):
            if o == "+":
                return a+b
            elif o == "*":
                return a*b
            elif o == "-":
                return a-b
            elif o == "/":
                return a/b
        st = []
        hs = {"*","-","/","+"}
        for i in tokens:
            if i in hs:
                st.append(calculate(int(st.pop()),int(st.pop()),i))
                continue
            st.append(i)
        return int(st[-1])    

         
                                 
        