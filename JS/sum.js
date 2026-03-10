function sum(...args) {
    // Your implementation

    const total = args.reduce((acc, curr) => acc += curr, 0)
    return total
}

//For the purpose of user debugging.
console.log(sum(100, 200, 300, 400));