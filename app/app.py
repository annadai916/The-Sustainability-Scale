from flask import *
# from flask_socketio import SocketIO
from money_calculator import *

app = Flask(__name__)
# socketio = SocketIO(app)

net_sum = 0
left_side = 0
right_side = 0

def update_net(left, right):
    global net_sum
    global left_side
    global right_side
    if (left != 0):
        left_side -= int(left)
    if (right != 0):
        right_side += int(right)
    net_sum -= int(left)
    net_sum += int(right)
    scaledValue = ((net_sum / abs(left_side)) * 10)
    print("net: " + str(net_sum))
    print("left: " + str(left_side))
    print("right: " + str(right_side))
    print("scaled: " + str(scaledValue))
    return scaledValue

@app.route('/')
def index():
    global net_sum
    global left_side
    global right_side
    net_sum = 0
    left_side = 0
    right_side = 0
    return render_template('index.html', data=net_sum)

@app.route('/index.html')
def goback():
    return redirect('/')

@app.route('/handle_neg_input', methods=['POST'])
def handle_neg_input():
    cost = request.form['input_cost']
    new_net = update_net(cost, 0)
    return render_template('index.html', data=new_net)

@app.route('/handle_pos_input', methods=['POST'])
def handle_pos_input():
    multiplier = request.form['savings_times']
    base = request.form['savings_type']
    new_net = update_net(0, multiplier)
    return render_template('index.html', data=new_net)

if __name__ == '__main__':
    app.run(debug=True, port=4001)