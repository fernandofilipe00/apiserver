from flask import Flask, request, jsonify
from scan_script import scan_files

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    directory = data.get('directory')
    if directory:
        files = scan_files(directory)
        return jsonify(files)
    else:
        return jsonify({"error": "No directory provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
