from flask import (
    Blueprint, render_template, request, json
)
import csv
import os
import random
from random import choice

pyint = 1
skipTime = 0
movieNum = 8
movieNum1=20
count=0
index=0
index1=0
genreNum=13
movieNumEachcsv=100
eleNumEachQeury=0

queryTypeNum=3; #define

Genres = ["Action","Adventure","Animation","Comedy","Crime",
          "Documentary","Drama","Fantasy","Horror","Mystery","Romance",
          "Thriller","War","Western"]

Actors =  ["Robert Downey Jr.", "Leonardo DiCaprio", "Tom Cruise", "Johnny Depp", "George Clooney", "Steve Carell", "Meryl Streep", "Mark Wahlberg", "Brad Pitt", "Jennifer Lawrence", "Will Smith"]

ReleaseDate = ["after2015","before2000","in2017","in2018"]

queryTypes=[Genres,Actors,ReleaseDate]

pydata=[[0 for col in range(10)] for row in range(movieNum)]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Read data from movies.csv
# Data: movie name, poster address and detail info addr
my_file = THIS_FOLDER + '/static/movies.csv'
pydata1=[[0 for col in range(32)] for row in range(movieNum1)]
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in csv_reader:
        pydata1[count] = row
        count = count + 1





bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>/<int:skipTime>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint,skipTime):
    
    queryType = choice(queryTypes) #choose queryType randomly
    print("query type: ")
    print(queryType)
    print(' ')
    
    #queryType = ReleaseDate
    if queryType == Genres or queryType == Actors:
        eleNumEachQeury=len(queryType)
        #    randomly chosen from all elements
        #indexes = random.sample([i for i in range(eleNumEachQeury-1)],5)
        elements = random.sample(queryType,5)

        #choose first genre/actor:"You want movies like these"
        file1Name = THIS_FOLDER + '/moviedata/GenresOrActors/%s.csv' % (elements[0])
        print("the first row of mvies are from:")
        print(elements[0])
        print(' ')
        #pydata reads 4 lines randomly from this csv file
        movieNumEachcsv = len(open(file1Name).readlines())-1
        with open(file1Name) as file1:
            reader=csv.reader(file1, delimiter=',')
            count=0
            indexes1 = random.sample([i for i in range(1, movieNumEachcsv)],4)

            for i,row in enumerate(reader):
                if i in indexes1:
                    pydata[count] = row
                    pydata[count][0]= str(count) #change movieId to 0~7
                    count = count + 1
               
        print("the second row of mvies are from:")
        for element in elements[1:5]: #1~4 randomly choose another 4 Genres: "rather than these movies:"
            file1Name = THIS_FOLDER + '/moviedata/GenresOrActors/%s.csv' % (element)
            print(element)
            #    pydata reads 1 line randomly from this csv file
            movieNumEachcsv = len(open(file1Name).readlines())-1
            with open(file1Name) as file1:
                reader=csv.reader(file1, delimiter=',')
                index1 = random.randint(1,movieNumEachcsv)
                for i,row in enumerate(reader):
                    if i == index1 :  #here should be a random integer
                        pydata[count] = row
                        pydata[count][0]= str(count) #change movieId to 0~7
                        count = count + 1


    if queryType == ReleaseDate:
        element = choice(ReleaseDate)
        # the first row of movies
        file1Name = THIS_FOLDER + '/moviedata/ReleaseDate/%s.csv' % (element)
        print("the first row of mvies are from:")
        print(element)
        #pydata reads 4 lines randomly from this csv file
        movieNumEachcsv = len(open(file1Name).readlines())-1
        with open(file1Name) as file1:
            reader=csv.reader(file1, delimiter=',')
            count=0
            indexes1 = random.sample([i for i in range(1, movieNumEachcsv)],4)
            
            for i,row in enumerate(reader):
                if i in indexes1:
                    pydata[count] = row
                    pydata[count][0]= str(count) #change movieId to 0~7
                    count = count + 1
        # the second row of movies
        if (element == "after2015"):
            element = 'before2000'
            file1Name = THIS_FOLDER + '/moviedata/ReleaseDate/before2000.csv'
        if (element == "before2000"):
            element = 'after2015'
            file1Name = THIS_FOLDER + '/moviedata/ReleaseDate/after2015.csv'
        if (element == "in2017"):
            element = 'notIn2017'
            file1Name = THIS_FOLDER + '/moviedata/ReleaseDate/notIn2017.csv'
        if (element == "in2018"):
            element = 'before2018'
            file1Name = THIS_FOLDER + '/moviedata/ReleaseDate/before2018.csv'
            #    pydata reads 4 lines randomly from this csv file
        movieNumEachcsv = len(open(file1Name).readlines())-1
        print("the second row of mvies are from:")
        print(element)
        with open(file1Name) as file1:
            reader=csv.reader(file1, delimiter=',')
            indexes1 = random.sample([i for i in range(1, movieNumEachcsv)],4)
            for i,row in enumerate(reader):
                if i in indexes1 :
                    pydata[count] = row
                    pydata[count][0]= str(count) #change movieId to 0~7
                    count = count + 1
    
    # delete redundant actors and genres

    # delete redundant genres, only keep the first one
    for data in pydata:
        index = data[2].find(',')
        if (index != -1):
            data[2]=data[2][:index]

    # delete redundant actors, only keep the first three ones
    for data in pydata:
        index = -1
        index0 = data[3].find(',') #find the first ','
        if (index0 != -1):
            index=index0
            index1 = data[3][index+1:].find(',') #find the second ','
            if (index1 != -1):
                index=index + index1 + 1
                index2 = data[3][index+1:].find(',') #find the third ','
                if (index2 != -1):
                    index = index + index2 + 1
            data[3]=data[3][:index]

    count=0
    for data in pydata:
        print(count)
        print(data)
        print(' ')
        count = count + 1

    return render_template('index_v2_loop.html',
                           htmlint=pyint,
                           SkipTime=skipTime,
                           Movies=pydata1[pyint],
                           Movies1=pydata,
                           Count=0)



