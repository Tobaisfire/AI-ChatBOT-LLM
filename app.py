
from flask import Flask, request, jsonify,render_template,redirect,session
from time import sleep
from LLM import *
app = Flask(__name__)

app.secret_key = 'your_secret_key'
memory = Mem()

@app.route('/',methods= ['POST','GET'])

def id_get():
    name = request.form.get('name')

    if name !=None:
        session['user'] = name
        return redirect('/Chat')
   
    return render_template('id_fecther.html')


@app.route('/Chat')
def home():
    if session['user'] != None:
        
   
        return render_template('UI.html')

    return redirect('/')



@app.route('/get_response', methods=['POST'])
def get_response():
    user = session['user']
    
    data = request.get_json()
    message = data['message']
    

    
    bot_reply = generate_reply(message,user)
    sleep(2)
    response = {
        'reply': bot_reply
    }
    
    return jsonify(response)




def generate_reply(message,user_id):
    chat_history = memory.bot_memory(user_id)

    query = message

    result = qa({"question": str(query),"chat_history":chat_history })

  
    chat_history = [(query, result["answer"])]

    data = {'Id':user_id,'msg_history':chat_history}

    memory.insert_or_update_data(data)
  
    return result["answer"]

