fs = require("fs")

a = 100;

setImmediate(() => {
    console.log("setImmediate")
});

fs.readFile("sample.txt", "utf8", (err, data) => {
    if (err) {
        console.log(err)
    } else {
        console.log(data)
    }
});

setTimeout(() => {
    console.log("setTimeout")
}, 0);

function test(){
    console.log("a=",a)
};

test()
console.log("last line");
