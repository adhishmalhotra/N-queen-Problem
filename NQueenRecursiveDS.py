#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
class NQueens:
    #constructor function
    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size #stores the size of the n*n chess board
        self.solutions = 0 #stores the number of solutions
        self.timeSpent = 0 #variable in order to calculate the time spent
        self.solve() #method to solve the number of possible solutions

    def solve(self):
        #solving the n queen puzzle and printing the number of solutions which were found
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
    #this method try to put a queen on target_row by checking all the N possible cases
    #if a valid case is found the function calls itself
    #the method calls itself until the next row until all the queens are placed on the chess board
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.show_full_board(positions)
            # self.show_short_board(positions)
            self.solutions += 1
            if(self.solutions == 1):
                self.timeSpent = time.time()
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        #this method checks if a given position of the queen is under attack or not
        #from any of the previously places queens
        #this particular part of the code checks the column and diagonal positions
        for i in range(ocuppied_rows):
            if positions[i] == column or                 positions[i] - i == column - ocuppied_rows or                 positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        #this function just the full N*N board
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        #shows the positions of the queens on the chess board in compressed form
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    #this is the main function which initializes and solves for the n queen puzzle
    StartTime = time.time()
    NQ = NQueens(int(input("Enter the size of your N:")))
    EndTime = time.time()
    print("time to first:" + str(NQ.timeSpent - StartTime))
    print("time to print them all:" + str(EndTime - StartTime))
    print("Done!")

if __name__ == "__main__":
    main()


# In[ ]:




