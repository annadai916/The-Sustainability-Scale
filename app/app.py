from flask import *
# from flask_socketio import SocketIO
from money_calculator import *

app = Flask(__name__)
# socketio = SocketIO(app)

net_sum = 0
left_side = 0
right_side = 0

right_side_dict = {"walk": 
                    {"Num": 0, "Money": round(0, 2)}, 
                   "boba": 
                   {"Num": 0, "Money": round(0, 2)}, 
                   "water": 
                   {"Num": 0, "Money": round(0, 2)},
                    "cook": 
                    {"Num": 0, "Money": round(0, 2)}
                }


def update_net(left, right):
    global net_sum
    global left_side
    global right_side
    if (left != 0):
        left_side -= float(left)
    if (right != 0):
        right_side += float(right)
    net_sum -= float(left)
    net_sum += float(right)
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
    right_side_dict = {"walk": 
                    {"Num": 0, "Money": 0}, 
                   "boba": 
                   {"Num": 0, "Money": 0}, 
                   "water": 
                   {"Num": 0, "Money": 0},
                    "cook": 
                    {"Num": 0, "Money": 0}}
    return render_template('index.html', data=net_sum, right_side_dict=right_side_dict)

@app.route('/index.html')
def goback():
    return redirect('/')

@app.route('/handle_neg_input', methods=['POST'])
def handle_neg_input():
    global net_sum
    cost = request.form['input_cost']
    new_net = net_sum
    if cost != "":
        new_net = update_net(cost, 0)
    return render_template('index.html', data=new_net, right_side_dict=right_side_dict)

@app.route('/handle_pos_input', methods=['POST'])
def handle_pos_input():
    global net_sum
    # Get values from form
    new_net = net_sum
    multiplier = request.form['savings_times']
    base = request.form['savings_type']
    base_type = request.form['savings_type']
    # Get money saved for event
    base = get_base_value(base_type)
    total_saved = float(multiplier) * base
    new_net = update_net(0, total_saved)
    # Update dictionary
    right_side_dict[base_type]["Num"] += int(multiplier)
    right_side_dict[base_type]["Money"] += float(total_saved)
    # Update right_side value
    # Update net_sum value

    return render_template('index.html', data=new_net, right_side_dict=right_side_dict)

if __name__ == '__main__':
    app.run(debug=True, port=4001)