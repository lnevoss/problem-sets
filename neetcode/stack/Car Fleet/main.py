class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        fleets = [0]
        n = len(position)

        pairs = [(p, s) for p, s in zip(position,speed)]
        pairs.sort(reverse=True)

        for x in range(n):
            time = (target - pairs[x][0]) / pairs[x][1]
            if time not in fleets and fleets[-1] < time:
                fleets.append(time)
        
        return len(fleets)-1

sol = Solution()
target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
print(sol.carFleet(target,position,speed))
      