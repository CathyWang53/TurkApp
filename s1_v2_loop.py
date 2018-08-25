from flask import (
    Blueprint, render_template, request, json
)
import csv
import os

pyint = 1
skipTime = 0
movieNum = 10
count=0

genres = ["Action","Adventure","Animation","Comedy","Crime",
          "Documentary","Drama","Fantasy","Horror","Mystery","Romance",
          "Thriller","War","Western"]

pydata=[[0 for col in range(10)] for row in range(movieNum)]

# Read data from movies.csv
# Data: movie name, poster address and detail info addr
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#    genre for one webpage is randomly chosen from genres
file1Name = THIS_FOLDER + '/moviedata/Genres/%s.csv' % ("Comedy")
#    pydata reads 4 lines randomly from this csv file
with open(file1Name) as file1:
    reader=csv.reader(file1, delimiter=',')
    count=0
    for i,row in enumerate(reader):
        if i == 2 or i == 8 or i == 10 or i == 20:  #here should be random integers
            pydata[count] = row
            count = count + 1
print("This is pydata 0")
print(pydata[0])

    
my_file = THIS_FOLDER + '/static/movies.csv'
pydata1=[[0 for col in range(24)] for row in range(movieNum)]
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        pydata1[count] = row
        count = count + 1




bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>/<int:skipTime>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    return render_template('index_v2_loop.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Movies=pydata1,
                           Count=0
                           )



