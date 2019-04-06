function sound(src) {
  this.sound = document.createElement("audio");
  this.sound.src = src;
  this.sound.setAttribute("preload", "auto");
  this.sound.setAttribute("controls", "none");
  this.sound.style.display = "none";
  document.body.appendChild(this.sound);
  this.play = function(){
    this.sound.currentTime = 0;
    this.sound.play();
  }
}
const sounds = {
	"0": new sound("-1.mp3"),
	"1": new sound("0.mp3"),
	"2": new sound("1.mp3"),
	"3": new sound("2.mp3"),
	"4": new sound("3.mp3"),
	"5": new sound("4.mp3"),
	"6": new sound("5.mp3"),
	"7": new sound("6.mp3"),
	"8": new sound("7.mp3")
}

function toggle(x, y, boxID){
	var item = document.getElementById(boxID).getElementsByClassName("row")[x].getElementsByClassName("item")[y];
	if(item.innerHTML.includes("false")){
		item.innerHTML = "true"
	} else {
		item.innerHTML = "false"
	}
}
var iteration = 0;
function loop(boxID){
	var rows = document.getElementById(boxID).getElementsByClassName("row");
	for (var i = 0; i < rows[1].length; i++) {
		var items = rows[i].getElementsByClassName("item");
		var item = items[iteration].innerHTML;
		if(item.includes("true")){
			sounds[8-i].play();
		}
	}
	iteration++;
	if(iteration> rows.length-1){iteration=0}
}
function create(y, x, boxID) {
	var box = "<div id='" + boxID + "' class='box'>";
	for(var i=0; i<x;i++){
		var row = "<div class='row'>";
		for(var j=0; j<y;j++){
			var item = "<div class='item' onclick=\"toggle("+i.toString()+", "+j.toString()+", '"+boxID.toString()+"')\">false</div>";
			row += item;
		}
		box += row + "</div>";
	}
	box += "</div>";
	document.write(box);
}
create(16, 8, "box1")
setInterval(loop, 250, "box1")

