from util import PriorityQueue
import copy
class Agent:
    def __init__(self):
        self.Domain = {}
        self.Queue = PriorityQueue()
        
    def ArcConsistency(self,gameState):
        variables = gameState.getVariables()
        Queue = PriorityQueue()
        for var in variables:
            domain = []
            constraints = gameState.getConstraints(var)
            for i in range(1,gameState.gameSize+1):
                if i not in constraints:
                    domain.append(i)
            
            self.Domain[var] = domain
            Queue.push(var,len(domain))
        self.Queue = Queue

    def Assignment(self,gameState):
        self.ArcConsistency(gameState)
        if self.Queue.isEmpty():
            return gameState
        else:
            AssignVar = self.Queue.pop()
            if len(self.Domain[AssignVar]) == 0:
                return None
            else:
                for domain in self.Domain[AssignVar]:
                    state = copy.deepcopy(gameState)
                    state.getUpdate(AssignVar,domain)
                    returnState = self.Assignment(state)
                    if returnState != None:
                        return returnState
        return None

"""
0 3 0 0 0 6 9 0 4
0 1 0 5 8 0 0 0 0
6 0 8 0 0 3 1 0 0
0 8 0 0 0 0 0 2 0
4 0 2 1 0 9 8 0 3
0 9 0 0 0 0 0 4 0
0 0 7 9 0 0 6 0 5
0 0 0 0 7 5 0 1 0
8 0 3 6 0 0 0 9 0
"""
