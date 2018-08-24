from flask import (
    Blueprint, render_template, request, json
)

pyint = 1
pydata = [{"genre":"Comedy","actor":None,"director": None,
          "region": None,"language":None,"date":None,
          "prefix":None, "postfix":None, "similar":None},
          
          {"genre":"sci-fi","actor":None,"director":"Jack",
          "region": None,"language":None,"date":None,
          "prefix":"good", "postfix":None, "similar":None},
          
          {"genre":None,    "actor":"BP","director": None,
          "region": None,"language":None,"date":"2010",
          "prefix":None, "postfix":None, "similar":None},
          
          {"genre":None,    "actor":None,"director": None,
          "region": "USA","language":"English","date":None,
          "prefix":None, "postfix":"with open endings", "similar":None},
          
          {"genre":None,    "actor":None,"director": None,
          "region": None,"language":None,"date":None,
          "prefix":None, "postfix":None, "similar":"Coco"}]

            # Prefix：sad/interesting/classical/top/popular
            # Postfix：with open endings/plot twists/good acting skill

#json_str = json.dumps(pydata[pyint])
#print(json_str)
print(pydata[1]["genre"])


bp = Blueprint('s1_noJS', __name__, url_prefix='/<int:pyint>')

@bp.route('/', methods=('GET', 'POST'))
def scene1(pyint):
    return render_template('index_noJS.html',
                           Genre=pydata[pyint]["genre"],
                           Actor=pydata[pyint]["actor"],
                           Director=pydata[pyint]["director"],
                           Region=pydata[pyint]["region"],
                           Language=pydata[pyint]["language"],
                           Date=pydata[pyint]["date"],
                           Prefix=pydata[pyint]["prefix"],
                           Postfix=pydata[pyint]["postfix"],
                           Similar=pydata[pyint]["similar"],
                           htmldata=json.dumps(pydata), htmlint=pyint)
