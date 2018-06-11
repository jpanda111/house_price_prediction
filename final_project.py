# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:14:07 2018
@author: Dai

The final project must include a Python program or programs that will contain 
at least 6 Python elements from the following list.

1.  Use any data structure like list, dictionary, set or tuple
2.  List comprehension
3.  Dictionary comprehension
4.  Functions
5.  Classes
6.  User created iterators
7.  Importing external modules
8.  Error checks using try-except
9.  File input and output
10. Regular expression
11. Itertools 
12. Decorators

a report in pdf format that will explain the work that you have done 
including any relevant screen-shot and Python program(s) that you have written.

1. Introduction
Describe the problem that you are solving, background information that will 
help the instructors to understand the program
2. Requirements
List all the Python modules that need to be installed. If some of these modules
need a specific version, please indicate so. You can also list any other conditions 
that are needed to run the program.

3. Description of the Python program . 
You need to describe the programs that you wrote.  

4. Screenshots of the program output
If you are using a specific hardware and cannot obtain screenshot, please enclose 
appropriate photographs
  
5. Conclusion
Describe in brief the problem you solved, the program you wrote and obtained output.
 
6. Python program  - If the program is one file, please add it as one of the 
pages in the report. If the code is large and spans more than one file, enclose 
a separate zip file.
 
Go to this link http://www.car.org/marketdata/data/housingdata/ and download 
the Excel file in the link titled, ‘Median Prices of Existing Detached Homes.’ 
Based on the available data, predict the house price in various counties using 
linear regression. Learn more about linear regression at https://en.wikipedia.org/wiki/Linear_regression
You can use Python module scikit learn to program linear regression. Plot house 
prices for two counties in separate graphs and also include the corresponding linear 
regression lines in the graphs. For plotting, you can use Python modules matplotlib or 
plotply. You might have to use Python modules like xlrd or xlwt to read and write excel
files respectively.

"""

from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from xlrd import open_workbook
from mmap import mmap, ACCESS_READ


#with open('houseprice.xls','rb') as f:
#    print open_workbook(file_contents=mmap(f.fileno(), 0, access=ACCESS_READ))
#
#aString = open('houseprice.xls','rb').read()
#print open_workbook(file_contents=aString)

wb = open_workbook("houseprice.xls")
sheet = wb.sheet_by_index(0)
print sheet.name

for row in range(sheet.nrows):
    values=[]
    for col in range(sheet.ncols):
        values.append(sheet.cell(row,col).value)
    print ','.join(values)

#print sheet.nrows
#print sheet.ncols


#def cell_contents(sheet, row_x):
#    result=[]
#    for col_x in range(2, sheet.ncols):
#        cell = sheet.cell(row_x, col_x)
#        result.append((cell, cell.value))
#    return result
#
#print 'XL_CELL_TEXT', cell_contents(sheet, 1)
#print 'XL_CELL_NUMBER', cell_contents(sheet, 2)
#print 'XL_CELL_DATE', cell_contents(sheet, 3)
#print 'XL_CELL_BOOLEAN', cell_contents(sheet, 4)  


#for row_index in range(sheet.nrows):
#    for col_index in range(sheet.ncols):
#        print cellname(row_index, col_index), "-",
#        print sheet.cell(row_index, col_index).value

"""
# linear regression examples

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_pred = regr.predict(diabetes_X_test)
print("Coefficients: \n", regr.coef_)
print("Mean squared error：%0.2f" %mean_squared_error(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
"""
