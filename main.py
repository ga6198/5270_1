from flask import Flask, render_template, request, jsonify
from encrypt import encrypt
from decrypt import decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toenc')
def toenc():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def enc():
    text = request.form['encode_text']
    key = request.form['encode_key']

    if text == "":
        return "Please provide plaintext."

    if key == "":
        return "Please provide a key."

    ciphertext = encrypt(text, key)

    return render_template('result.html', data = ciphertext)

    return """
<body>
Plaintext: %s <br>
Key: %s <br>
Ciphertext: %s <br>
<a href='/'>Back Home</a>
</body>
""" % (text, key, ciphertext)

@app.route('/todec')
def todec():
    return render_template('decode.html')

@app.route('/decrypt', methods=['POST'])
def dec():
    ciphertext = request.form['decode_text']
    key = request.form['decode_key']

    plaintext = decrypt(ciphertext, key)

    return render_template('result.html', data = plaintext)

if __name__ == "__main__":
    app.run()
