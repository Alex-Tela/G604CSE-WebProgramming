const buttons = document.querySelectorAll('button');
const inputs = document.querySelectorAll('input');
const warning = document.getElementById('warning');
let clicks = 0;

buttons[0].addEventListener('click', () => {
    clicks++;
    if (clicks === 1) {
        warning.style.display = "block";
    } else if (clicks > 1) {
        inputs.forEach(input => {
            input.value = "";
        })
        clicks = 0;
        warning.style.display = "none";
    }
    console.log(clicks);
});

buttons[1].addEventListener('click', () => {
    let check = 0;
    for (let input of inputs) {
        if (input.value === "") {
            check += 1;
        }
    }

    console.log(check);
    if (check < 1) {
        const data = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value,
            confirm: document.getElementById('confirm').value
        } 

        const response = fetch("", {
            method: "POST",
            body: JSON.stringify(data)
        }).then((r) => {
            console.log("Congratulations! You have successfully created an account!\n" + JSON.stringify(data))})
        .catch((r) => {
            console.log("Congratulations! You have successfully created an account!\n" + JSON.stringify(data))});
    
        // let sum = 0;
        // for (let i = 0; i <= 50; i++) {
        //     sum += i;
        // }
        // console.log(`Sum of numbers up to 50: ${sum}`)
    }
});