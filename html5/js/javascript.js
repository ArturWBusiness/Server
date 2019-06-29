var canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var context = canvas.getContext("2d");
window.onkeydown = function (eve) {
    console.log(eve.key);
    return eve.key;
};
function loop() {
    requestAnimationFrame(loop);
}
