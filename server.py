from flask import Flask, render_template, request, jsonify
import word_decision
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        sentence = request.form['sentence']
        if len(sentence) < 1:
            return

        return_word_dicision = ['긍정', [('너', 'NP'), ('는', 'JX'), ('아름답', 'VA'), ('다', 'EFN'), ('.', 'SF')], request.form['sentence']]
        json = {'status': "success", 'data': return_word_dicision, 'message': "true"}
        return jsonify(results=json)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8009)