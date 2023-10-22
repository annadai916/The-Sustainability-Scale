from flask import *
# from flask_socketio import SocketIO
from money_calculator import *
from decimal import Decimal

app = Flask(__name__)
# socketio = SocketIO(app)

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
                    {"Num": 0, "Money": 0}
                }


def update_net(left, right):
    global net_sum
    global left_side
    global right_side
    if (left != 0):
        left_side -= Decimal(left)
    if (right != 0):
        right_side += Decimal(right)
    net_sum -= Decimal(left)
    net_sum += Decimal(right)
    return scale()

def scale():
    global net_sum
    global left_side
    global right_side
    scaledValue = 0
    if (net_sum < 0):
        scaledValue = ((net_sum / abs(left_side)) * 10)
    elif (net_sum > 0):
        scaledValue = ((net_sum / abs(right_side)) * 10)
    else:
        if left_side != 0:
            scaledValue = ((net_sum / abs(left_side)) * 10)
        elif right_side != 0:
            scaledValue = ((net_sum / abs(right_side)) * 10)
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
    right_side_dict["walk"] = {"Num": 0, "Money": 0}
    right_side_dict["boba"] = {"Num": 0, "Money": 0}
    right_side_dict["water"] = {"Num": 0, "Money": 0}
    right_side_dict["cook"] = {"Num": 0, "Money": 0}
    return render_template('index.html', data=net_sum, right_side_dict=right_side_dict, total_spent=left_side, total_saved=right_side, net=net_sum)

@app.route('/index.html')
def goback():
    return redirect('/')

@app.route('/handle_neg_input', methods=['POST'])
def handle_neg_input():
    global net_sum
    global left_side
    global right_side
    cost = request.form['input_cost']
    new_net = net_sum
    if cost != "":
        new_net = update_net(cost, 0)
    print(right_side_dict)
    return render_template('index.html', data=new_net, right_side_dict=right_side_dict, total_spent=round(Decimal(str(left_side)), 2), total_saved=round(Decimal(str(right_side)), 2), net=round(Decimal(str(net_sum)), 2))

@app.route('/handle_pos_input', methods=['POST'])
def handle_pos_input():
    global net_sum
    global left_side
    global right_side
    # Get values from form
    new_net = scale()
    multiplier = request.form['savings_times']
    if multiplier != "":
        base = request.form['savings_type']
        base_type = request.form['savings_type']
        # Get money saved for event
        base = get_base_value(base_type)
        total_saved = Decimal(str(float(multiplier) * base))
        new_net = update_net(0, total_saved)
        # Update dictionary
        right_side_dict[base_type]["Num"] += Decimal(multiplier)
        right_side_dict[base_type]["Num"] = round(Decimal(str(right_side_dict[base_type]["Num"])), 2)
        right_side_dict[base_type]["Money"] += Decimal(total_saved)
        right_side_dict[base_type]["Money"] = round(Decimal(str(right_side_dict[base_type]["Money"])), 2)
        # Update right_side value
        # Update net_sum value
        print(right_side_dict)
    return render_template('index.html', data=new_net, right_side_dict=right_side_dict, total_spent=round(Decimal(str(left_side)), 2), total_saved=round(Decimal(str(right_side)), 2), net=round(Decimal(str(net_sum)), 2))

if __name__ == '__main__':
    app.run(debug=True, port=4001)