from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
import pandas as pd
import numpy as np
import math
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.preprocessing import LabelEncoder, Imputer
import warnings

warnings.filterwarnings('ignore')
#preprocessing step ------------------------------------
#return id data
def id(data,i):
    if(data.iat[i,11]==1):
        value="Secret Identity"
    elif(data.iat[i,12]==1):
        value="Public Identity"
    elif(data.iat[i,13]==1):
        value="No Dual Identity"

    return value    

#return gender data
def gender(data,i):
    if(data.iat[i,14]==1):
        value="Male Characters"
    elif(data.iat[i,15]==1):
        value="Female Characters"
    elif(data.iat[i,16]==1):
        value="Agender Characters"
    elif(data.iat[i,17]==1):
        value="Genderfluid Characters"

    return value

#return ratio list
def ratio(data,values,index):
    p=[]

    for i in range(0,len(values)):
        n=0
        for j in range(0,len(data)):
            if(data.iat[j,index]==values[i]):
                n=n+1
        print(n)
        p.append(n/len(data))
        
    return p
        
#return hair data by value of rHair column
def hair(data,i,hair):

    rand=data["rHair"]

    for j in range(0,len(hair)):
        if(rand[i]==j):
            return hair[j]

#return eye data by value of rEye column
def eye(data,i,eye):
    
    rand=data["rEye"]

    for j in range(0,len(eye)):
        if(rand[i]==j):
            return eye[j]

#return align data by value of rAlign column
def align(data,i):

    rand=data["rAlign"]
    
    if(rand[i]==0):
        value="Bad Characters"
    elif(rand[i]==1):
        value="Good Characters"
    elif(rand[i]==2):
        value="Neutral Characters"

    return value

#return alive data by value of rAlive column
def alive(data,i):
    rand=data["rAlive"]

    if(rand[i]==0):
        value="Deceased Characters"
    elif(rand[i]==1):
        value="Living Characters"

    return value


#Read dataset    
data=pd.read_csv('Marvel_Data.csv')

#assign align label depending on the ratio
ran_align=np.random.choice(3,len(data),p=[0.5,0.34,0.16])
data["rAlign"]=ran_align

#Assigned to nan
for i in range(0,len(data)):
    if(pd.isnull(data.iat[i,3])):
        data.iat[i,3]=align(data,i)
        
#drop unnecessary column
data.drop(['rAlign'], axis='columns', inplace=True)

#assign alive label depending on the ratio
ran_alive=np.random.choice(2,len(data),p=[0.23,0.77])
data["rAlive"]=ran_alive

#Assigned to nan
for i in range(0,len(data)):
    if(pd.isnull(data.iat[i,7])):
        data.iat[i,7]=alive(data,i)
        
#drop unnecessary column
data.drop(['rAlive'], axis='columns', inplace=True)

#eye
eyes=['Blue Eyes', 'Brown Eyes', 'Green Eyes', 'Black Eyes', 'Yellow Eyes',
       'Violet Eyes', 'Red Eyes', 'White Eyes', 'Yellow Eyeballs', 'Grey Eyes',
       'Hazel Eyes', 'Silver Eyes', 'Purple Eyes', 'Orange Eyes',
       'Variable Eyes', 'One Eye', 'Pink Eyes', 'Gold Eyes', 'Amber Eyes',
       'No Eyes', 'Multiple Eyes', 'Black Eyeballs', 'Magenta Eyes',
       'Compound Eyes']
temp=data['EYE'].value_counts()
p=temp/len(data)
sum=0
for i in range(0,23):
    sum=sum+p[i]

#assign eye label depending on the ratio

ran_eye=np.random.choice(len(eyes),len(data),p=[2.93478261e-01,2.88776258e-01,8.70175867e-02,8.34147533e-02,5.86834392e-02,3.90815828e-02,3.18759160e-02,2.44870542e-02,
                                                2.40595994e-02,1.42892037e-02,1.20908647e-02,5.98436737e-03,4.33561309e-03,3.96922325e-03,3.84709331e-03,3.23644358e-03,
                                                3.05324866e-03,1.58768930e-03,1.52662433e-03,1.40449438e-03,9.77039570e-04,3.05324866e-04,1.83194919e-04,1-sum])
data["rEye"]=ran_eye

#Assigned to nan
for i in range(0,len(data)):
    if(pd.isnull(data.iat[i,4])):
        data.iat[i,4]=eye(data,i,eyes)
        
#drop unnecessary column
data.drop(['rEye'], axis='columns', inplace=True)

#hair
hairs=['Black Hair', 'Brown Hair', 'Blond Hair', 'No Hair', 'Bald',
       'White Hair', 'Grey Hair', 'Red Hair', 'Variable Hair', 'Purple Hair',
       'Green Hair', 'Auburn Hair', 'Blue Hair', 'Strawberry Blond Hair',
       'Orange Hair', 'Yellow Hair', 'Pink Hair', 'Silver Hair', 'Gold Hair',
       'Reddish Blond Hair', 'Light Brown Hair', 'Magenta Hair',
       'Orange-brown Hair', 'Dyed Hair', 'Bronze Hair']
temp=data['HAIR'].value_counts()
p=temp/len(data)
sum=0
for i in range(0,24):
    sum=sum+p[i]

#assign hair label depending on the ratio

ran_hair=np.random.choice(len(hairs),len(data),p=[3.06485100e-01,1.91621886e-01,1.30129458e-01,9.65437225e-02,6.91255496e-02,4.54323400e-02,4.20127015e-02,3.77992184e-02,
                                                1.66096727e-02,1.56326331e-02,8.97655105e-03,6.41182218e-03,4.33561309e-03,3.72496336e-03,3.72496336e-03,2.38153395e-03,
                                                2.25940401e-03,1.70981925e-03,6.71714704e-04,6.71714704e-04,6.10649731e-04,4.27454812e-04,1.83194919e-04,1.22129946e-04,1-sum])
data["rHair"]=ran_hair

#Assigned to nan
for i in range(0,len(data)):
    if(pd.isnull(data.iat[i,5])):
        data.iat[i,5]=hair(data,i,hairs)
        
#drop unnecessary column
data.drop(['rHair'], axis='columns', inplace=True)

#data restructering
data['SEX']=None
for i in range(0,len(data)):
    data.at[i,'SEX']=gender(data,i)

data['ID']=None
for i in range(0,len(data)):
    data.at[i,'ID']=id(data,i)

#drop unnecessary column
data.drop(['Secret Identity'], axis='columns', inplace=True)
data.drop(['Public Identity'], axis='columns', inplace=True)
data.drop(['No Dual Identity'], axis='columns', inplace=True)
data.drop(['Male Characters'], axis='columns', inplace=True)
data.drop(['Female Characters'], axis='columns', inplace=True)
data.drop(['Agender Characters'], axis='columns', inplace=True)
data.drop(['Genderfluid Characters'], axis='columns', inplace=True)
    

#print(data.isnull().sum())

#grouping
data['group'] = np.nan

for i in range(len(data)):
    appear = data.at[i, 'APPEARANCES']
    if(appear >=140):
        data.at[i, 'group'] = int(1)
    elif(35 <= appear and appear <= 139):
        data.at[i, 'group'] = int(2)
    elif(22 <= appear and appear <= 34):
        data.at[i, 'group'] = int(3)
    elif(9 <= appear and appear <= 21):
        data.at[i, 'group'] = int(4)
    elif(7 <= appear and appear <= 8):
        data.at[i, 'group'] = int(5)
    elif(4 <= appear and appear <= 6):
        data.at[i, 'group'] = int(6)
    elif(2 <= appear and appear <= 3):
        data.at[i, 'group'] = int(7)
    elif(appear == 1):
        data.at[i, 'group'] = int(8)
    else:
        data.at[i, 'group'] = int(9)
##print(data['group'].value_counts())

#-----------------------------------------------Data Analysis-----------------------
trainSize = 20

trainSetList = []
#train data set list
trainTargetList = []
#target data list
testSet = []

featureDataSet = data.drop(['page_id'], axis=1)
featureDataSet = featureDataSet.drop(['name'], axis=1)
featureDataSet = featureDataSet.drop(['SPECIES'], axis=1)
featureDataSet = featureDataSet.drop(['APPEARANCES'], axis=1)
featureDataSet = featureDataSet.drop(['FIRST APPEARANCE'], axis=1)
featureDataSet = featureDataSet.drop(['Year'], axis=1)

##data_child = dataa[dataa[drop_feature]==drop_feature_unique[i]]

tempTest = pd.DataFrame({'ALIGN': 'Good Characters', 'EYE':'Blue Eyes', 
                            'HAIR' : 'Blond Hair', 'GSM':'Heterosexual Characters',
                            'ALIVE':'Living Characters', 'ID': 'Public Identity',
                            'SEX':'Male Characters', 'group':pd.Series([1])})

tempTestSet = pd.DataFrame({'ALIGN': 'Good Characters', 'EYE':'Blue Eyes', 
                            'HAIR' : 'Blond Hair', 'GSM':'Heterosexual Characters',
                            'ALIVE':'Living Characters', 'ID': 'Public Identity',
                            'SEX':'Male Characters', 'group':pd.Series([1])})

for q in range(int(len(featureDataSet)/100)):
    tempTestSet.loc[q+1] = tempTest.loc[0]

print(int(len(featureDataSet)/100))

print(tempTestSet)

print("**************************")
print(tempTestSet)
testSet.append(tempTestSet)

for j in range(trainSize):#import data sets
    #split dataset
    

    train, test = train_test_split(featureDataSet,test_size=0.01)
    trainSetList.append(train.drop(['group'],axis=1))#train Set
    trainTargetList.append(train['group'])#train target
    testSet.append(test)
#test!!!!
#------------------------------------bootstrap-----------

predictList = []

for i in range(trainSize):#10 train set
    X_train = trainSetList[i]
    y_train = trainTargetList[i]
    test = testSet[i]

    le1 = LabelEncoder()
    le2 = LabelEncoder()
    le3 = LabelEncoder()
    le4 = LabelEncoder()
    le5 = LabelEncoder()
    le6 = LabelEncoder()
    le7 = LabelEncoder()
    
    X_train.iloc[:,0] = le1.fit_transform(X_train.iloc[:,0])
    X_train.iloc[:,1] = le2.fit_transform(X_train.iloc[:,1])
    X_train.iloc[:,2] = le3.fit_transform(X_train.iloc[:,2])
    X_train.iloc[:,3] = le4.fit_transform(X_train.iloc[:,3])
    X_train.iloc[:,4] = le5.fit_transform(X_train.iloc[:,4])
    X_train.iloc[:,5] = le6.fit_transform(X_train.iloc[:,5])
    X_train.iloc[:,6] = le7.fit_transform(X_train.iloc[:,6])

    test.iloc[:,0] = le1.fit_transform(test.iloc[:,0])
    test.iloc[:,1] = le2.fit_transform(test.iloc[:,1])
    test.iloc[:,2] = le3.fit_transform(test.iloc[:,2])
    test.iloc[:,3] = le4.fit_transform(test.iloc[:,3])
    test.iloc[:,4] = le5.fit_transform(test.iloc[:,4])
    test.iloc[:,5] = le6.fit_transform(test.iloc[:,5])
    test.iloc[:,6] = le7.fit_transform(test.iloc[:,6])
    

    marvel_tree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=7, random_state=0)#make decision tree model
    marvel_tree.fit(X_train, y_train)
    y_pred_tr = marvel_tree.predict(test.iloc[:,:-1])#predict by the model
    predictList.append(y_pred_tr)#save the predict result
'''
for i in range(trainSize):
    print('%.2f' % accuracy_score(testSet[0].iloc[:,-1], predictList[i]))
'''
#----------------------------------------------------------random forest---------

predict = []
for i in range(len(testSet[0])):#test
    groupVoting = [0,0,0,0,0,0,0,0,0]
    #count value
    
    for j in range(trainSize):
        Index = predictList[j][i] - 1
        groupVoting[int(Index)] = groupVoting[int(Index)] +1
    #voting

        
    max_num = max(groupVoting)
    index_num = groupVoting.index(max_num)

    predict.append(index_num+1)
    #voting result
        
'''
for i in range(10):
    tempDF = pd.DataFrame(predictList[i])
    print(tempDF[0].value_counts())
'''
temp1 = pd.DataFrame(predictList)
temp2 = temp1
temp2.loc[trainSize] = np.nan
for i in range(len(testSet[0])):
    temp2.iloc[trainSize, i] = predict[i]

#make voting matrix

print('-------------------------------------voting: ')
print(temp2)
print()

print('-------------------------------------confusion matrix: ')
print(confusion_matrix(testSet[0].iloc[:,-1],predict))
print()

print('-------------------------------------report: ')
print(classification_report(testSet[0].iloc[:,-1],predict))
print()

print('-------------------------------------Accuracy:')
print('%.2f' % accuracy_score(testSet[0].iloc[:,-1], predict))
#print
