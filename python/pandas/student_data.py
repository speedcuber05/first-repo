import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

entries=0    #total number of students
grades=["A","A-","B","B-","C","C-","E"]
colors=['#1aff00','#40d507','#66aa0E','#8d8016','#b3551d','#d92b24','#ff002b']


filepath = r"C:\Users\devan\OneDrive\Documents\programming\first-repo\subjects_data_mm.json"

with open(filepath, "r") as file:
    data = json.load(file)


for value in data.values():
    for i in value:
        entries+=1


dataArr=np.empty((entries,len(value[0])+1),dtype='U50')   # dat is an array which would contain all students along with their subject
index=0
for key,value in data.items() :
    for i in value:            #each value is the list of students under a given subject (key), for i is each student in the value
        dataArr[index][0]=key
        dataArr[index][1]=i['marks_obtained']
        dataArr[index][2]=i['max_marks']
        dataArr[index][3]=i['grade_awarded']
        index+=1
    print(key)

columns=np.array(["Subject","marks_obtained","max_marks","grade_awarded"])

df=pd.DataFrame(dataArr,columns=columns)    # the data is now contained in df


def showData(subject):

    def count(grade):
        return pd.to_numeric(grade["marks_obtained"]).count()
    
    def minMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).min(),2)
    
    def maxMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).max(),2)
    
    def meanMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).mean(),2)
    
    def medianMarks(grade):
        return round(pd.to_numeric(grade["marks_obtained"]).median(),2)
    
    def modeMarks(grade):
        if count(grade)==0:
             pass
        else:
            return round(pd.to_numeric(grade["marks_obtained"]).mode()[0],2)
    
    def percent(grade):
        return round(count(grade)/totalStudents * 100,2) 


             
    
    global subjectData
    subjectData=df[df["Subject"]==subject]

    Agrade=subjectData[subjectData["grade_awarded"]=="A"]
    Amgrade=subjectData[subjectData["grade_awarded"]=="A-"]
    Bgrade=subjectData[subjectData["grade_awarded"]=="B"]
    Bmgrade=subjectData[subjectData["grade_awarded"]=="B-"]
    Cgrade=subjectData[subjectData["grade_awarded"]=="C"]
    Cmgrade=subjectData[subjectData["grade_awarded"]=="C-"]
    Egrade=subjectData[subjectData["grade_awarded"]=="E"]

    totalStudents=count(subjectData) - 1     #1st row is the name of the columns
    print(totalStudents)

    if totalStudents==0:
         print(f"0 students in {subject}")
    else:

        global table 
        tableData={  
            "count"  :  pd.Series([count(Agrade),count(Amgrade),count(Bgrade),count(Bmgrade),count(Cgrade),count(Cmgrade),count(Egrade)],index=(grades))
            ,"min" : pd.Series([minMarks(Agrade),minMarks(Amgrade),minMarks(Bgrade),minMarks(Bmgrade),minMarks(Cgrade),minMarks(Cmgrade),minMarks(Egrade)],index=(grades))
            ,"max" : pd.Series([maxMarks(Agrade),maxMarks(Amgrade),maxMarks(Bgrade),maxMarks(Bmgrade),maxMarks(Cgrade),maxMarks(Cmgrade),maxMarks(Egrade)],index=(grades))
            ,"mean"  :  pd.Series([meanMarks(Agrade),meanMarks(Amgrade),meanMarks(Bgrade),meanMarks(Bmgrade),meanMarks(Cgrade),meanMarks(Cmgrade),meanMarks(Egrade)],index=(grades))
            ,"median" : pd.Series([medianMarks(Agrade),medianMarks(Amgrade),medianMarks(Bgrade),medianMarks(Bmgrade),medianMarks(Cgrade),medianMarks(Cmgrade),medianMarks(Egrade)],index=(grades))
            ,"mode"  :  pd.Series([modeMarks(Agrade),modeMarks(Amgrade),modeMarks(Bgrade),modeMarks(Bmgrade),modeMarks(Cgrade),modeMarks(Cmgrade),modeMarks(Egrade)],index=(grades))   
            ,"probability" :  pd.Series([percent(Agrade),percent(Amgrade),percent(Bgrade),percent(Bmgrade),percent(Cgrade),percent(Cmgrade),percent(Egrade)],index=(grades)) 

        }

        table=pd.DataFrame(tableData,index=(grades))
        
        print(subject)
        print(table)

        Agrade["marks_obtained"].index=np.arange(count(Agrade))
        Amgrade["marks_obtained"].index=np.arange(count(Amgrade))
        Bgrade["marks_obtained"].index=np.arange(count(Bgrade))
        Bmgrade["marks_obtained"].index=np.arange(count(Bmgrade))
        Cgrade["marks_obtained"].index=np.arange(count(Cgrade))
        Cmgrade["marks_obtained"].index=np.arange(count(Cmgrade))
        Egrade["marks_obtained"].index=np.arange(count(Egrade))

        fig,ax=plt.subplots(1,2,figsize=(10,8))
        bar=ax[0].bar(grades,tableData['probability'],color=colors,edgecolor='black')    
        ax[0].bar_label(bar,tableData['probability'])

        gradeData=[np.array(pd.to_numeric(Agrade["marks_obtained"])),
                   np.array(pd.to_numeric(Amgrade["marks_obtained"])),
                     np.array(pd.to_numeric(Bgrade["marks_obtained"])),
                    np.array(pd.to_numeric(Bmgrade["marks_obtained"])),
                     np.array(pd.to_numeric(Cgrade["marks_obtained"])),
                    np.array(pd.to_numeric(Cmgrade["marks_obtained"])),
                    np.array(pd.to_numeric(Egrade["marks_obtained"])),
        
        ]
        
        ax[1].boxplot(gradeData,tick_labels=grades,meanline=True,showmeans=True )
        fig.suptitle(f"{subject}")
        plt.show()

showData("PHYSICS")