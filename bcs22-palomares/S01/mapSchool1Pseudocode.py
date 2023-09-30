# LOCATE SHORT PATH:
# Initialize 'distances' and 'shortestPath' as empty dictionaries
# Initialize 'currentDistance' and 'currentPoint' to 0 and 'start' respectively

# WHILE LOOP: while True
    # IF 'currentDistance' > 'distances[currentPoint]' THEN continue

    # FOR EACH 'neighbor' of 'currentPoint'
        # Calculate 'newDistance' as 'currentDistance' + distance from 'currentPoint' to 'neighbor'
        # IF 'newDistance' < 'distances[neighbor]'
            # Update 'distances[neighbor]' to 'newDistance'
            # Update 'shortestPath[neighbor]' to include 'currentPoint' as the previous point

    # Mark 'currentPoint' as visited

    # IF 'currentPoint' is the 'end' point
        # Create 'shortestPathList' by backtracking from 'end' to 'start' using 'shortestPath'
        # RETURN 'distances[end]' and 'shortestPathList'

    # Find the next 'currentPoint' with the smallest 'distances' value among unvisited points

# END WHILE

# List all paths:
# Initialize 'locations' as a list containing Home, Store A, Store B, School, Intersection

# WHILE LOOP: while True
    # Print "LOCATIONS: Home, Store A, Store B, School, Intersection"
    # Ask input for 'startPoint' with "Where is your starting point?:"

    # IF 'startPoint' is in 'locations'
        # WHILE LOOP: while True
            # Ask for 'endPoint' input with "Where do you want to go:"

            # IF 'endPoint' is in 'locations' THEN break
            # ELSE print "Invalid endpoint. Please type another location."

        # CALL 'short path' function to find the shortest path and distance between 'startPoint' and 'endPoint'
        # IF length of 'shortestPath' = 1
            # IF 'startPoint' = 'endPoint' THEN
                # Print "Shortest Distance:", 'distances[endPoint]'
                # Print "Shortest Path:", 'shortestPath'
            # ELSE print "Invalid path. Please try again"
        # ELSE
            # Print "Shortest Distance:", 'distances[endPoint]'
            # Print "Shortest Path:", 'shortestPath'

    # ELSE print "Invalid starting point. Please type another location."

# END WHILE
