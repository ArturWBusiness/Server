/*eslint-env browser*/

var canvas = document.getElementById("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var ctx = canvas.getContext("2d");
var cursorx = -100,
    cursory = -100;
const ParticleFactory = function(){
    this.interval = 100;
    this.lastOutput = Date.now();
    this.particles = [];
    this.y = 0
}

ParticleFactory.prototype.tick = function(){
    if (Date.now() > this.lastOutput + this.interval) {
        const particle = new Particle((canvas.width+100)*Math.random()-50, -50);
        this.particles.push(particle);
        this.lastOutput = Date.now();
    }
    for (var i=0; i < this.particles.length; i++) {
        this.particles[i].tick();
    };
    this.recycle()
}
ParticleFactory.prototype.draw = function(){
    for (var i=0; i < this.particles.length; i++) {
        this.particles[i].draw();
    };
}
ParticleFactory.prototype.recycle = function(){
    this.particles = this.particles.filter(item => item.y < canvas.height + 50);
    this.particles = this.particles.filter(item => item.r > 0.1);
}
const Particle = function(x, y){
    // properties;
    this.max_size = 1;
    this.min_size = 1;
    this.lineDistance = 100;
    this.color = "rgba(200, 200, 200, ";
    this.max_alpha = 1;
    this.min_alpha = 0;
    
    this.max_radius = 4;
    this.min_radius = 1.5;
    
    this.x_offset = -0.5;   // Neg       0       Pos [offset]
    this.x_range = 1.75;    // -1--------0########1- [ 0    ]
                            // -1----####0####----1- [-0.5  ]
    this.min_speed = 0.75;
    this.max_speed = 2.5;
    this.max_slowness = 0.5;
    
    this.x = x;
    this.y = y;
    this.r = Math.random() * (this.max_radius-this.min_radius) + this.min_radius;
    this.dx = (Math.random() + this.x_offset) * this.x_range;
    this.dy = Math.random()* (this.max_speed-this.min_speed) + this.min_speed;
}

Particle.prototype.tick = function(){
    this.x += this.dx;
    this.y += this.dy;
}
Particle.prototype.draw = function(){
    
    // Particle
    ctx.beginPath();
    ctx.arc(Math.floor(this.x), Math.floor(this.y), this.r, 0, 2 * Math.PI, false);
    ctx.fillStyle = "rgba(200, 200, 255, 0.7)";
    ctx.fill();
    ctx.closePath();
    
    this.distanceCursor = Math.sqrt(Math.pow(this.x-cursorx,2) + Math.pow(this.y-cursory,2))
    if (this.distanceCursor < this.lineDistance) {
        // Connection line
        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(cursorx, cursory);
        ctx.lineWidth = (this.max_size-this.min_size) * (1 - this.distanceCursor/this.lineDistance) + this.min_size;
        this.alpha = (((this.max_alpha-this.min_alpha)- this.distanceCursor/this.lineDistance) + (1-this.max_alpha+this.min_alpha));
        ctx.strokeStyle = this.color + this.alpha + ")";
        ctx.stroke();
        ctx.closePath();
        this.x -= this.dx*(this.max_slowness*(1-this.distanceCursor/this.lineDistance));
        this.y -= this.dy*(this.max_slowness*(1-this.distanceCursor/this.lineDistance));
        //this.r -= (1-this.distanceCursor/this.lineDistance)*0.05;
    }
}
// Definitions
let particleFactory = new ParticleFactory;

function draw(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particleFactory.draw();
    
}
function tick(){
    particleFactory.tick();
    
    draw()
    window.requestAnimationFrame(tick)
}
function mouseTrack(event){
    cursorx = event.clientX;
    cursory = event.clientY;
}
document.addEventListener("mousemove", mouseTrack);
document.addEventListener("DOMContentLoaded", function() {
	tick();
});