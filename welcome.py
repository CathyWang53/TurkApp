from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('welcome', __name__, url_prefix='/welcome')

@bp.route('/', methods=('GET', 'POST'))
def wlcm():
    return render_template('welcome.html')
