class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[(p,s) for p,s in zip(position,speed)]
        car.sort(reverse=True)
        stack=deque()
        for i,j in car:
            stack.append((target-i)/j)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)