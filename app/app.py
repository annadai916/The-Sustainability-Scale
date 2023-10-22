from flask import *
# from flask_socketio import SocketIO
from money_calculator import *

app = Flask(__name__)
# socketio = SocketIO(app)

net_sum = 0

@app.route('/')
def index():
    return render_template('index.html', data=0)

@app.route('/index.html')
def goback():
    return redirect('/')

""" @socketio.on('calculate')
def handle_calculation(data):
    global money_spent
    cost_difference = data['costDifference']
    money_spent -= cost_difference
    socketio.emit('result', {'result': money_spent}) """

@app.route('/handle_input', methods=['POST'])
def handle_input():
    print("in handle_input")
    cost = request.form['input_cost']
    print(cost)
    return render_template('index.html', data=cost)

if __name__ == '__main__':
    app.run(debug=True, port=4001)