
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """

        # Your code
        # the agents are in the same row/column
        # getAction, AgentState, GetGhostStates()
        # if ghost.getDirection.x == pacman.getDirection.x or pacman.y == ghost.y:
        #if ghost.getDirections.x in pacman.getDirections.x:
            # the ghost is not frightened
        if not ghost.isScared:
            # the agents are <= dist units away from one another
            if (abs(ghost.x - pacman.x)) or (abs(ghost.y - pacman.y)) <= dist:
                return ghost.Directions
        else:
            # if not in danger agent stops/ left turn behavior
            Directions.STOP

        raise NotImplemented

    def getAction(self, state):
        """
        state - GameState
        
        Fill in appropriate documentation
        """

        raise NotImplemented
