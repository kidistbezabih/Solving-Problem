class Robot:

    def __init__(self, width: int, height: int):
        self.matrix = [[0 for i in range(width)]for j in range(height)]
        self.n = height
        self.m = width
        self.x = 0
        self.y = 0
        self.direction = "East"
        
    def step(self, num: int) -> None:
        if num >=(((self.n + self.m)*2)-4) and self.x == 0 and self.y == 0:
            self.direction = "South"
        num = num%(((self.n + self.m)*2)-4)

        for  _ in range(num):
            if self.x == 0:
                if self.y+1 < self.m:
                    self.y+=1
                    self.direction = "East"
                else:
                    self.x+=1
                    self.direction = "North"
            elif self.y == self.m-1:
                if self.x+1 < self.n:
                    self.x+=1
                else:
                    self.y -= 1
                    self.direction = "West"
            elif self.x == self.n-1:
                if self.y-1 > -1:
                    self.y-=1
                else:
                    self.x -= 1
                    self.direction = "South"

            else:
                if self.y == 0:
                    self.x-=1

    def getPos(self) -> List[int]:
        return [self.y,self.x]

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()