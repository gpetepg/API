from flask import (
    Blueprint,
    render_template,
    flash,
    request,
    redirect,
    url_for,
)
from flask_restplus import Api
from werkzeug.utils import secure_filename
from flask_rest_psql_docker.database.database_funcs import insert_csv_to_db
import os
import pandas as pd
from sqlalchemy import exc


blueprint = Blueprint('website', __name__, template_folder='templates')
api = Api(blueprint)


ALLOWED_EXTENSIONS = {
    'txt',
    'csv',
}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(url_for(
                'website.failed_file')
            )
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(url_for(
                'website.failed_file')
            )
            return redirect(request.url)
        if not allowed_file(file.filename):
            return redirect(url_for(
                'website.failed_file')
            )
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.environ.get('WEBSITE_UPLOADS'), filename))
            try:
                insert_csv_to_db(
                    # 'postgresql+psycopg2://localhost/tylerguo'
                    'postgresql+psycopg2://test:password@postgres:5432/testdb',
                    pd.read_csv(os.path.join(os.environ.get('WEBSITE_UPLOADS'), filename)),
                    table="people",
                )
                return redirect(url_for(
                    'website.uploaded_file',
                    filename=filename)
                )
            except (exc.IntegrityError, FileNotFoundError) as e:
                return redirect(url_for(
                    'website.failed_file')
                )
    return render_template('input.html')


@blueprint.route('/uploaded_file')
def uploaded_file():
    return render_template('success.html')


@blueprint.route('/failed_file')
def failed_file():
    return render_template('failed.html')
