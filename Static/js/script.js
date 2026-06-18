async function translateText(){

let text =
document.getElementById(
"inputText").value;

let source =
document.getElementById(
"source").value;

let target =
document.getElementById(
"target").value;

const response =
await fetch(
"/translate",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({

text:text,
source:source,
target:target

})
}
);

const data =
await response.json();

document.getElementById(
"outputText"
).value =
data.translated;
}

function copyText(){

let text =
document.getElementById(
"outputText"
);

text.select();

document.execCommand(
"copy"
);

alert(
"Copied Successfully!"
);
}