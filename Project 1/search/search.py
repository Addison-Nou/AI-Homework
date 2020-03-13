# search.py
# ---------
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


#Partner: Addison Nou, Connor Weese

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    ^---- OUTPUT:
    [SearchAgent] using function depthFirstSearch
    [SearchAgent] using problem type PositionSearchProblem
    Start: (5, 5)
    Is the start a goal? False
    Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]

    Successors are structured as Next State, action, and cost
    *** Method not implemented: depthFirstSearch at line 94 of /home/cody/Desktop/cse471p1/search.py
    """

    "*** YOUR CODE HERE ***"
    """ BEGIN DFS CODE SEGMENT """
    actions = []
    from util import Stack
    stack = Stack()
    exploredNodes = []
    childParentPair = {}

    #getStartState is returning an (x,y) instead of a node so we can't start with it

    SS = problem.getStartState()
    for successor in problem.getSuccessors(SS):
        stack.push(successor)
        childParentPair[successor] = problem.getStartState()

    while True:
        if (stack.isEmpty()):
            print("Stopping")
            return ["Stop"]
        #While the stack is not empty, pop the top and then add it to the explored nodes list
        current = stack.pop()

        #If the goal has been found then assemble the path
        if (problem.isGoalState(current[0])):
            print("GOAL FOUND: ", current)
            #Loop back through the explored list and find the node's parent in order to construct the action list
            loopstate = current
            while (loopstate != problem.getStartState()):
                actions.append(loopstate[1])
                loopstate = childParentPair[loopstate]
                #print("Current loopstate:", loopstate)
            actions.reverse()
            print("Finished!")
            return actions

        exploredNodes.append(current[0])

        #For all neighbors (successors) of the current node
        for successor in problem.getSuccessors(current[0]):
            #If the neighbor has not been explored yet
            print("Successor being checked: ", successor)

            #If the successor has not been explored yet
            if (successor[0] not in exploredNodes):
                #Add the neighbor to the stack
                stack.push(successor)
                print("Pushed: ", successor)
                childParentPair[successor] = current
                print("Parent: ", childParentPair[successor])
                #print("exploredNodes[current]: ", exploredNodes[current])
            else:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = []
    from util import Queue
    queue = Queue()
    exploredNodes = []
    childParentPair = {}
    exploredNodeFailed = 0

    #getStartState is returning an (x,y) instead of a node so we can't start with it

    #Tuple Form: ((x, y), 'dir', cost)

    # SS = problem.getStartState()
    # for successor in problem.getSuccessors(SS):
    #     queue.update(successor, successor[2])
    #     childParentPair[successor] = problem.getStartState()

    startNode = (problem.getStartState(), None, 0)
    queue.push(startNode)

    if problem.isGoalState(startNode[0]):
        return ["Stop"]

    while True:
        if (queue.isEmpty()):
            print("Stopping")
            return ["Stop"]
        #While the queue is not empty, pop the top and then add it to the explored nodes list
        
        current = queue.pop()

        #print("CURRENT[1][1]: ", current[1][1])
        #print("Current: ", current)

        #If the goal has been found then assemble the path
        if (problem.isGoalState(current[0])):
            print("GOAL FOUND: ", current)
            count = 0
            for x in exploredNodes:
                count = count+1
            print("Number of items in explored: ", count)
            #Loop back through the explored list and find the node's parent in order to construct the action list
            loopstate = current
            while (loopstate[1] != None):
                actions.append(loopstate[1])
                loopstate = childParentPair[loopstate]
                #print("Current loopstate:", loopstate)
            actions.reverse()
            print("Finished!")
            return actions

        if (current[0] not in exploredNodes):
            exploredNodes.append(current[0])
        else:
            exploredNodeFailed = exploredNodeFailed+1
            print("Explored node failed: ", exploredNodeFailed)
            continue

        #For all neighbors (successors) of the current node
        for successor in problem.getSuccessors(current[0]):
            #If the neighbor has not been explored yet
            print("Successor being checked: ", successor)
            
            # fuckyou = []
            # for thing in queue.heap:
            #     fuckyou.append(thing[2])
            #     print("thing added to fuckyou: ", thing)

            #If the successor has not been explored yet
            if (successor[0] not in exploredNodes and successor not in queue.list):
                #if (successor not in queue.heap):
                #Add the neighbor to the stack
                #print("fuckyou: ", fuckyou)
                queue.push(successor)
                childParentPair[successor] = current
                print("Pushed: ", successor)
                print("Parent: ", childParentPair[successor])
                #print ("queue Count: ", queue.count)
                #print("exploredNodes[current]: ", exploredNodes[current])
            else:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def iterativeDeepeningSearch(problem):
    """Search the tree iteratively for goal nodes."""
    "*** YOUR CODE HERE ***"
    actions = []
    from util import Stack
    stack = Stack()
    exploredNodes = []
    childParentPair = {}
    depthPair = {}
    cutoff = 0

    #getStartState is returning an (x,y) instead of a node so we can't start with it

    while True:
        
        exploredNodes = []
        exploredNodeFailed = 0
        startNode = (problem.getStartState(), None, 0)
        stack.push(startNode)
        depthPair[startNode[0]] = 0
        childParentPair[startNode[0]] = None
        currentDepth = 0

        #print("Problem: ", problem)
        # if (stack.isEmpty()):
        #     print("Stopping")
        #     return ["Stop"]
        #While the stack is not empty, pop the top and then add it to the explored nodes list
        

        #print("Entering while loop (cutoff = {0})\n____________________________________________".format(cutoff))
        while(stack.isEmpty() == False):
            
            print("Stack:\n----------")
            for x in stack.list:
                print(x)

            current = stack.pop()

            if (current[0] not in exploredNodes):
                exploredNodes.append(current[0])
            else:
                exploredNodeFailed = exploredNodeFailed+1
                print("Explored node failed: ", exploredNodeFailed)
                continue
            
            print("Current: ", current)
            if(childParentPair[current[0]] != None):
                if (current[0] not in depthPair.keys()):
                    print("{0} being set to depth {1}".format(current[0], depthPair[childParentPair[current[0]]] + 1))
                    depthPair[current[0]] = depthPair[childParentPair[current[0]]] + 1

            #childParentPair is a dict of Node : Node
            #Node is made up of (Name, action, cost)
            #We need childParentPair[Node][0]

            print("Depth:\n----------")
            for x in depthPair:
                print("depthPair[{0}]: {1}".format(x[0], depthPair[x]))

            #If the goal has been found then assemble the path
            if (problem.isGoalState(current[0])):
                print("GOAL FOUND AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n\n", current)
                #Loop back through the explored list and find the node's parent in order to construct the action list
                loopstate = current
                print("Loopstate: ", loopstate)
                for x in childParentPair:
                    print("Key: {0} | Parent: {1}".format(x, childParentPair[x]))
                while (loopstate[1] != None):
                    actions.append(loopstate[1])
                    print("Added: ", childParentPair[loopstate[0]])
                    loopstate = childParentPair[loopstate[0]]

                    #ChildParentPair == string : node
                    #loopstate == node

                    #print("Current loopstate:", loopstate)
                actions.reverse()
                print("Finished!")
                return actions

            #For all neighbors (successors) of the current node
            for successor in problem.getSuccessors(current[0]):
                #If the neighbor has not been explored yet
                print("Successor being checked: ", successor)
                if (successor[0] not in depthPair.keys()):
                    depthPair[successor[0]] = depthPair[current[0]] + 1

                #If the successor has not been explored yet
                if (successor[0] not in exploredNodes and depthPair[current[0]] < cutoff and successor not in stack.list):
                    #Add the neighbor to the stack
                    if (successor[0] not in childParentPair.keys()):
                        childParentPair[successor[0]] = current
                        print("childParentPair[{0}] set to {1}".format(successor, current))
                        print("childParentPair List:\n------------")
                    if (childParentPair[successor[0]] == current):
                        stack.push(successor)
                        print("Pushed: ", successor)
                        for x in childParentPair:
                            print("Key: {0} | Parent: {1}".format(x, childParentPair[x]))
                    else:
                        print("{0} NOT SUCCESSOR of {1}".format(childParentPair[successor[0]], current))
                    #depthPair[successor[0]] = depthPair[current] + 1
                    #print("Parent: ", childParentPair[successor])
                    #print("exploredNodes[current]: ", exploredNodes[current])
                #else:
                    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        cutoff = cutoff + 1


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
iddfs = iterativeDeepeningSearch