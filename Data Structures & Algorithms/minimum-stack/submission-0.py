class MinStack:

    def __init__(self):
        self.items=[]
        self.min=[]

    def push(self, val: int) -> None:    
        self.items.append(val)
        if(self.min):
            if(val<self.min[-1]):
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.min.pop()

    def top(self) -> int:
        if(self.items):
            return self.items[-1]
        else:
            return []

    def getMin(self) -> int:
        return self.min[-1]
        
