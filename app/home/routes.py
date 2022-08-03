from flask import Blueprint, render_template, request, jsonify
from random import randint

home = Blueprint('home', __name__)


@home.route('/home')
@home.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title='Home')


@home.route('/dataset')
def dataset():
    return jsonify({
        "indicator": "eiusmod aute minim enim in",
        "survey_id": "adipisicing laboris nisi sed Excepteur",
        "area_id": "ad voluptate ullamco",
        "sex": "mollit",
        "age_group": "ut",
        "n_clusters": -95041416.62018403,
        "n_observations": -64427538.00610257,
        "estimate": -31275331.865845367,
        "std_error": -29491693.537324786,
        "ci_lower": 23,
        "ci_upper": 23,
        "n_eff_kish": -11426367.100693628,
        "survey_year": 29264554.883909106
    })

