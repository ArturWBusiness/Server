const canvas = < HTMLCanvasElement > document.getElementById("canvas");
canvas.width = 500;
canvas.height = 300;
let context = canvas.getContext("2d");

window.onkeydown = function (eve) {
    if (eve.key === "a") {

    } else if (eve.key === "s") {

    } else if (eve.key === "d") {

    } else if (eve.key === "w") {

    }
}
window.onkeyup = function (eve) {
    if (eve.key === "a") {

    } else if (eve.key === "s") {

    } else if (eve.key === "d") {

    } else if (eve.key === "w") {

    }
}

class Player {
    constructor(x: number, y: number) {
        let s = x
    }
    draw(){

    }
}

const player = new Player(10, 10);

function loop() {


    requestAnimationFrame(loop)
}