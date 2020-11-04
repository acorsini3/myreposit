var user_input = window.prompt("Enter a temperature in celsius :");


function conv(celsius) {
    var farenheit = (celsius *9/5)+32;
    return farenheit;
}

console.log("The equivalet in Farenheit is ");
console.log (conv(user_input));