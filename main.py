import warnings
warnings.filterwarnings("ignore")
import os
from flask import Flask,request,jsonify
from question import get_llm_response


app = Flask(__name__)

@app.route('/askquery', methods=["POST"])
def ask():
    query = request.json['query']
    answer=get_llm_response(str(query))
    print(answer)
    return jsonify(answer)



if __name__ == '__main__':
	app.run()
