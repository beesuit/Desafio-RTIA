import xlsxwriter
from sklearn import datasets

iris = datasets.load_iris()

print(iris.data)
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

for i, row in enumerate(iris.data):
    print(i, row)
    # Write some numbers, with row/column notation.
    worksheet.write(i, 0, row[0])
    worksheet.write(i, 1, row[1])
    worksheet.write(i, 2, row[2])
    worksheet.write(i, 3, row[3])
    
workbook.close()