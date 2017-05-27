from flask import Flask, render_template, request, abort
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
query_handler = SourceFileLoader("query_handler", current_file_path + "/data_manager/query_handler.py").load_module()
error_helper = SourceFileLoader("error_helper", current_file_path + "/error_handler/error_helper.py").load_module()

app = Flask(__name__)


@app.route("/")
# @error_helper.error_handler
def index():
    dew = query_handler.select_applicants()
    return render_template("body.html", datas=dew)


@app.errorhandler(AttributeError)
def value_error(e):
    print(e)
    return abort(500)

# @app.route("/applicant/<int:applicant_id>"
# def applicant_data

if __name__ == '__main__':
    app.run(debug=True)