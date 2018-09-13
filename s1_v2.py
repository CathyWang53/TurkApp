from flask import (
    Blueprint, render_template, request, json
)
import csv
import os
import random
from random import choice

pyint = 1
skipTime = 0
showIntro = 0 # 1 is showing intro.js; 0 is not showing intro.js
flag=1
movieNum = 12
count=0
index=0

#define
partNum=6

queryFiles=["Leonardo DiCaprio", "Jennifer Lawrence","Hepburn",
            "Alfred Hitchcock", "Miyazaki","Wes",
            "Mexico", "China","India",
            "Comedy","Romance","Disney",
            "Shark","Robot","Female",
            "Old", "JapanAnime&Others", "2018Horror&Others1",
            "2018Horror&Others1","Book",]
hideRow2Index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
showRow3Index = [18]


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:showIntro>/<int:pyint>/<int:skipTime>/')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime,showIntro):
    index=(3*pyint+skipTime)%len(queryFiles)
    queryFile = queryFiles[index]
    file1Name = THIS_FOLDER + '/moviedata/%s.csv' % queryFile
    print("the movies are from:")
    print(file1Name)
    
    pydata=[[0 for col in range(22)] for row in range(movieNum)]
    
    with open(file1Name) as file1:
        reader=csv.reader(file1, delimiter=',')
        count=0
        for i,row in enumerate(reader):
            if i != 0:
                pydata[count] = row
                pydata[count][0]= str(count) #change movieId to 0~7
                pydata[count][1]= str(pydata[count][1])
                count = count + 1

    # delete redundant genres, only keep the first one
    for data in pydata:
        if (data[2] != 0):
            index = data[2].find(',')
            if (index != -1):
                data[2]=data[2][:index]
    
    # delete redundant actors, only keep the first three ones
    for data in pydata:
        index = -1
        if (data[3] != 0):
            index0 = data[3].find(',') #find the first ','
            if (index0 != -1):
                index = index0+1
                data[3] = data[3][:index]+' '+data[3][index:] #insert a ' ' after the ','
                
                index1 = data[3][index:].find(',') #find the second ','
                if (index1 != -1):
                    index=index + index1 +1
                    data[3] = data[3][:index]+' '+data[3][index:] #insert a ' ' after the ','
                    index2 = data[3][index:].find(',') #find the third ','
                    if (index2 != -1):
                        index = index + index2 + 1
                        data[3] = data[3][:index]+' '+data[3][index:] #insert a ' ' after the ','
                data[3]=data[3][:index-1]

    # delete redundant directors, only keep the first 2 ones
    for data in pydata:
        index = -1
        if (data[4] != 0):
            index0 = data[4].find(',') #find the first ','
            if (index0 != -1):
                index = index0+1
                data[4] = data[4][:index]+' '+data[4][index:] #insert a ' ' after the ','
                
                index1 = data[4][index:].find(',') #find the second ','
                if (index1 != -1):
                    index=index + index1 +1
                    data[4] = data[4][:index]+' '+data[4][index:] #insert a ' ' after the ','
                    index2 = data[4][index:].find(',') #find the third ','
                data[4]=data[4][:index-1]


    count=0
    for data in pydata:
        print(count)
        print(data)
        print(' ')
        count = count + 1
    print(type(pydata[0][3]))

    return render_template('index_v2_loop.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           showIntro=showIntro,
                           Flag=flag,
                           Movies1=pydata,
                           QueryTypeNum=len(queryFiles),
                           HideIndex=hideRow2Index,
                           ShowRow3Index=showRow3Index,
                           partNum=partNum,
                           Count=0)



