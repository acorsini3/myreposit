function greet (gender) {
    if (gender == "male") {
    return "Welcome Sir !";
    } else if (gender == "female") {
    return "Welcome Miss !";
    } else {
    return "Welcome !";
    }
}

// From this line we are testing
console.log(greet("male"));
console.log(greet("female"));
console.log(greet("dog"));