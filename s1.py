#from flask import (
#    Blueprint, render_template, request, json
#)
#
#pyint = 0
#pydata = [{"genre":"Comedy","actor":"","date":""},
#          {"genre":"","actor":"Jack","date":""},
#          {"actor":"BP","date":"2010","genre":""}]
##json_str = json.dumps(pydata[pyint])
##print(json_str)
#
#
#bp = Blueprint('s1', __name__, url_prefix='/<int:pyint>')
#
#@bp.route('/', methods=('GET', 'POST'))
#def scene1(pyint):
#    return render_template('index.html',GenreName='genre',htmldata=json.dumps(pydata),htmlint=pyint)
