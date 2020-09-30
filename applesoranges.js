var apples = 11;
var oranges = 7;
var fruits = apples+oranges;
console.log(fruits);

// At this point, eat an apple and store the new
// amount of apples
apples = apples-1;

// Now, we compute the new amount of fruits
fruits = apples+oranges;
console.log(fruits);

// Let's eat an orange too...
oranges = oranges-1;

// ...and one more apple because we are hungry
apples = apples-1;

// We again compute the new amount of fruits
// and display the result
fruits = apples+oranges;
console.log(fruits);
