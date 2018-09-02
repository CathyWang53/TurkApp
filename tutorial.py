from flask import (
    Blueprint, render_template, request, json
)
import csv
import os
import random
from random import choice

pyint = 1
skipTime = 0
movieNum = 12
count=0
index=0

queryFiles=["Nike","superhero","summer","JeanShorts","JeanShorts_3rows"]
hideRow2Index = [0,1]
showRow3Index = [4]

pydata=[[0 for col in range(22)] for row in range(movieNum)]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


bp = Blueprint('tutorial', __name__, url_prefix='/tutorial/<int:pyint>/<int:skipTime>', static_url_path = "")

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    index=(pyint+skipTime)%len(queryFiles)
    queryFile = queryFiles[index]
    file1Name = THIS_FOLDER + '/tutorialData/%s.csv' % queryFile
    print("the items are from:")
    print(file1Name)
    with open(file1Name) as file1:
        reader=csv.reader(file1, delimiter=',')
        count=0
        for i,row in enumerate(reader):
            if i != 0:
                pydata[count] = row
                pydata[count][0]= str(count) #change movieId to 0~7
                count = count + 1

    count=0
    for data in pydata:
        print(count)
        print(data)
        print(' ')
        count = count + 1

    return render_template('tutorial.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Items=pydata,
                           QueryTypeNum=len(queryFiles),
                           HideIndex=hideRow2Index,
                           ShowRow3Index=showRow3Index,
                           Count=0)



