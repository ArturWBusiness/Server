var myGamePiece;

function startGame() {
	myGameArea.start();
	myGamePiece = new component(30, 30, "red", 10, 120);
}
let t = 0;
function component(width, height, color, x, y) {
	this.width = width;
	this.height = height;
	this.x = x;
	this.y = y;
	this.color = color;
	this.update = function() {
		let i = t/20;
		this.x = Math.cos(Math.random());
		this.y = Math.cos(i);
		ctx = myGameArea.context;
		ctx.fillStyle = this.color;
		ctx.fillRect(this.x*100 + 100, this.y*100 + 100, 5, 5);
		t++;
	}
}

var myGameArea = {
    canvas: document.getElementById("canvas"),
    start: function() {
        this.canvas.width = 300;
        this.canvas.height = 300;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.interval = setInterval(updateGameArea, 16)
    },
    clear: function() {
    	this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

function updateGameArea() {
	//myGameArea.clear();
	myGamePiece.update();
}

startGame()