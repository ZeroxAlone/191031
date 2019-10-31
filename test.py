# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:55:06 2019

@author: lisa_
"""
#1
def main():
    TicketType = input("Enter a ticket type: ")
    BaggageWeight = eval(input("Enetr a baggage weight: "))
    if TicketType == "E":
        ChargeRate = 3.5
        BaggageAllowance = 16
    if TicketType == "s":
        ChargeRate = 5.75
        BaggageAllowance = 20
    else:
        print("Error type.")
        
    ExcessWeight = BaggageWeight - BaggageAllowance
    
    if ExcessWeight > 0:
        Charge = ExcessWeight * ChargeRate
    else:
        Charge = 0
    
    print("Charge: ", Charge)

main()

#2
def main():
    file = open("PRODUCTS", "r")
    PCode = []
    PDescription = []
    PRetialPrice = []
    i = -1
    while True:
        i += 1        
        PCode.append(file.readline()[:-1])
        if PCode[i] == "":
            PCode.pop(-1)
            break        
        PDescription.append(file.readline()[:-1])
        PRetialPrice.append(eval(file.readline()[:-1]))
        
    file.close()
    print("Product file contents written to arrays")

main()

def main2():
    global PCode
    file = open("PRODUCTS2.txt", "r")
    PCode = []
    PDescription = []
    PRetialPrice = []
    while True:
        Temp = file.readline()[:-1]
        if Temp == "":
            break
        PCode.append(Temp[:4]) 
        PDescription.append(Temp[5:-6])
        PRetialPrice.append(eval(Temp[-5:]))
        
    file.close()
    print("Product file contents written to arrays")

main2()

def ProductCodeSearch(SearchCode):
    for i in range(len(PCode)):
        if PCode[i] == SearchCode:
            ThisIndex = i
            break
        else:
            ThisIndex = -1
    
    return ThisIndex

ProductCodeSearch('0198')

#3
DailyHoursWorked = [5, 10, 10]
ProductionData = [[10, 20, 9],
                  [11, 16, 11],
                  [10, 24, 13],
                  [14, 20, 17]]
WorkerTotal = []

for WorkerNum in range(3):
    WorkerTotal.append(0)

for WorkerNum in range(3):
    for DayNum in range(4):
        WorkerTotal[WorkerNum] += ProductionData[DayNum][WorkerNum]
        
for WorkerNum in range(3):
    WorkerAverage = WorkerTotal[WorkerNum] / ( 4 * DailyHoursWorked[WorkerNum])
    if WorkerAverage < 2:
        print("Investigate", WorkerNum + 1)
        
