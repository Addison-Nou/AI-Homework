# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        oldPos = currentGameState.getPacmanPosition()

        "*** YOUR CODE HERE ***"
        import math
        def getDistance(a, b):
            return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

        #print("Distance between {0} and {1}: {2}".format(oldPos, newPos, getDistance(oldPos, newPos)))

        score = successorGameState.getScore()
        #print("Score: ", score)
        #print(newFood.asList())
        #print("newFood: ", newFood.asList())
        #print("newPos: ", newPos)
        #print("newGhostStates: ", newGhostStates)
        #print("newScaredTimes: ", newScaredTimes)

        #Add to score if move closer to new food
        for food in newFood.asList():
            if (getDistance(oldPos, food) > getDistance(newPos, food)) and (getDistance(newPos, food) < 3):
                score+=1

        for i in newGhostStates:
            ghostPos = i.configuration.pos
            #print(i.configuration.pos)
            if (getDistance(oldPos, ghostPos) < getDistance(newPos, ghostPos)) and (getDistance(newPos, ghostPos) < 5):
                score+=2
        #newGhostStates.__str__()

        #print("newFood: {0}\nnewPos: {1}\nnewGhostStates: {2}\nnewScaredTimes: {3}".format(newFood, newPos, newGhostStates, newScaredTimes))

        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        #NOTES:

        #print("--------------------NEW CALL-----------------------")

        #print("Total depth (self.depth): ", self.depth)

        # def minimaxRecursive(aGameState, action, dept, current):
        #     #print("Current Depth: ", depth)
        #     if (dept <= self.depth):
        #         #print("Current depth: ", depth)

        #         #print(str(aGameState))
        #         # #If we're in a win state
        #         # if (aGameState.isWin()):
        #         #     #Stop the player
        #         #     #return Directions.STOP
        #         #     print("Win leaf found")
        #         #     score = self.evaluationFunction(aGameState)

        #         # elif (aGameState.isLose()):
        #         #     print("Lose leaf found")
        #         #     score = self.evaluationFunction(aGameState)

        #         for act in aGameState.getLegalActions(0):
        #             if act != Directions.STOP:
        #                 #print(str(aGameState))
        #                 #print("action: {0}".format(act))

        #                 if dept%2 == 0:
        #                     value = 999999999
        #                     childScore = minimaxRecursive(aGameState.generateSuccessor(0, act), action, dept+1, value)
        #                     if childScore[0] > current:
        #                         current = childScore[0]
        #                         if dept == 0:
        #                             action = act

        #                 else:
        #                     value = -999999999
        #                     childScore = minimaxRecursive(aGameState.generateSuccessor(0, act), action, dept+1, value)
        #                     if childScore[0] <= current:
        #                         current = childScore[0]
        #                         if dept == 0:
        #                             action = act

        #         #print("Current Score for action {0}: {1}".format(action, current))
        #         return (current, action)

        #     else:
        #         #print("Depth reached; score: ", self.evaluationFunction(aGameState))
        #         return (self.evaluationFunction(aGameState), action)

        # minimaxResult = minimaxRecursive(gameState, None, 0, -999999999)
        # #print("FINAL ACTION: ", minimaxResult[1])
        # #print(self.depth) #This gets passed in to be what depth we search to
        # #print(self.evaluationFunction) #This is what we call to evaluate what exactly is in the game state

        # return minimaxResult[1]


        #Call maximize on the pacman
            #For each action the pacman takes
                #Get the potential action for each ghost (Call minimize)
                #Choose the best (maximum) value for the pacman


        #Minimize function
            #For each ghost except the last
                #For all actions for that ghost
                    #Generate the new successor assuming it has moved a given action
                    #Cafucll Minimize to check against the next ghost

        return self.maximize(gameState, self.depth)[1]

    #maximize the player
    def maximize(self, aGameState, depth):
        if aGameState.isLose() or aGameState.isWin() or depth == 0:
            return self.evaluationFunction(aGameState), None
            
        bestAction = None
        scoreList = []
        actions = aGameState.getLegalActions(0)
        
        #For each legal action for the pacman with the ghost making the worst move
        for act in aGameState.getLegalActions(0):
            #Generate the successor for that action
            successor = aGameState.generateSuccessor(0, act)
            #Check the best actions for each of the ghosts
            scoreList.append(self.minimize(successor, 1, depth))

        bestScore = max(scoreList)
        for scoreIndex in range(len(scoreList)):
            if scoreList[scoreIndex] == bestScore:
                bestAction = actions[scoreIndex]

        return (bestScore, bestAction)


    #minimize the ghost
    def minimize(self, aGameState, ghost, depth):
        if aGameState.isLose() or aGameState.isWin() or depth == 0:
            return self.evaluationFunction(aGameState)
            
        scoreList = []

        #print("Gamestate: ", aGameState)
        actions = aGameState.getLegalActions(ghost)
        #print("Ghost: ", ghost)
        #print("Actions: ", actions)

        #For every ghost except the last ghost (recursive)
        if (ghost != aGameState.getNumAgents()-1):
            #print("------------ IF --------------")

            #For every action that the ghost can take
            for act in aGameState.getLegalActions(ghost):
                #print("------------ IF FOR --------------")
                #See the best action that it can take
                successor = aGameState.generateSuccessor(ghost, act)
                #Call recursion to check more ghosts
                scoreList.append(self.minimize(successor, ghost+1, depth))

        #The last ghost
        else:
            #print("------------ ELSE --------------")
            #For every action that it can take (different branches)
            for act in aGameState.getLegalActions(ghost):
                #See the best ation that it can take
                successor = aGameState.generateSuccessor(ghost, act)
                #Decrement the depth for the next pacman step
                
                scoreList.append(self.maximize(successor, depth-1)[0])
                #print("Scorelist at maximize: ", scoreList)
                

        #Floating up the recursion function
        #Find the 'best' value for the ghost and return it
        #print("End scorelist floating up: ", scoreList)
        lowest_score = min(scoreList)

        return lowest_score

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        return self.maximize(gameState, -999999999, 999999999, self.depth)[1]

    def value(self, aGameState, alpha, beta, depth, agent):
        if aGameState.isLose() or aGameState.isWin() or depth == 0:
            return self.evaluationFunction(aGameState), None
        
        #Choose whether or not you need to do maximizing or minimizing
        #If the agent is a ghost then minimize
        if agent != 0:
            return self.minimize(aGameState, alpha, beta, depth, agent)
        else:
            return self.maximize(aGameState, alpha, beta, depth)


    def maximize(self, aGameState, alpha, beta, depth):

        v = -999999999
        scoreList = []
        actions = aGameState.getLegalActions(0)
        bestAction = None

        #for each successor of the state
        for act in aGameState.getLegalActions(0):
            #Generate the successor
            successor = aGameState.generateSuccessor(0, act)
            #Call value to call minimize
            # (value, action) = self.value(successor, alpha, beta, depth, 1)
            value = self.value(successor, alpha, beta, depth, 1)[0]
            v = max(value, v)
            #Pruning
            if v > beta:
                return (v, None)
            alpha = max(alpha, v)
            scoreList.append(value)

        bestScore = max(scoreList)
        #print("Best Score: ",bestScore)
        for scoreIndex in range(len(scoreList)):
            if scoreList[scoreIndex] == bestScore:
                bestAction = actions[scoreIndex]

        return (bestScore, bestAction)

    def minimize(self, aGameState, alpha, beta, depth, agent):

        v = 999999999
        scoreList = []

        #Not the last ghost so depth stays the same
        if (agent != aGameState.getNumAgents()-1):

            #for each successor of the state
            for act in aGameState.getLegalActions(agent):
                successor = aGameState.generateSuccessor(agent, act)
                v = min(self.value(successor, alpha, beta, depth, agent+1)[0], v)
                if v < alpha:
                    return (v, None)
                beta = min(beta, v)
                scoreList.append(v)

        #The last ghost so we decrement depth and call maximize
        else:
            for act in aGameState.getLegalActions(agent):
                successor = aGameState.generateSuccessor(agent, act)
                v = min(self.value(successor, alpha, beta, depth-1, 0)[0], v)
                if v < alpha:
                    return (v, None)
                beta = min(beta, v)
                scoreList.append(v)

        return (min(scoreList), None)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def arcConsistencyCSP(csp):
    """
    Implement AC3 here
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
