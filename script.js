//Take user input of a string of text
let selection = prompt("Rock, Paper, or Scissors? Press R for Rock, P for Paper, or S for Scissors (case sensitive)");
//verify user selection

const yourSelection = function () {
console.log("You have selected",selection)
}
//Ensure user has selected a correct character
if (selection=="R"){
    yourSelection();
}

else if (selection=="P"){
    yourSelection();
}

else if (selection=="S"){
    yourSelection();
}

else {
    console.log("Invalid Selection... please refresh page and try again...")
}


//Declare a global variable and then use the built in math function to assign it a random number between 1-3 by declaring 2 (which offers three values of 0, 1, 2) in order to correlate with our choices: R, P, or S
let cpu = Math.floor(Math.random() * 2)
console.log (cpu)
if (cpu==0){
    console.log("Computer has selected Rock")
}
else if (cpu==1){
    console.log("Computer has selected Paper")
}
else if (cpu==2){
    console.log("Computer has selected Scissors")
}
//Show end-user random number for debugging and testing purposes, remove or comment out when finished
function getRandomInt(max) {
    return ;
  }

  
//compare CPU integer against user inputted letter and evaluate who has won via three top level nested If Statements 
if (cpu==0){
    if (selection=="R"){
    console.log("Tied! Refresh and try again...")
    }
    else if (selection=="P"){
        console.log("You're Winner! Refresh and try again...")
    }
    else if (selection=="S"){
        console.log("You lose... Refresh and try again...")
    }
    else {
        console.log ("Error")
    }
}
else if (cpu==1){
    if (selection=="R"){
    console.log("You lose... Refresh and try again...")
    }
    else if (selection=="P"){
        console.log("Tied! Refresh and try again...")
    }
    else if (selection=="S"){
        console.log("You're Winner! Refresh and try again...")
    }
    else {
        console.log ("Error")
    }
}
else if (cpu==2){
    if (selection=="R"){
    console.log("You're Winner! Refresh and try again...")
    }
    else if (selection=="P"){
        console.log("You lose... Refresh and try again...")
    }
    else if (selection=="S"){
        console.log("Tied! Refresh and try again...")
    }
    else {
        console.log ("Error")
    }
}
else {
     console.log ("Error")
}