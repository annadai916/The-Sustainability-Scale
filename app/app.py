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

@app.route('/handle_neg_input', methods=['POST'])
def handle_neg_input():
    global net_sum
    cost = request.form['input_cost']
    net_sum -= int(cost)
    print(net_sum)
    return render_template('index.html', data=net_sum)

@app.route('/handle_pos_input', methods=['POST'])
def handle_pos_input():
    global net_sum
    multiplier = request.form['savings_times']
    base = request.form['savings_type']
    net_sum += int(multiplier)
    print(net_sum)
    return render_template('index.html', data=net_sum)

if __name__ == '__main__':
    app.run(debug=True, port=4001)