//Maximum number of attempts
let maxAttempts = 3;
//Current number of attempts
let attempts = 0;
//Generate a random number between 0 and 9
let finalNumber = Math.floor(Math.random() * 10);
//DOM = Document Object Model
let inputField = document.getElementById("userNumber");
let btnConfirm = document.getElementById("guessButton");
let messageArea = document.getElementById("result");

//Add event listener to the button
btnConfirm.addEventListener("click", function() {
    //Get the user's input and convert it to a number
    let userNumber = parseInt(inputField.value);

    //Check if the input is a valid number
    if (isNaN(userNumber) || userNumber < 0 || userNumber > 9) {
        messageArea.textContent = "Please enter a valid number between 0 and 9.";
        return;
    }

    attempts++;

    if (userNumber === finalNumber) {
        messageArea.textContent = `Congratulations! You guessed the number in ${attempts} attempt${attempts > 1 ? "s" : ""}.`;
        btnConfirm.disabled = true;
        inputField.disabled = true;
        return;
    }

    if (attempts >= maxAttempts) {
        messageArea.textContent = `Sorry, you've run out of attempts. The correct number was ${finalNumber}.`;
        btnConfirm.disabled = true;
        inputField.disabled = true;
        return;
    }

    let hint = userNumber < finalNumber ? "too low" : "too high";
    messageArea.textContent = `Your guess is ${hint}. Attempts left: ${maxAttempts - attempts}.`;
});
