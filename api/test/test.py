import flask 
from flask import request, jsonify, render_template 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
        {
            'id': 0,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        {
            'id': 1,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        {
            'id': 2,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        ]
@app.route('/',methods=['GET'])
def home():
    return '''
    <h1> Okay so the plan now is to study it well and proper</h1>
    <h2> dont rush thru things :) </h2>
    <h3> good, stage 1 cleared take your time and solve it one by one </h3>
    '''
@app.route('/api/all',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/',methods=['GET'])
def api_id():
    if 'id' in request.args:
        print(request.args)
        id=int(request.args['id'])
    
    else:
        return render_template("home.html") 
    
    results= []

    for book in books:
        if book['id'] == id:
            results.append(book)
            results.append(request.args)
            results.append(request.remote_addr)
            results.append(request.environ['REMOTE_ADDR'])
    return jsonify(results)
@app.route('/credits/',methods=['GET'])
def api_credits():
    return '''
    <h1>This page is meant to contain the credits information </h1>
    '''

app.run()

        

