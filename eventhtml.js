// works with indexxx.html

// part 1 change text when clicking the button

// If it has a HTML tag use innerHTML
const title = document.getElementById("title");
// If it has no HTML tag use value
const myButton1 = document.getElementById("myButton1");

function changeTitle() {
    title.innerText = myText1.value;
}
// 1 Event 2 Name of the function
myButton1.addEventListener("click", changeTitle);




// part 2 add paragraph
const content = document.getElementById("content");

function addParagraph() {
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText2.value;
    newParagraph.className = "red";
    content.appendChild(newParagraph);
}

myButton2.addEventListener("click", addParagraph);