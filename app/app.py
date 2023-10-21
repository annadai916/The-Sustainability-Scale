from flask import Flask, render_template
from flask_socketio import SocketIO
from money_calculator import *

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('calculate')
def handle_calculation(data):
    global money_spent
    cost_difference = data['costDifference']
    money_spent -= cost_difference
    socketio.emit('result', {'result': money_spent})

if __name__ == '__main__':
    socketio.run(app, debug=True)
