from crypt import methods
from flask import Flask,render_template,redirect,session,request

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    if session['count'] >= 1:
        session['count'] += 1
        return render_template('index.html',count=session['count'])
    else:
        session['count'] = 1
    return render_template('index.html',count=session['count'])

@app.route('/suma',methods=['POST'])
def suma():
    count = int(request.form['visitas_num'])
    session['count'] += count - 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    
    
# la ruta /destroy_session aqui se llama /reset