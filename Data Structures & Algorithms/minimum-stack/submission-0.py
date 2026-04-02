class MinStack:

    def __init__(self):
        self.st = []
        self.ms = []

        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ms:
            self.ms.append(val)
        else:    
            self.ms.append(min(val,self.ms[-1]))
        

    def pop(self) -> None:
        self.st.pop()
        self.ms.pop()
        

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        return None    
        

    def getMin(self) -> int:
        if not self.ms:
            return None
        return self.ms[-1]
        
