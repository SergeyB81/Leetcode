class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 +1):
                self.rec[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]

if __name__ == ('__main__'):
    rc = [[5, 7, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]
    sq = SubrectangleQueries(rc)
    print(sq.rec)
    print(sq.getValue(0,1))
    sq.updateSubrectangle(1,0,2,1,10)
    print(sq.rec)

    #rep5
