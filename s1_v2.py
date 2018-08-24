from flask import (
    Blueprint, render_template, request, json
)
import csv
import os

pyint = 1
skipTime = 0
movieNum = 20

# Read data from movies.csv
# Data: movie name, poster address and detail info addr
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = THIS_FOLDER + '/static/movies.csv'
pydata1=[[0 for col in range(32)] for row in range(movieNum)]
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        pydata1[count] = row
        count = count + 1

print("This is pydata1 3")
print(pydata1[2])



bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>/<int:skipTime>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    return render_template('index_v2_loop.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Movies=pydata1[pyint],
                           Count=0)



