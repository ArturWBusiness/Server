function generateClockOutside() {
	var canvas = <HTMLCanvasElement> document.getElementById('canvas-clock-outside');
	var ctx = canvas.getContext('2d');
	canvas.height = 400;
	canvas.width = 400;
	var x = 200,
	    y = 200,
	    // Radii of the white glow.
	    innerRadius = 100,
	    outerRadius = 200,
	    // Radius of the entire circle.
	    radius = 200;
	var gradient = ctx.createRadialGradient(x, y, innerRadius, x, y, outerRadius);
	gradient.addColorStop(0, 'rgba(100,100,255,1)');
	gradient.addColorStop(1, 'rgba(100,100,255,0)');
	ctx.arc(x, y, radius, 0, 2 * Math.PI);
	ctx.fillStyle = gradient;
	ctx.fill();
	ctx.save();
	ctx.beginPath();
	ctx.arc(x, y, radius-10, 0, 2 * Math.PI);
	ctx.clip();
	ctx.clearRect(0,0,canvas.width, canvas.height)
	ctx.restore();
}
function generateClockInside() {
	var canvas = <HTMLCanvasElement> document.getElementById('canvas-clock-inside');
	var ctx = canvas.getContext('2d');
	canvas.height = 400;
	canvas.width = 400;
	var x = 200,
	    y = 200,
	    // Radii of the white glow.
	    innerRadius = 5,
	    outerRadius = 300,
	    // Radius of the entire circle.
	    radius = 190;
	var gradient = ctx.createRadialGradient(x, y, innerRadius, x, y, outerRadius);
	gradient.addColorStop(0, 'rgba(0,0,0,0)');
	gradient.addColorStop(1, 'rgba(100,100,255,1)');
	ctx.arc(x, y, radius, 0, 2 * Math.PI);
	ctx.fillStyle = gradient;
	ctx.fill();
}
function generateClock(){
	generateClockOutside();
	generateClockInside();
}

var monthNames = [
   "January", "February", "March",
   "April", "May", "June", "July",
   "August", "September", "October",
   "November", "December"
];
setInterval(function() {
	const date = new Date();
	var day = date.getDate();
	var monthIndex = date.getMonth();
	var year = date.getFullYear();
	var hour = date.getHours();
	var minute = date.getMinutes();
	var secondsN = date.getSeconds();
	var seconds = (secondsN<10)?"0"+secondsN.toString():secondsN.toString();
	if(day==1||day==21||day==31){var suffix="st"}
	else if(day==2||day==22||day==32){var suffix="nd"}
	else if(day==3||day==23||day==33){var suffix="rd"}
	else{var suffix = "th";}
	document.getElementById("date").innerHTML=day+suffix+" "+monthNames[monthIndex]+" "+year;
	document.getElementById("seconds").innerHTML= seconds + "s";
	if(hour > 12) {
		hour -= 12
		var fotmatHours = (hour < 10)?"0"+hour:hour;
		var formatMinutes = (minute < 10)?"0"+minute:minute;
		document.getElementsByClassName("time")[0].innerHTML = fotmatHours + ":" + formatMinutes;
		document.getElementsByClassName("zone")[0].innerHTML = "PM";
	} else {
		var fotmatHours = (hour < 10)?"0"+hour:hour;
		var fotmatMinutes = (minute < 10)?"0"+minute:minute;
		document.getElementsByClassName("time")[0].innerHTML =  fotmatHours + ":" + fotmatMinutes;
		document.getElementsByClassName("zone")[0].innerHTML = "AM";
	}
},500)
generateClock();