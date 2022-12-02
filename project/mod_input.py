#!/usr/bin/env python3

"""
Module to play sounds when ultrasonic sensor detects object within hot-encoded ranges.
This file must be run on the robot.
"""


#x values starting left to right
x_values = [0,-115, -230, -345, -460]
y_values = [-710, -600,-480,-360,-240] #y values from bottom up

def algorithm():        
        
        inputArray = [1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1]
        
        print(len(inputArray))
        
#         finalInputArray = []
#         
#         currentSmallArray = []
#         
#         for unit in inputArray:
#             currentSmallArray.append(unit)
#             if (len(currentSmallArray) == 5):
#                 finalInputArray.append(currentSmallArray)
#                 currentSmallArray = []
#             
#             
#         print(finalInputArray)
#         
#         print(len(finalInputArray))
#         
#         print(sum(finalInputArray[0]))


        modInputArray = []
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        modInputArray.append([])
        
        k = 0
        for unit in inputArray:
            modInputArray[k].append(unit)
            k = k + 1
            k = k%5                    

        for array in modInputArray:
            array.reverse()
            
        print(modInputArray)
        
        
        for column in range(len(modInputArray)):
            print("current column " + str(column) + " with " + str(x_values[column]))
            if (sum(modInputArray[column]) > 0): print("not empty")
            for row in range(len(modInputArray[column])):
                if (modInputArray[column][row] == 1):    
                    print(y_values[row])
            print("column " + str(column) + " done")
        
        
        
        

if __name__ == "__main__":
    algorithm()