from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    name = request.form['name']
    return render_template('certificate_generated.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
