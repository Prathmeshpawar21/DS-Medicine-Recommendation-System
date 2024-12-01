#!/usr/bin/env python
# coding: utf-8

# In[1578]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 



# In[1579]:


df = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\Training.csv")
df.tail()


# In[1580]:


df.isnull().sum()
df.shape


# In[1581]:


df.info()


# In[1582]:


df.columns.unique()


# In[1583]:


from sklearn.preprocessing import LabelEncoder


lc = LabelEncoder()
lc.fit(df['prognosis'])
labelEnc = lc.transform(df['prognosis'])

# Get Label Encoder Mapping
# print(lc.classes_)
# print(labelEnc.tolist())
diseaseEncodedList ={}
for i, label in enumerate(lc.classes_):
    # print(f"{i} -> {label}")
    diseaseEncodedList[i] = label
diseaseEncodedList # example 40 


# In[1584]:


from sklearn.model_selection import train_test_split

inputData = df.drop(columns="prognosis")
OutputData = labelEnc

x_train, x_test, y_train, y_test = train_test_split(inputData,OutputData, train_size=0.90, random_state=42,shuffle=True)
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

# print(OutputData.tolist())

# print(df['prognosis'].unique())


# In[ ]:





# In[1585]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# modelDict = {
#     "RandomForestClassifier": RandomForestClassifier(),
#     "KNeighborsClassifier" : KNeighborsClassifier(),
#     "SVC": SVC(),
#     "DecisionTreeClassifier" : DecisionTreeClassifier()
# }

# for model_name, model in modelDict.items():
    
#     model.fit(x_train,y_train)
#     cm = confusion_matrix(y_test,model.predict(x_test))
#     print(model_name ," Score : ",model.score(x_test,y_test)*100)
#     print(model_name, " Accuracy : ",accuracy_score(y_test,model.predict(x_test)))
    # print(cm)
    
    # print(c)
        # model.accuracy 


# In[1586]:


model = SVC()
model.fit(x_train,y_train)
model.score(x_test,y_test)*100


# In[1587]:


import pickle as pkl 
# pkl.dump(svc,open("Model.pkl",'wb'))


# In[1588]:


# print(x_test)
# print(y_test[10])


# In[1589]:


index = 3
# print(model.predict([x_test.iloc[index].tolist()]))
# print(y_test[index])
result = y_test[index]


# In[1590]:


diseaseEncodedList[result]


# In[1591]:


df['prognosis'].iloc[3081] #double conformation


# # Logic Mapping

# In[1592]:


# userInputSymptomList = input("Enter Symptoms : ")
# userInputSymptomList = [input.strip() for input in userInputSymptomList.split(",")] 
# print(userInputSymptomList)


userInputtedlist = "skin_rash,joint_pain, skin_peeling, silver_like_dusting, small_dents_in_nails, inflammatory_nails" # Tempraory making of use 


# ### Prediction Function

# In[1593]:


def get_prediction(userInput):

    print("User Input : ",userInput)
    
    col = df.columns.tolist()                                       #Getting Column-Name for (Predicting DataFrame )
    col.remove("prognosis")
    
    emptyZeroArray = np.zeros(len(df.columns)-1).tolist()           # Creating Array of 0's for (Predicting DataFrame )
    userInputDf = pd.DataFrame([emptyZeroArray],columns=col)        # (Predicting DataFrame) Created for Prediction

    userInput = [input.strip() for input in userInput.split(",")]   # User Input chi List Created 
    for sym in userInput:
        userInputDf[sym] = 1
    # userInputDf
    
    predicted_value = model.predict(userInputDf)[0]    #####  Make Prediction on (Predicting DataFrame )  #####
    print('predicted_value :' ,predicted_value)
    PersonDisease = diseaseEncodedList[predicted_value]
    # print(PersonDisease)
    return PersonDisease
    
    


# In[1594]:


FinalOutput_PersonDisease = get_prediction(userInputtedlist)
print(FinalOutput_PersonDisease)
# df.columns
# df.iloc[4918].tolist()
# for col in df.columns:
#     if df.iloc[4918][col] == 1:
#         print(col)


# In[ ]:





# ## Other Dataset loading 

# In[ ]:


Description = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\description.csv")
Diet = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\diets.csv")
Medication = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\medications.csv")
Precaution = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\precautions_df.csv")
# symptomSeverity = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\Symptom-severity.csv")
Workout = pd.read_csv(r"E:\DataScientist\DS-Medicine-Recommendation-System\notebook\dataset\workout_df.csv")


# In[1596]:


# Description.head()


# In[1597]:


# Diet.head()


# In[1598]:


# Medication.head()


# In[1599]:


Precaution.drop(columns='Unnamed: 0',inplace=True)
# Precaution.head()


# In[1600]:


Workout.drop(columns=['Unnamed: 0.1','Unnamed: 0'],inplace=True)
Workout.rename(columns={'disease':'Disease','workout':'Workout'},inplace=True)
# Workout.head()


# In[1601]:


# Description[Description['Disease'] == FinalOutput_PersonDisease]['Description'].tolist()
# Precaution[Precaution['Disease'] == 'Drug Reaction'][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()


# #### Other Details Fetching regarding to Disease --  (Description, Diet, Medication, Precaution, Workout)

# In[ ]:

def otherDetails(Predicted_Dis):
    desc = Description[Description['Disease'] == Predicted_Dis]['Description'].tolist()

    diet = Diet[Diet['Disease'] == Predicted_Dis]['Diet'].tolist()
    diet = diet[0].replace('[','').replace( ']','').replace("'",' ')
    diet = diet.split(',')
    

    med = Medication[Medication['Disease'] == Predicted_Dis]['Medication'].tolist()
    med = med[0].replace('[','').replace( ']','').replace("'",' ')
    med = med.split(',')

    prec = Precaution[Precaution['Disease'] == Predicted_Dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()
    prec = prec[0]

    work = Workout[Workout['Disease'] == Predicted_Dis]['Workout'].tolist()

    return desc, diet, med, prec , work

desc, diet, med, prec,  work = otherDetails(FinalOutput_PersonDisease)


# print("Description:", desc)
# print(type(desc))
# print()

# print("Diet:", diet)
# print(type(diet))
# print()

# print("Medication:", med)
# print(type(med))
# print()

# print("Precaution:", prec)
# print(type(prec))
# print()

# print("Workout:", work)
# print(type(work))
# print()


# In[ ]:




