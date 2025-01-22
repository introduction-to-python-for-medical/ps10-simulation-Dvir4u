import copy


def spread_fire(grid):
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):  # Iterate through all rows, including the last one
        for j in range(grid_size):  # Iterate through all columns, including the last one
            if grid[i][j] == 1:  # If the cell contains a tree
                neighbors = []
                # Check the neighbors and add them to the list (make sure not to go out of bounds)
                if i > 0:  # Check the cell above
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # Check the cell below
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Check the cell to the left
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # Check the cell to the right
                    neighbors.append(grid[i][j+1])
                # If any neighbor is burning, set this cell on fire
                if 2 in neighbors:
                    update_grid[i][j] = 2
    return update_grid
    

