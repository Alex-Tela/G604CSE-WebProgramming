const buttons = document.querySelectorAll('button');
const inputs = document.querySelectorAll('input');
let clicks = 0;

buttons[0].addEventListener('click', () => {
    clicks++;
    if (clicks === 1) {
        console.log("Warning! You are about to reset your inputs. Are you sure you want to continue?");
    } else if (clicks > 1) {
        inputs.forEach(input => {
            input.value = "";
        })
        clicks = 0;
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
        console.log("Congratulations! You have successfully created an account!");
        let sum = 0;
        for (let i = 0; i <= 50; i++) {
            sum += i;
        }
        console.log(`Sum of numbers up to 50: ${sum}`)
    }
});