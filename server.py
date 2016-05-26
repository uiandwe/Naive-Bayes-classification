from flask import Flask, render_template, request, jsonify
import word_decision
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        sentence = request.form['sentence']
        if len(sentence) < 1:
            return
        morpheme = word_decision.sentence_to_kkma(sentence)
        return_value = word_decision.run_word_decision(morpheme)
        return_word_dicision = [return_value, morpheme, request.form['sentence']]
        json = {'status': "success", 'data': return_word_dicision, 'message': "true"}
        return jsonify(results=json)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8009)