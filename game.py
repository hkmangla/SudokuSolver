class GameState:
    def __init__(self,gameSize,gameState):
        self.gameSize = gameSize
        self.gameState = gameState
    
    def getVertical(self,position):
        vertical = []
        x,y = position
        for i in range(self.gameSize):
            vertical.append(self.gameState[i][y])
        return vertical

    def getHorizontal(self,position):
        x,y = position
        return self.gameState[x]
    
    def getBlock(self,position):
        blockSize = self.gameSize // 3
        x,y = position
        x = x - x%blockSize
        y = y - y%blockSize
        block = []
        for i in range(x,x+blockSize):
            for j in range(y,y+blockSize):
                block.append(self.gameState[i][j])
        return block
    
    def getConstraints(self,position):
        return self.getHorizontal(position) + self.getVertical(position) + self.getBlock(position)
    
    def getValue(self,x,y):
        return self.gameState[x][y]

    def getVariables(self):
        var = []
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                if self.gameState[i][j] == 0:
                    var.append((i,j))
        return var
    def getUpdate(self,position,value):
        x,y = position
        self.gameState[x][y] = value

    def getGame(self):
        print "\n\nGetting GameState\n\n"
        for row in self.gameState:
            for col in row:
                print col,
            print
