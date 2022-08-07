import os
from flask import Flask, render_template, request, redirect, url_for, jsonify # import Flask in Python
from collections import Counter

app = Flask(__name__,template_folder='templates') # creates an instance of a Flask app

@app.route('/') # home 
def home():
    return render_template('home.html') # input - template

@app.route('/returnjson', methods=['GET', 'POST'])
def returnJSON(): 
    if request.method == 'GET':
        word=request.args.get('word')    
        if(word==word[::-1]):
            # print("The string is a palindrome")
            data = { 
            "name": word, 
            "palindrome": True, 
            "sorted": Counter(word),
            "length": len(word) 
            }
            return jsonify(data) # returning a JSON response            
        else:
            # print("Not a palindrome") 
            data = { 
            "name": word, 
            "palindrome": False 
            }  
            return jsonify(data) # returning a JSON response    
    else:
        return redirect(url_for(home))

# app.run(host='0.0.0.0', port=8000) # starts the web app at port 8000

# if __name__=='__app__':  # Used with flask jinja, pipenv shell for autodetect changes
#     app.run(debug=True)  # Starts the web app at localhost port 5000 (http://127.0.0.1:5000/)

if __name__ == "__main__":   # run app with just:  \path...\$ python app.py
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Code: Tonatiuh Zamarron