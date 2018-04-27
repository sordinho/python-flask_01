// script.js included in index.html
//js use c syntax for comments

// alert("Hello world");
//
// alert(3 + 2); //5
// alert("3" + 2); //32
// alert("3" + "2"); //32
//
// //variable declaration and assignment
// var a = "3";
// var b = 2;
//
// alert(a + b); //unknown till run time

function roosterClicked() {
    alert("Ouch!!");
    //change the color of a <p> of the index page
    //worst way to search paragraph
    //var p = document.children[1].children[0].children[2];

    //this one is a better way
    var p = document.getElementById("subtitle");
    p.style = "color: red";

    //jquery will be another way (better) to modify
}