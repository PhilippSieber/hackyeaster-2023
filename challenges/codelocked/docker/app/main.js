code = "";

var audioDelete = new Audio("delete.mp3");
audioDelete.load();
var audioClick = new Audio("click.wav");
audioClick.load();
var audioSuccess = new Audio("success.mp3");
audioSuccess.load();
var audioFail = new Audio("fail.mp3");
audioFail.load();

wasmMemory = null;
wasmCheck = null;

function checkWASM(code) {
    const pinArray = new Int32Array(wasmMemory.buffer, 0, 26);
    encode(code, pinArray);
    wasmCheck(pinArray.byteOffset, pinArray.length);
    return decode(pinArray);
}

function play(file) {
    a = new Audio(file);    
    a.play();
}

function press(input) {
    if (input == "*") {
        play("delete.mp3");
        $("#yellow").show(0).delay(200).hide(0);
        code = "";
    } else if (input == "#") {
        msg = checkWASM(code);
        if (msg.startsWith("he2023")) {
            play("success.mp3");
            audioSuccess.play();
            $("#green").show(0).delay(5000).hide(0);
        } else {
            play("fail.mp3");
            $("#red").show(0).delay(1000).hide(0);
        }
        setTimeout(function() {alert(msg);}, 200)
    } else {
        $("#yellow").show(0).delay(200).hide(0);
        play("click.wav");
        code = (code + input).substr(-8, 8);
    }
}

const encode = function stringToIntegerArray(string, array) {
    for (let i = 0; i < string.length; i++) {
        array[i] = string[i].charCodeAt(0);
    }
};

const decode = function integerArrayToString(array) {
    let string = "";
    for (let i = 0; i < array.length; i++) {
        string += String.fromCharCode(array[i]);
    }
    return string;
};

$(document).ready(function () {
    (async () => {
        const response = await fetch("check.wasm");
        const file = await response.arrayBuffer();
        const wasm = await WebAssembly.instantiate(file);
        const {memory, check} = wasm.instance.exports;
        wasmMemory = memory;
        wasmCheck = check;
    })();
})