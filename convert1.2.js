//intro
var user_input1 = window.prompt("What do you want to convert ? celsius or CHF ? :");

//choice 1
if(user_input1=="celsius"){
    var user_input2 = window.prompt("Enter a temperature in celsius :");
    function conv(celsius) {
        var farenheit = (celsius *9/5)+32;
        return farenheit;
    }
    console.log("The equivalent in Farenheit is ");
    console.log (conv(user_input2));
}

//choice 2
if(user_input1=="CHF"){
    var user_input2 = window.prompt("Enter an amount in CHF :");
    function conv(CHF) {
        var EUR = (CHF *1.2);
        return EUR;
    }
console.log("The equivalent in EUR is ");
console.log (conv(user_input2));
}