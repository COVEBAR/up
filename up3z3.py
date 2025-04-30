class Calculation:
    def __init__(self, calculationLine):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, newCalcLine):
        self.calculationLine = newCalcLine
    def SetLastSymbolCalculationLine(self, newCalcSymbol):
        self.calculationLine += newCalcSymbol
    def GetCalculationLine(self):
        print(self.calculationLine)
    def GetLastSymbol(self):
        return self.calculationLine[-1]
    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[0:-1]

calc_line = Calculation("1+2-3")
calc_line.SetLastSymbolCalculationLine(input("calc symbol: "))
print(calc_line.GetLastSymbol())
calc_line.SetCalculationLine(input("calc line: "))
calc_line.DeleteLastSymbol()
calc_line.GetCalculationLine()