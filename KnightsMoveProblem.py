vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

validMoves = [{'x': 1, 'y': 2}, 
              {'x': 1, 'y': -2},
              {'x': -1, 'y': 2},
              {'x': -1, 'y': -2},
              {'x': 2, 'y': 1}, 
              {'x': 2, 'y': -1},
              {'x': -2, 'y': 1},
              {'x': -2, 'y': -1}]



'''
countKnightPaths
    Accepts a starting coordinate for our matrix and counts the number of valid night paths with
    a length of eight moves. Valid moves must be within matrix bounds, not lead to an empty spot, and must not
    lead to a third vowel if we alread have stopped at two.


    -   matrix: Unaltered matrix that we are navigating and check our move against
    -   x: Our current x coordinate
    -   y: Our current y coordinate
    -   knightMoves: The number of valid moves up until now.
    -   vowelCount: The number of vowels currently in our path 
'''
def countKnightPaths(matrix, currentX: int, currentY: int, knightMoves: int = 0, vowelCount: int = 0):
    # Check if the move was within matrix bounds
    if (currentX not in range(len(matrix[0])) or currentY not in range(len(matrix))) or (matrix[currentX][currentY] is None):
        return 0

    # Check if the valid move was a vowel or empty. If the vowel count is greater than 2 then the move was invalid.
    newVowelCount = vowelCount + 1 if matrix[currentX][currentY] in vowels else vowelCount

    if (vowelCount > 2):
        return 0
    if knightMoves == 7:
        return 1

    # Iterate through all possible moves recursively and add the number of good paths to the total.
    validPaths = 0
    for move in validMoves:
        newX = move['x'] + currentX
        newY = move['y'] + currentY
        validPaths += countKnightPaths(matrix, newX, newY, knightMoves + 1, newVowelCount)

    return validPaths


def solveMatrix(matrix):
    validPathsInMatrix = 0

    # Iterate through each cell in the matrix and get the number of valid paths from each.
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            validPathsInMatrix += countKnightPaths(matrix, x, y)

    print('Valid Paths In Matrix: ' + str(validPathsInMatrix))


testMatrix =    [['A', 'B', 'C', None, 'E'],
                 [None, 'G', 'H', 'I', 'J'],
                 ['K', 'L', 'M', 'N', 'O'],
                 ['P', 'Q', 'R', 'S', 'T'],
                 ['U', 'V', None, None, 'Y']]

print('Starting test')
#print('Number of paths: ' + str(countKnightPaths(testMatrix, 0, 0)))
solveMatrix(testMatrix)
