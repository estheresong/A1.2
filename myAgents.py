import myAgents
import pacmanAgents
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
        """
        inDanger(pacman, ghost) - Is the pacman in danger
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

        # the ghost is not frightened
        if not ghost.isScared:
            # check if agents are in the same row/column
            if ghost.getPosition()[0] == pacman.getPosition()[0] or ghost.getPosition()[1] == pacman.getPosition()[1]:
                # the agents are <= dist units away from one another
                if abs(ghost.pos()[0] - pacman.pos()[0]) or abs(ghost.pos()[1] - pacman.pos()[1]) <= dist:
                    return ghost.Directions
        else:
            # if not in danger agent stops/ left turn behavior
            return Directions.STOP

        # raise NotImplemented

    def getAction(self, state):
        """
        state - GameState
        """
        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # Get the agent's state from the game state and find agent heading
        agentState = state.getPacmanState()
        ghostStates = state.getGhostStates()
        heading = agentState.getDirection()

        # if the pacman is actually in danger, these steps will be taken
        self.inDanger(pacman, state.getGhostStates()[0])
        self.inDanger(pacman, state.getGhostStates()[1])

        # runs left turn agent when not in danger
        return pacmanAgents.LeftTurnAgent.getAction(self, state)