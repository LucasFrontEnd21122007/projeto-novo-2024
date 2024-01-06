from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

rodizio_data = []

@app.route('/')
def index():
    return render_template('index.html', rodizio_data=rodizio_data)

@app.route('/add_rodizio', methods=['POST'])
def add_rodizio():
    nome = request.form['nome']
    tipo = request.form['tipo']
    data = request.form['data']
    
    rodizio_data.append({'nome': nome, 'tipo': tipo, 'data': data})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)