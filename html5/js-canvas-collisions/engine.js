/**
 * Rotates coordinate system for velocities
 *
 * Takes velocities and alters them as if the coordinate system they're on was rotated
 *
 * @param  Object | velocity | The velocity of an individual particle
 * @param  Float  | angle    | The angle of collision between two objects in radians
 * @return Object | The altered x and y velocities after the coordinate system has been rotated
 */

function rotate(velocity, angle) {
    const rotatedVelocities = {
        x: velocity.x * Math.cos(angle) - velocity.y * Math.sin(angle),
        y: velocity.x * Math.sin(angle) + velocity.y * Math.cos(angle)
    };

    return rotatedVelocities;
}

/**
 * Swaps out two colliding particles' x and y velocities after running through
 * an elastic collision reaction equation
 *
 * @param  Object | particle      | A particle object with x and y coordinates, plus velocity
 * @param  Object | otherParticle | A particle object with x and y coordinates, plus velocity
 * @return Null | Does not return a value
 */

    
function resolveCollision(particle, otherParticle) {
    const xVelocityDiff = particle.velocity.x - otherParticle.velocity.x;
    const yVelocityDiff = particle.velocity.y - otherParticle.velocity.y;

    const xDist = otherParticle.x - particle.x;
    const yDist = otherParticle.y - particle.y;

    // Prevent accidental overlap of particles
    if (xVelocityDiff * xDist + yVelocityDiff * yDist >= 0) {

        // Grab angle between the two colliding particles
        const angle = -Math.atan2(otherParticle.y - particle.y, otherParticle.x - particle.x);

        // Store mass in var for better readability in collision equation
        const m1 = particle.mass;
        const m2 = otherParticle.mass;

        // Velocity before equation
        const u1 = rotate(particle.velocity, angle);
        const u2 = rotate(otherParticle.velocity, angle);

        // Velocity after 1d collision equation
        const v1 = { x: u1.x * (m1 - m2) / (m1 + m2) + u2.x * 2 * m2 / (m1 + m2), y: u1.y };
        const v2 = { x: u2.x * (m1 - m2) / (m1 + m2) + u1.x * 2 * m2 / (m1 + m2), y: u2.y };

        // Final velocity after rotating axis back to original location
        const vFinal1 = rotate(v1, -angle);
        const vFinal2 = rotate(v2, -angle);

        // Swap particle velocities for realistic bounce effect
        particle.velocity.x = vFinal1.x;
        particle.velocity.y = vFinal1.y;

        otherParticle.velocity.x = vFinal2.x;
        otherParticle.velocity.y = vFinal2.y;
    }
}

window.addEventListener("resize", init);
let particles;
let canvas;
let context;
let p;
function resize() {
    canvas = document.getElementById("canvas");
    context = canvas.getContext('2d');
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
    window.onclick = function(eve){
        let p = new particle(eve.clientX, eve.clientY, 20+10*(Math.random()));
        particles.push(p);
    }
}

function distance(x1,y1,x2,y2){
    let a = x1-x2;
    let b = y1-y2;
    
    // a^2 + b^2 = c^2
    return Math.sqrt(a*a + b*b);
}
function init(){
    resize()
    particles = []
    let particleRadius;
    let x;
    let y;
    let isSpawnValid;
    let spawnError = 0;
    for(let i=0;i<500;i++){
        particleRadius = 20+10*(Math.random());
        x=(canvas.width-2*particleRadius)*Math.random()+particleRadius;
        y=(canvas.height-2*particleRadius)*Math.random()+particleRadius;
        isSpawnValid = true;
        for(let j=0;j<particles.length;j++){
            if(particles[j].radius + particleRadius> distance(x,y,particles[j].x,particles[j].y)){
                isSpawnValid = false;
            }
        }
        
        if(spawnError > 100){
            break;
        }
        if(!isSpawnValid){
            spawnError++;
            i--;
            continue;
        }
        spawnError = 0;
        p = new particle(x, y, particleRadius);
        particles.push(p);
    }
}
function particle(x, y, radius){
    this.x = x;
    this.y = y;
    this.velocity = {
        x: (Math.random()-0.5)*5,
        y: (Math.random()-0.5)*5
    };
    this.radius = radius;
    this.mass = 5;
}
particle.prototype.update =  function() {
    
    this.x += this.velocity.x;
    this.y += this.velocity.y;
    if(this.x < this.radius){
        this.x = this.radius;
        this.velocity.x = -this.velocity.x;
    }else if(canvas.width - this.radius < this.x){
        this.x = canvas.width - this.radius;
        this.velocity.x = -this.velocity.x;
    }
    if(this.y < this.radius){
        this.y = this.radius;
        this.velocity.y = -this.velocity.y;
    }else if(canvas.height - this.radius < this.y){
        this.y = canvas.height - this.radius;
        this.velocity.y = -this.velocity.y;
    }
    for(var i=0; i<particles.length;i++){
        if(particles[i] === this){
            continue;
        }
        if(particles[i].radius + this.radius > distance(this.x, this.y, particles[i].x, particles[i].y)){
            resolveCollision(this, particles[i])
        }
    }
    this.draw()
}
particle.prototype.draw = function() {
    context.beginPath();
    context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
    context.fillStyle = 'rgba(67, 224, 188, 0.63)';
    context.fill();
    context.lineWidth = 5;
    context.strokeStyle = 'rgb(46, 84, 155)';
    context.stroke();
}
function animation(){
    context.clearRect(0, 0, canvas.width, canvas.height);
    for(let i=0;i<particles.length;i++){
        particles[i].update()
    }
    requestAnimationFrame(animation);
}

init()
animation()