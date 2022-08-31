from flask import Blueprint, render_template, jsonify
from app.auth0.scope import requires_scope
from app.auth0.authorization import requires_auth
from flask_cors import cross_origin
from app.exceptions import AuthError

home = Blueprint('home', __name__)


@home.route('/home')
@home.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html', title='Home')


@home.route('/authorisation/dataset')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def authorisation():
    if requires_scope("read:dataset"):
        return jsonify(dataset={
            "authorized": "datasets",
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

    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)


@home.route('/authenticated/dataset')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def authenticated():
    return jsonify(dataset={
        "authenticated": "datasets"
    })
