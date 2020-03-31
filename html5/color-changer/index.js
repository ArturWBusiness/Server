let rgb = [0,0,0];
let rgb_r = [false,false,false]
const color = (r,g,b) => {
    document.getElementById("box").style.backgroundColor = "rgb("+r+","+g+","+b+")";
    document.getElementById("box").innerHTML = r+" "+g+" "+b;
}

/* Scroller */
setInterval(() => {
    ["red","green","blue"].forEach(element => {
        document.getElementById(element+"_").innerHTML = document.getElementById(element).value
    });
    let box=document.getElementById("box");
    if(rgb[0]+rgb[1]+rgb[2]>200){box.style.color="black"}
    else{box.style.color="white"}
}, 10);

/* Draw */
setInterval(() => {
    color(rgb[0],rgb[1],rgb[2])
}, 100);

/* Logic */
setInterval(() => {
    [["red",0],["green",1],["blue",2]].forEach(list => {
        let i=list[1];
        let acc = parseInt(document.getElementById(list[0]).value);
        if(rgb_r[i]){
            if(rgb[i]-acc<0||rgb[i]+acc>255){rgb[i]+=acc;rgb_r[i]=false}
            else(rgb[i]-=acc)
        }else{
            if(rgb[i]+acc>255||rgb[i]+acc<0){rgb[i]-=acc;rgb_r[i]=true}
            else(rgb[i]+=acc)
        }
    });
}, 100);
[1,2,3].forEach(i => {
    console.log(i)
});