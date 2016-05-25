from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['sentence'])
        json = {'status': "success", 'data': request.form['sentence'], 'message': "true"}
        return jsonify(results=json)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8009)