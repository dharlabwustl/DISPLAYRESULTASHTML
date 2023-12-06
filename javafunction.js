
var img = document.createElement("img");
var img1 = document.createElement("img");
var img2 = document.createElement("img");
var img3 = document.createElement("img");
var img4 = document.createElement("img");
var div = document.createElement("div");
div.className = "parent"
var div1 = document.createElement("div") //figure");
// var figcaption1=document.createElement("figcaption");
// var t = document.createTextNode("Fig.1 - A view of the pulpit rock in Norway.");
// figcaption1.appendChild(t);
// div1.appendChild(figcaption1)
var div2 = document.createElement("div") //figure");
var div3 = document.createElement("div") //figure");
var div4 = document.createElement("div") //figure");
var div5 = document.createElement("div") //figure");
// document.body.appendChild(div)
// div.appendChild(div1);
// div.appendChild(div2);
// div.appendChild(div3);
// div.appendChild(div4);
var firstRow0=document.getElementById("row1_col_0")
var firstRow1=document.getElementById("row1_col_1")
var firstRow2=document.getElementById("row1_col_2")
var firstRow3=document.getElementById("row1_col_3")
var firstRow4=document.getElementById("row1_col_4")
firstRow0.appendChild(div1);
firstRow1.appendChild(div2);
firstRow2.appendChild(div3);
firstRow3.appendChild(div4);
firstRow4.appendChild(div5);
function displayImage(src, src1,src2,src3,src4, width, height) {
img.src = src;
img.width = width;
img.height = height;
// img.title = "GRAYSCALE";
img.style="transform:rotate(270deg)";

div1.appendChild(img);
img1.src = src1;
img1.width = width;
img1.height = height;
// img1.title = "CSF";
img1.style="transform:rotate(270deg)";
div2.appendChild(img1);
img2.src = src2;
img2.width = width;
img2.height = height;
// img2.title = "CSF COMPARTMENT";
img2.style="transform:rotate(270deg)";
div3.appendChild(img2);
img3.src = src3;
img3.width = width;
img3.height = height;
// img3.title="SAH COMPARTMENT"
img3.style="transform:rotate(270deg)";
div4.appendChild(img3);
img4.src = src4;
img4.width = width;
img4.height = height;
// img3.title="SAH COMPARTMENT"
img4.style="transform:rotate(270deg)";
div5.appendChild(img4);
}

// var array= new Array();
// var array1= new Array();
// var array2= new Array();
// var array3= new Array();
