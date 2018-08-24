from flask import (
    Blueprint, render_template, request, json
)
import csv
import os

pyint = 1
skipTime = 0
movieNum = 10

# Read data from movies.csv
# Data: movie name, poster address and detail info addr
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = THIS_FOLDER + '/static/movies.csv'
pydata1=[[0 for col in range(24)] for row in range(movieNum)]
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        pydata1[count] = row
        count = count + 1

print("This is pydata1 2")
print(pydata1[2])



bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>/<int:skipTime>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    return render_template('index_v2.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Name1=pydata1[pyint][0],
                           Poster1=pydata1[pyint][1],
                           Detail1=pydata1[pyint][2],
                           Name2=pydata1[pyint][3],
                           Poster2=pydata1[pyint][4],
                           Detail2=pydata1[pyint][5],
                           Name3=pydata1[pyint][6],
                           Poster3=pydata1[pyint][7],
                           Detail3=pydata1[pyint][8],
                           Name4=pydata1[pyint][9],
                           Poster4=pydata1[pyint][10],
                           Detail4=pydata1[pyint][11],
                           Name5=pydata1[pyint][12],
                           Poster5=pydata1[pyint][13],
                           Detail5=pydata1[pyint][14],
                           Name6=pydata1[pyint][15],
                           Poster6=pydata1[pyint][16],
                           Detail6=pydata1[pyint][17],
                           Name7=pydata1[pyint][18],
                           Poster7=pydata1[pyint][19],
                           Detail7=pydata1[pyint][20],
                           Name8=pydata1[pyint][21],
                           Poster8=pydata1[pyint][22],
                           Detail8=pydata1[pyint][23])



