import os
import sys
from pathlib import Path
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    # SERVER_NAME='localhost:5999',
    UPLOAD_FOLDER=os.path.join(app.root_path, 'static', 'upload'),
))

# Custom User Imports
user_paths = [
    Path('{root_path}/static/scripts'.format(root_path=app.root_path))
]
sys.path.extend([str(path.resolve()) for path in user_paths])
import beta_pdf_miner


@app.route('/')
def hello_world():
    print(url_for('static', filename='css/bootstrap.min.css'))
    print(url_for('static', filename='css/bootstrap.min.css', _external=True))
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
