from flask import Flask, render_template, request
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
query_handler = SourceFileLoader("query_handler", current_file_path + "/server_coonection/query_handler.py").load_module()


app = Flask(__name__)


@app.route("/")
def index():
    dew = query_handler.select_applicants()
    return render_template("body.html", datas=dew)


if __name__ == '__main__':
    app.run(debug=True)