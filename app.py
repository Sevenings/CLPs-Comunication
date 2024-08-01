from flask import Flask, render_template, jsonify, request
from cozinheiro import ConexaoCLP
import time
app = Flask(__name__)


tag = ConexaoCLP('172.17.85.114', 'B10:2/6')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tag-status')
def tag_status():
    clp_status = {'status': tag.status(), 'tag': tag.read()}
    return jsonify(clp_status)

@app.route('/api/write-tag', method=('POST'))
def write_tag():
    if 'state' not in request.json:
        return jsonify({'error': 'state not found'})
    else:
        state = request.json['state']
        tag.write(state)


if __name__ == '__main__': 
    app.run(debug=True)
