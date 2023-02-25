# Flask imports
from flask import Flask
from flask import request
from flask import jsonify

# Module Imports
from modules.nlp import predText

app = Flask(__name__)

inputText = []

@app.route('/getInstructions', methods=['GET', 'POST'])
def process1():
    
    '''
    /getInstructions?text=xxxx - to be sent from client side
    '''

    # Process the POST data - retrieve the user's instructions
    raw_data = request.args.get('text')
    print(raw_data)
    inputText.append(raw_data)
    print(type(predText(inputText)))
    
    return(predText(inputText)) 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")