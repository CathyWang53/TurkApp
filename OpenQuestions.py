from flask import (
    Blueprint, render_template, request
)

questionNum=1
htmlint=0 #no use at all, only a variable in base.html


bp = Blueprint('OpenQuestions', __name__, url_prefix='/OpenQuestions/<int:questionNum>')

@bp.route('/', methods=('GET', 'POST'))
def OpenQuestions(questionNum):
    return render_template('OpenQuestions.html',
                           questionNum = questionNum,
                           htmlint=htmlint
                           )
