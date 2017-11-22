from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import checkpy
import checkpy.lib
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        print('No selected file')
        return redirect(request.url)

    if file and _allowedFile(file.filename):
        filename = secure_filename(file.filename)
        file.save(_filepath(filename))
        return _testJson(filename, callback = lambda : _removeUpload(filename))

    return file.read()

def _testJson(filename, callback = None):
    filepath = _filepath(filename)
    testerResult = checkpy.test(filepath)
    if not testerResult:
        return jsonify({})

    json = {}
    json["nTests"] = testerResult.nTests
    json["nRunTests"] = testerResult.nRunTests
    json["nFailedTests"] = testerResult.nFailedTests
    json["nPassedTests"] = testerResult.nPassedTests
    json["output"] = testerResult.output

    json["testResults"] = []
    for testResult in testerResult.testResults:
        testResultJson = {}
        testResultJson["description"] = testResult.description
        testResultJson["message"] = testResult.message
        testResultJson["hasPassed"] = testResult.hasPassed
        testResultJson["exception"] = testResult.exception
        json["testResults"].append(testResultJson)

    json["source"] = checkpy.lib.source(filepath)

    if callback:
        callback()

    return jsonify(json)

def _removeUpload(filename):
    os.remove(_filepath(filename))

def _filepath(filename):
    return os.path.join(app.config['UPLOAD_FOLDER'], filename)

def _allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['py']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
