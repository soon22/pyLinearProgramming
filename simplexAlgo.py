import numpy as np

class simplex:

    def __init__(self,numberOfVariable, numberOfConstraint,minOrMax, inputArray):
        self.numberOfVariable = numberOfVariable
        self.numberOfConstraint = numberOfConstraint
        self.minOrMax = minOrMax
        self.inputArray = inputArray
        self.enteringColumn = 0
        self.leavingRow = 0
        self.rangeRow = 0
        self.pivot = 0
        self.generateVariable()
        self.solve()


    def generateVariable(self):
        self.varList = []
        self.basicVariableList = []
        for i in range(0,self.numberOfVariable):
            self.varList.append('x'+str(i+1))

        for i in range(0,self.numberOfConstraint):
            j ='s'+str(i+1)
            self.varList.append(j)
            self.basicVariableList.append(j)

        print(self.varList)
        print(self.basicVariableList)


    def solve(self):
        flag = 1
        while(flag == 1):

            #find entering column
            #for maximization & minimization:
            self.rangeRow = self.numberOfConstraint+self.numberOfConstraint
            if self.minOrMax == 0:
                maxNumber = max(self.inputArray[0])
                self.enteringColumn = self.inputArray[0].index(maxNumber)

            elif self.minOrMax == 1:
                minNumber = min(self.inputArray[0])
                self.enteringColumn = self.inputArray[0].index(minNumber)

            #find leaving row
            ratios = []
            ratioNum = []
            lastcolumn = self.numberOfVariable+self.numberOfConstraint
            for x in range(1,self.numberOfConstraint+1):
                if self.inputArray[x][self.enteringColumn]!=0:
                    ratio = self.inputArray[x][lastcolumn]/self.inputArray[x][self.enteringColumn]
                    if ratio >= 0:
                        ratios.append(ratio)
                        ratioNum.append(x)

            minRatio = min(ratios)
            self.leavingRow = ratioNum[ratios.index(minRatio)]

            #change basic variable ,for future GUI
            self.basicVariableList[self.leavingRow-1] = self.varList[self.enteringColumn]

            #pivot
            self.pivot = self.inputArray[self.leavingRow][self.enteringColumn]
            print(self.enteringColumn,self.leavingRow)
            print(self.pivot)
            #Gauss Jordan Elimination


            for item in self.inputArray[self.leavingRow]:
                item = item/self.pivot

            for i in range(0, self.numberOfVariable + self.numberOfConstraint + 1):
                self.inputArray[self.leavingRow][i] = self.inputArray[self.leavingRow][i] / self.pivot

            for i in range(0, self.numberOfConstraint + 1):
                entcolcoeff = self.inputArray[i][self.enteringColumn]
                if i != self.leavingRow:
                    for j in range(0, self.numberOfVariable + self.numberOfConstraint + 1):
                        self.inputArray[i][j] = self.inputArray[i][j] - entcolcoeff * self.inputArray[self.leavingRow][j]

            if self.checkOptimality()==1:
                print(np.array(self.inputArray))
                break
    def checkOptimality(self):
        count = 0
        if self.minOrMax == 0:
            for x in range(0,self.numberOfVariable+self.numberOfConstraint):
                if self.inputArray[0][x] <= 0:
                    count += 1

        if self.minOrMax == 1:
            for x in range(0,self.numberOfVariable+self.numberOfConstraint):
                if self.inputArray[0][x] >= 0:
                    count += 1

        if count == (self.numberOfVariable+self.numberOfConstraint):
            return 1
        else :
            return 0




input =   [[-1,-4,-5,0,0,0,0]
              ,[3,6,3,1,0,0,22]
              ,[1,2,3,0,1,0,14]
              ,[3,2,0,0,0,1,14]]

mom = 1
nov = 3
noc = 3
bacon = simplex(nov,noc,mom,input)

