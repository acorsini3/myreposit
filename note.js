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



// add an element in the local storage then display it on the screen
function addParagraph() {
    const paragraphs = document.getElementsByClassName("newElement");
    const count = paragraphs.length + 1;
    console.log(count);

    const data = myText.value;
    console.log(data);
    data.classeName = "newElement";

    localStorage.setItem(count, data);

    location.reload();

}
addButton.addEventListener("click", addParagraph);