from flask import *
# from flask_socketio import SocketIO
from money_calculator import *

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
                    {"Num": 0, "Money": 0}}

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
    net_sum -= float(cost)
    print(net_sum)
    return render_template('index.html', data=net_sum)

@app.route('/handle_pos_input', methods=['POST'])
def handle_pos_input():
    global net_sum, right_side, right_side_dict
    # Get values from form
    multiplier = request.form['savings_times']
    base_type = request.form['savings_type']
    # Get money saved for event
    base = get_base_value(base_type)
    total_saved = float(multiplier) * base
    # Update dictionary
    right_side_dict[base_type]["Num"] += base
    right_side_dict[base_type]["Money"] += total_saved
    # Update right_side value
    right_side += total_saved
    # Update net_sum value
    net_sum += right_side
    print(net_sum)
    return render_template('index.html', data=net_sum, right_side_dict=right_side_dict)

if __name__ == '__main__':
    app.run(debug=True, port=4001)