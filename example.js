
function add(){
    console.log("hi");
    var num1, num2, num3, num4, num5, sum;
    num1 = parseFloat(document.getElementById("firstnumber").value);
    num2 = parseFloat(document.getElementById("secondnumber").value);
    num3 = parseFloat(document.getElementById("thirdnumber").value);
    num4 = parseFloat(document.getElementById("fournumber").value);
    num5 = parseFloat(document.getElementById("fifthnumber").value);
    sum = 8.463 - 0.109*num1-0.048*num2+0.067*num4 - 0.529*num5-0.401*num3;
    document.getElementById("answer").value = Math.round(sum *100)/100;
    tryall();
    
}

function tryall() {
    const model = tf.loadLayersModel('model.json');
    model.then(function (res) {

        const prediction = res.predict([[0, 0, 0, 0, 0]]);
        console.log(prediction);
    });

}



