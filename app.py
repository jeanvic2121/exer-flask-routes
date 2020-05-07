from flask import Flask, render_template

app = Flask(__name__)

produtos = [['Refrigerante', 4.50], ['Pizza', 2.50],
    ['suco', 24.90], ['Salgado', 5.50], ['lanche', 18.50]]
    
@app.route('/')

def index():
    return render_template('index.html',
    produtos = produtos )

@app.route('/info/<int:id>')

def pokemon(id):
    info = produtos[id]
    return render_template('info.html', produtos = info)

if __name__ == '__main__':
    app.run()