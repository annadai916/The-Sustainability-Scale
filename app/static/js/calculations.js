const socket = io.connect('http://' + document.domain + ':' + location.port);

total_spent = 0;

socket.on('result', function (data) {
    const resultValue = document.getElementById('result-value');
    resultValue.textContent = data.result;
});

document.addEventListener('DOMContentLoaded', function () {
    const calculateButton = document.getElementById('calculate-button');
    const inputCostElement = document.getElementById('input_cost');
    
    calculateButton.addEventListener('click', function (event) {
        event.preventDefault();
        const costDifference = parseFloat(inputCostElement.value);
        
        socket.emit('calculate', { costDifference: costDifference });
    });
});