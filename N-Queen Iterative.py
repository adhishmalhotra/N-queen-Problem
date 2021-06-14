import time

filename = None


class NQueenIterative:
    timeOfSolution: float
    size: object

    def __init__(mat, size):
        # defines the size of the chess board
        mat.size = size
        # defines the rows and columns
        # determines that the time starts from 0
        mat.timeOfSolution = 0
        # array of the chess board NxN
        mat.queenChess = []

    def isFunc(mat, a, b):
        # It goes through options in the rows and columns to decide where the Queen should go
        for rowA, colB in enumerate(mat.queenChess):
            if abs(a - rowA) != abs(colB - b) and not (rowA == a):
                if colB != b:
                    continue
            return False
        # If the queen is placed in the same row or column or diagonal of another queen
        # then false otherwise it is true
        return True

    # It prints the solution of the chess board NxN
    def printSolution(mat, calculate: object) -> object:
        """

        :rtype: object
        """
        # the word calculate in the string prints the number of solution
        # example; Solution #100
        print('\nSOLUTION #{0}:'.format(str(calculate)))
        filename.write('\nSOLUTION #{0}:\n'.format(str(calculate)))

        a: int
        # calculates the size/range for the rows
        for a in range(mat.size):
            row_num: object = [" / "] * mat.size
            if not a >= len(mat.queenChess):
                row_num[mat.queenChess[a]] = " Q "
                # Organizes the rows in such a matter where it won't look clustered
            print("{0}\n".format(''.join(row_num)))
            filename.write("{0}\n".format(''.join(row_num)))

    def solve(mat, size):
        # b = col  it will be print out as an integer number
        b: int = 0
        # a = row   it will be print out as an integer number
        a: int = 0
        # Calculates the number of solution starting from 1 then 2, then ...
        calculate = 1
        while True:
            # will not be placed at the ending of a column or that will not be considered a safe spot for the Queen
            while not (b >= mat.size or mat.isFunc(a, b)):
                # calculates if the next column in the row will work or not
                b = b + 1
                # if it is not on the end of the column
            if b >= mat.size:
                pass
            else:
                # then add the column as a merger
                mat.queenChess.append(b)
                # queen's have been added to all the rows
                if a != mat.size - 1:
                    # goes on to the next row to see if that works
                    a = a + 1
                    # re-calibrates from the beginning of the row
                    b = 0


                else:
                    if calculate == 1:
                        mat.timeOfSolution = time.time()

                    # prints the calculated solution
                    mat.printSolution(calculate)
                    calculate += 1
                    # the last queen that was placed is removed
                    mat.queenChess.pop()
                    # begins at the end of the column to find another solution
                    b = mat.size
                    # done going through all columns and rows. Also, the queen's have been placed in the rows/columns
            if mat.size <= b:
                if not a == 0:
                    pass
                # starting a new chess board solution, with different solutions/combinations
                else:
                    # all possible solutions have been attempted,
                    # so the program stops calculating new solutions
                    return
                    # return to last calculated column + 1
                b = mat.queenChess.pop() + 1
                # go backwards one row
                a = a - 1
                # all possible solutions have been calibrated for that size of chess board (NxN)

# asks which size chess board to calculate
chessSize = int(input("PLEASE ENTER THE SIZE OF THE CHESS BOARD: "))
# size of 3x3 and under aren't valid
if chessSize > 3:
    queen = NQueenIterative(chessSize)
    # calculating the starting time which is a decimal
    startingTime: float = time.time()
    filename = open("answers.txt", "w+")
    queen.solve(queen.size)
    filename.close()
    # calculating the starting time which is a decimal
    endingTime: float = time.time()
    # Prints the time for the first solution for whatever size that was previously chosen
    print('Time to first: {0}'.format(str(queen.timeOfSolution - startingTime)))
    # Prints the time for how long it took to come up with all the solutions
    # for whatever size that was previously chosen
    print('Time to all: {0}'.format(str(endingTime - startingTime)))
else:
    # If size is 3 or less than 3 run the program again and put a whole number greater that 3
    chessSize = input('Run Again and the size of the Chess board size has to be greater than 3.')
