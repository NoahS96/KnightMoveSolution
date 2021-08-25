'''
Node
    -   letter: A char value associated with a point in the matrix
    -   left: A pointer to the left node from this respective node
    -   right: A pointer to the right node from this respective node
    -   up: A pointer to the up node from this respective node
    -   down: A pointer to the up node from this respective node
'''
class Node:
    letter = None       
    left = None         
    right = None
    up = None
    down = None

    


'''
checkIfPrevious
    Check is the previous node is equal to the next step node. If true then the step is invalid so return None,
    otherwise return the node.
'''
def checkIfPrevious(node: Node, prev: Node):
    if node == prev:
        return None
    return node


'''
checkIsStepThreeValid
    Checks if the prospective step three is a valid move. Checks if the first and second move are in the same direction 
    and if our next move is also in the same direction. If so then the move is invalid as this is a linear move. If the 
    first move is in one axis and the second is in another then the third move must be in the same axis as the second otherwise
    it is invalid. Invalid moves will return a None node.

    -   origin: The node we are currently on.
    -   dest: The node we are considering moving to.
    -   prev: The previous node we came from.
    -   step1horizontal: Boolean indicating if the first step in the knight move was horizontal.
    -   step2horizontal: Boolean indicating if the second step in the knight move was horizontal.
'''
def checkIsStepThreeValid(origin: Node, dest: Node, prev: Node, step1horizontal: bool, step2horizontal: bool):
    # If first and second are horizontal, don't move horizontal. If first is horizontal and second is not, don't move horizontal
    if ((step1horizontal and step2horizontal) and (origin.left == dest or origin.right == dest)) or ((step1horizontal and not step2horizontal) and (origin.left == dest or origin.right == dest)):
        return None
    # If first and second are vertical, don't move horizontal. If first is vertical and second is not, don't move vertical
    if ((not step1horizontal and not step2horizontal) and (origin.up == dest or origin.down == dest)) or ((not step1horizontal and step2horizontal) and (origin.up == dest or origin.down == dest)):
        return None
    return checkIfPrevious(dest, prev)


'''
knightsMove
    Accepts a starting node and will recursively move through neighboring nodes until seven valid knight moves have been made in which it will return a 1 indicating a valid path. Once all 
    paths have been explored then the number of valid paths will be returned.

    -   node: The current position node to move from.
    -   prev: The previous node that we moved from. To start this should be None.
    -   knightMoves: The number of valid knight moves performed up to this point. We are counting a valid path as eight moves total. To start this should be 0.
    -   step: The number of valid steps in a knight move up to this point. There are three steps in a knight move (ex. up, up, left). To start this should be 0.
'''
def knightsMove(node: Node, prev: Node = None, knightMoves: int = 0, step: int = 0, step1Horizontal: bool = False, step2Horizontal: bool = False):
    if (node == None):
        return 0

    if (knightMoves == 7):
        return 1

    if step == 3:
        return knightsMove(node, None, knightMoves + 1, 0, false, false)

    if step == 2: 
        return knightsMove(checkIsStepThreeValid(node, node.left, prev, step1Horizontal, step2Horizontal), node, knightMoves, step + 1, step1Horizontal, step2Horizontal) \
            + knightsMove(checkIsStepThreeValid(node, node.right, prev, step1Horizontal, step2Horizontal), node, knightMoves, step + 1, step1Horizontal, step2Horizontal) \
            + knightsMove(checkIsStepThreeValid(node, node.up, prev, step1Horizontal, step2Horizontal), node, knightMoves, step + 1, step1Horizontal, step2Horizontal) \
            + knightsMove(checkIsStepThreeValid(node, node.down, prev, step1Horizontal, step2Horizontal), node, knightMoves, step + 1, step1Horizontal, step2Horizontal) 

    if step == 1:
        return knightsMove(checkIfPrevious(node.left, prev), node, knightMoves, step + 1, step1Horizontal, true) \
            + nightsMove(checkIfPrevious(node.right, prev), node, knightMoves, step + 1, step1Horizontal, true) \
            + nightsMove(checkIfPrevious(node.up, prev), node, knightMoves, step + 1, step1Horizontal, false) \
            + nightsMove(checkIfPrevious(node.down, prev), node, knightMoves, step + 1, step1Horizontal, false)

    return knightsMove(node.left, prev, node, knightMoves, step + 1, true, false) \
        + nightsMove(node.right, prev, node, knightMoves, step + 1, true, false) \
        + nightsMove(node.up, prev, node, knightMoves, step + 1, false, false) \
        + nightsMove(node.down, prev, node, knightMoves, step + 1, false, false)
     



