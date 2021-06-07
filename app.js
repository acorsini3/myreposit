// works with Appindex.html

const addButton = document.getElementById("addButton");
addButton.className = "addButton";

const removeButton = document.getElementById("removeButton");
removeButton.className = "removeButton";

const clearButton = document.getElementById("clearButton");
clearButton.className = "clearButton";

const title = document.getElementById("title");
title.className = "appStyle";

const content = document.getElementById("content");
content.className = "appStyle";

const myText = document.getElementById("myText");
const p = document.getElementById("p");



// add an element
function addParagraph() {
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    content.appendChild(newParagraph);
    newParagraph.className = "newElement";

    //store the element in the local storage
    const paragraphs = document.getElementsByClassName("newElement");
    count = paragraphs.length;
    console.log(paragraphs.length);
    localStorage.setItem(count, myText.value);

}
addButton.addEventListener("click", addParagraph);


//remove the last element from the list AND in local storage

function removeParagraph() {
    const paragraphs = document.getElementsByClassName("newElement");

    if (paragraphs.length > 0) {
        const last = paragraphs.length - 1;
        content.removeChild(paragraphs[last]);
        console.log(paragraphs.length);
        localStorage.removeItem(last + 1);
    }

}
removeButton.addEventListener("click", removeParagraph);

// clear all

function clearAll() {
    const paragraphs = document.getElementsByClassName("newElement");

    while (paragraphs.length > 0) {
        const last = paragraphs.length - 1;
        content.removeChild(paragraphs[last]);
        localStorage.clear();
    }
}
clearButton.addEventListener("click", clearAll);