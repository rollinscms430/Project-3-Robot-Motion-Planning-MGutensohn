### Motion planning on a rectangular grid

from random import random
from random import seed
from Queue import PriorityQueue
from copy import deepcopy


class State(object):
    
    def __init__(self, start_position, goal_position, start_grid):
        self.position = start_position
        self.goal = goal_position
        self.grid = start_grid
        self.total_moves = 0
        
    #--- Fill in the rest of the class...
        

def create_grid():
    
    """Create and return a randomized grid
    
        0's in the grid indcate free squares
        1's indicate obstacles
        
        DON'T MODIFY THIS ROUTINE.
    """
    
    # Start with a num_rows by num_cols grid of all zeros
    grid = [[0 for c in range(num_cols)] for r in range(num_rows)]
    
    # Put ones around the boundary
    grid[0] = [1 for c in range(num_cols)]
    grid[num_rows - 1] = [1 for c in range(num_cols)]

    for r in range(num_rows):
        grid[r][0] = 1
        grid[r][num_cols - 1] = 1
            
    # Sprinkle in obstacles randomly
    for r in range(1, num_rows - 1):
        for c in range(2, num_cols - 2):
            if random() < obstacle_prob:
                grid[r][c] = 1;

    # Make sure the goal and start spaces are clear
    grid[1][1] = 0
    grid[num_rows - 2][num_cols - 2] = 0
            
    return grid
    

def print_grid(grid):
    
    """Print a grid, putting spaces in place of zeros for readability
    
       DON'T MODIFY THIS ROUTINE.
    """
    
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                print ' ',  # Ending comma prevents automatic newline
            else:
                print grid[r][c],
        print ''
            
    print ''

    return 


def main():
    
    # Setup the randomized grid
    grid = create_grid()
    print_grid(grid)
    
    # Initialize the starting state and priority queue
    start_position = (1, 1)
    goal_position = (num_rows - 2, num_cols - 2)
    start_state = State(start_position, goal_position, grid)
    start_state.grid[1][1] = '*'
    priority = start_state.total_moves + start_state.manhattan_distance()
    
    queue = PriorityQueue()
    
    # Insert as a tuple
    # The queue orders elements by the first tuple value
    # A call to queue.get() returns the tuple with the minimum first value
    queue.put((priority, start_state))
    
    # Maybe you need a dictionary of previously visited positions?
    
    #--- Fill in the rest of the search...
    

if __name__ == '__main__':
    
    seed(0)
    
    #--- Easy mode
    
    # Global variables --- saves us the trouble of continually passing them as
    # parameters to every routine
    num_rows = 8
    num_cols = 16
    obstacle_prob = .20
    
    for trial in range(5):
        print '\n\n-----Easy trial ' + str(trial + 1) + '-----'
        main()
        
    #--- Uncomment the following sets of trials when you're ready
        
    #--- Hard mode
    num_rows = 15
    num_cols = 30
    obstacle_prob = .30
    
    for trial in range(5):
        print '\n\n-----Harder trial ' + str(trial + 1) + '-----'
        ###main()
        
    #--- INSANE mode
    num_rows = 20
    num_cols = 60
    obstacle_prob = .35
    
    for trial in range(5):
        print '\n\n-----INSANE trial ' + str(trial + 1) + '-----'
        ###main()
