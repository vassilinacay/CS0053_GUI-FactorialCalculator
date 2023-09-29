/*	CS0053 - Technical 3 Source Code for 1T AY 2023-2024

    Program:        Functions - Recursion
    Programmer(s): 
                    Vassili L. Inacay (L)
                    Katryna Lei V. Martin 
    Section:        AN31
    Start Date:     September 28, 2023
    End Date:       October 2, 2023
*/

function calculateFactorial() {
    const numberInput = document.getElementById('numberInput');
    const resultElement = document.getElementById('result');
    const num = parseInt(numberInput.value);

    // Check if the numberInput by user is a valid number
    if (isNaN(num) || num < 0) {
        resultElement.textContent = 'Please enter a valid number.';
    } else {
        const factorial = calculateRecursiveFactorial(num);
        resultElement.textContent = `Factorial of ${num} is ${factorial}`;
    }
}

// Calculate the factorial of a number recursively
function calculateRecursiveFactorial(n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * calculateRecursiveFactorial(n - 1);
    }
}

document.addEventListener('keydown', (event) => {
    const eventKey = event.key;
    if(eventKey === 'Enter') {
        document.getElementById('calc-btn').click();
    }
})
