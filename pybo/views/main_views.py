#블루프린트 만들기

# from flask import Blueprint, render_template
from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/')
# def index():
    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template('question/question_list.html',question_list=question_list)
    # #'Pybo Index'

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)