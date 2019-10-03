//Задание 3
var a = prompt("Введите число a");
var b = prompt("Введите число b");
if (a >= 0 && b >= 0)
    console.log("a - b = "+ (a - b));
else if (a < 0 && b < 0)
    console.log("a * b = " + (a * b));

else
    console.log("a - b = "+ (a + b));


//Задание 4

var z = prompt("Введите число от 1 до 15")
switch(z){
    case "1":
    console.log("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "2":
    console.log("2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "3":
    console.log("3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "4":
    console.log("4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "5":
    console.log("5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "6":
    console.log("6, 7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "7":
    console.log("7, 8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "8":
    console.log("8, 9, 10, 11, 12, 13, 14, 15");
    break;
    case "9":
    console.log("9, 10, 11, 12, 13, 14, 15");
    break;
    case "10":
    console.log("10, 11, 12, 13, 14, 15");
    break;
    case "11":
    console.log("11, 12, 13, 14, 15");
    break;
    case "12":
    console.log("12, 13, 14, 15");
    break;
    case "13":
    console.log("10, 11, 12, 13, 14, 15");
    break;
    case "14":
    console.log("11, 12, 13, 14, 15");
    break;
    case "15":
    console.log("12, 13, 14, 15");
    break;
    default:
    console.log("неправильно введено число")
}

//задание 5 и 6


function plus(x, y){
return x + y
}

function minus(x, y){
return x - y
}

function composition(x, y){
return x * y
}

function division(x, y){
return x / y
}


function operation(a, b, c){
switch(c){
    case "1":
    return plus(a, b)
    break
    case "2":
    return minus(a, b)
    break
    case "3":
    return composition(a, b)
    break
    case "4":
    return division(a, b)
    break
}
}
console.log(composition(1, 2, 4))
