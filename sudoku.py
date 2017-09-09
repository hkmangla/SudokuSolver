from game import GameState
from Agent import Agent
print "Enter Size(N) of game N*N i.e. N: "
size = input()
print "Enter sudoku space separated elements and '0' for empty element: "
gameList = []
for i in range(size):
    l = [int(x) for x in raw_input().split(' ')]
    gameList.append(l)

gamestate = GameState(size,gameList)
agent = Agent()
solveState = agent.Assignment(gamestate)
solveState.getGame()
