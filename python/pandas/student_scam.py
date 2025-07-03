import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


filepath = r"C:\Users\devan\OneDrive\Documents\programming\first-repo\subjects_data_mm.json"

with open(filepath, "r") as file:
    data = json.load(file)

entries=0
grades=["A","A-","B","B-","C","C-","E"]
for value in data.values():
    for i in value:
        entries+=1
dat=np.empty((entries,len(value[0])+1),dtype='U50')   # +1 is for the subject

index=0
for key,value in data.items() :
    for i in value:            #each value is the list of students under a given subject (key), for i is each student in the value
        dat[index][0]=key
        dat[index][1]=i['marks_obtained']
        dat[index][2]=i['max_marks']
        dat[index][3]=i['grade_awarded']
        index+=1

columns=np.array(["Subject","marks_obtained","max_marks","grade_awarded"])

df=pd.DataFrame(dat,columns=columns)    # the data is now contained in df


def showData(subject):

    def count(grade):
        return pd.to_numeric(grade["marks_obtained"]).count()
    
    def minMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).min(),2)
    
    def maxMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).max(),2)
    
    subjectData=df[df["Subject"]==subject]

    Agrade=subjectData[subjectData["grade_awarded"]=="A"]
    Amgrade=subjectData[subjectData["grade_awarded"]=="A-"]
    Bgrade=subjectData[subjectData["grade_awarded"]=="B"]
    Bmgrade=subjectData[subjectData["grade_awarded"]=="B-"]
    Cgrade=subjectData[subjectData["grade_awarded"]=="C"]
    Cmgrade=subjectData[subjectData["grade_awarded"]=="C-"]
    Egrade=subjectData[subjectData["grade_awarded"]=="E"]

    totalStudents=(count(Agrade)+count(Amgrade)+count(Bgrade)+count(Bmgrade)+count(Cgrade)+count(Cmgrade)+count(Egrade))

    
    global table 

    table=pd.DataFrame({  
                        "count"  :  pd.Series([count(Agrade),count(Amgrade),count(Bgrade),count(Bmgrade),count(Cgrade),count(Cmgrade),count(Egrade)],index=(grades))
                        ,"min" : pd.Series([minMarks(Agrade),minMarks(Amgrade),minMarks(Bgrade),minMarks(Bmgrade),minMarks(Cgrade),minMarks(Cmgrade),minMarks(Egrade)],index=(grades))
                        ,"max" : pd.Series([maxMarks(Agrade),maxMarks(Amgrade),maxMarks(Bgrade),maxMarks(Bmgrade),maxMarks(Cgrade),maxMarks(Cmgrade),maxMarks(Egrade)],index=(grades))
                        },
    index=(grades))


scam=0

for key in data.keys():
     
    showData(key)

    check=0     # if the scam is done multiple times in the same subject, this will ensure the subject is called out once but does shows all the scams points
    for i in range(5):
        if table.iloc[i,1]<table.iloc[i+1,2]:
            scam+=1
            print()
            if check==0:     
                print(key)
                check=1
            print(f"the min marks of {table.index[i]} grade is lower than the highest marks of {table.index[i+1]} grade")
            print(table.iloc[i:i+2,1:3])
            print()
print(f"{scam} subjects are scam")