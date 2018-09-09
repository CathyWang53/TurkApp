from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('finish', __name__, url_prefix='/finish')

@bp.route('/', methods=('GET', 'POST'))
def wlcm():
    return render_template('finish.html')
