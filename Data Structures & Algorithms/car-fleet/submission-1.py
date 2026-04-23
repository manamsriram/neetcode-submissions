class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[(p,s) for p,s in zip(position,speed)]
        car.sort(reverse=True)
        fleet=1
        time=(target-car[0][0])/car[0][1]
        for i in range(1,len(car)):
            if ((target-car[i][0])/car[i][1])>time:
                fleet+=1
                time=(target-car[i][0])/car[i][1]
        return fleet