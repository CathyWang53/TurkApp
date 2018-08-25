from flask import (
    Blueprint, render_template, request, json
)
import csv
import os
import random

pyint = 1
skipTime = 0
movieNum = 20
count=0
index=0
index1=0
genreNum=13
movieNumEachcsv=100

queryType=3; #define

genres = ["Action","Adventure","Animation","Comedy","Crime",
          "Documentary","Drama","Fantasy","Horror","Mystery","Romance",
          "Thriller","War","Western"]

actors =  ["Robert Downey Jr.", "Leonardo DiCaprio", "Tom Cruise", "Johnny Depp", "George Clooney", "Steve Carell", "Meryl Streep", "Mark Wahlberg", "Brad Pitt", "Jennifer Lawrence", "Will Smith"]

releaseDate = ["after2015","before2000"]

moviedata=[genres,actors,releaseDate]

pydata=[[0 for col in range(10)] for row in range(movieNum)]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))



# Read data from movies.csv
# Data: movie name, poster address and detail info addr
my_file = THIS_FOLDER + '/static/movies.csv'
pydata1=[[0 for col in range(32)] for row in range(movieNum)]
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        pydata1[count] = row
        count = count + 1

#print("This is pydata1 3")
#print(pydata1[2])



bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>/<int:skipTime>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    
    #    genres for one webpage are randomly chosen from genres
    indexes = random.sample([i for i in range(genreNum-1)],5)
    #print(index)

    #choose first genre:"You want movies like these"
    file1Name = THIS_FOLDER + '/moviedata/Genres/%s.csv' % (genres[indexes[0]])
    #print(file1Name)
    #pydata reads 4 lines randomly from this csv file
    with open(file1Name) as file1:
        reader=csv.reader(file1, delimiter=',')
        count=0
        indexes1 = random.sample([i for i in range(movieNumEachcsv-1)],4)
        for i,row in enumerate(reader):
            if i in indexes1:
                pydata[count] = row
                pydata[count][0]= str(count) #change movieId to 0~7
                count = count + 1
    #print("This is pydata 0")
    #print(pydata[0])

    for index in indexes[1:5]: #1~4 randomly choose another 4 genres: "rather than these movies:"
        file1Name = THIS_FOLDER + '/moviedata/Genres/%s.csv' % (genres[index])
        #    print(genres[index])
        #    pydata reads 1 line randomly from this csv file
        with open(file1Name) as file1:
            reader=csv.reader(file1, delimiter=',')
            index1 = random.randint(0,movieNumEachcsv-1)
            for i,row in enumerate(reader):
                if i == 2 :  #here should be a random integer
                    pydata[count] = row
                    pydata[count][0]= str(count) #change movieId to 0~7
                    count = count + 1
    print("This is pydata 7")
    print(pydata[7][1])
    
    return render_template('index_v2_loop.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Movies=pydata1[pyint],
                           Movies1=pydata,
                           Count=0)



