class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Handle empty grid edge case
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Right, Down, Left, Up
        
        # Helper function to check if coordinates are within bounds
        def in_bound(r, c):
            # 0 <= r < rows AND 0 <= c < cols
            return 0 <= r < rows and 0 <= c < cols

        # DFS function to explore and mark an entire island
        def check_directions(r, c):
            # 1. Base Case: Mark the current cell as visited (change '1' to '2')
            # This is critical and was missing/incorrectly placed.
            grid[r][c] = "2" 
            
            # 2. Explore neighbors
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # Check if neighbor is in bounds AND is unvisited land ('1')
                if in_bound(new_r, new_c) and grid[new_r][new_c] == "1":
                    # Recursively explore the connected land
                    check_directions(new_r, new_c)

        count = 0
        
        # Iterate over every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land ('1'), we found a new island
                if grid[i][j] == "1":
                    count += 1
                    # Start DFS to mark the entire island as visited ('2')
                    check_directions(i, j)
                    
        return count
