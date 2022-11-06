
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
    //tryall();
    
}

function add2(){
    console.log("hi");
    var num1, num2, num3, num4, num5, sum;
    num1 = parseFloat(document.getElementById("num1").value);
    num2 = parseFloat(document.getElementById("num2").value);
    num3 = parseFloat(document.getElementById("num3").value);
    num4 = parseFloat(document.getElementById("num4").value);
    num5 = parseFloat(document.getElementById("num5").value);
    const model = tf.loadLayersModel('model.json');

    const inp = [[num1, num2, num4, num5, num3]];
    console.log(inp[0]);
    model.then(function (res) {

        const prediction = res.predict(tf.tensor(inp));
        console.log(prediction);
        sum = prediction.arraySync()[0][0];
        console.log(sum);
        document.getElementById("answer").value = Math.round(sum *100)/100;
    });
    
    //tryall();
    
}

function tryall() {
    const model = tf.loadLayersModel('model.json');
    model.then(function (res) {

        const prediction = res.predict([[0, 0, 0, 0, 0]]);
        console.log(prediction);
    });

}



