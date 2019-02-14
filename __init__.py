from sklearn import datasets
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from openpyxl import load_workbook
import numpy as np
from sklearn.model_selection import cross_val_score
from ramdomFlorestTest.writerXslx import iris

def get_row_datas():
    data = []
    workbook = load_workbook('pgsm3.xlsx', data_only=True)
    sheet = workbook.active
    
    rows = sheet.rows
    for row in rows:
        
        column_1  = row[0].value
        column_2  = row[1].value
        column_3  = row[2].value
        column_4  = row[3].value
        column_5  = row[4].value
        
        data.append([column_1, column_2, column_3, column_4, column_5])
        
    return np.asarray(data)

GSM_datas = get_row_datas()

data=pd.DataFrame({
    'standardDeviation':GSM_datas[:,1],
    'maximum':GSM_datas[:,2],
    'minimum':GSM_datas[:,3],
    'range':GSM_datas[:,4],
    'OutORin':GSM_datas[:,0]
})


nw_data = data.sample(frac=1).reset_index(drop=True)

X=data[['standardDeviation', 'maximum', 'minimum', 'range']]  # Features
y=data['OutORin']  # Labels

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
clf=RandomForestClassifier(n_estimators=100)

# #Train the model using the training sets y_pred=clf.predict(X_test)
# clf.fit(X_train,y_train)
# 
# y_pred=clf.predict(X_test)
# #print("Accuracy:",metrics.accuracy_score(y_test, y_pred))




scores = cross_val_score(clf, X, y , cv=10)
print(scores)
print("1 Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


scores = cross_val_score(clf, X, y, cv=10)
print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

'''
result = clf.predict([[1, 1, 1, 1]])



print(result)
'''
