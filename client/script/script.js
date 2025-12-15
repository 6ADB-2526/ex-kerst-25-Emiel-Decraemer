const usernameInpt = document.querySelector("#username")
const passwordInpt = document.querySelector("#password")
const btnSignIn = document.querySelector("#btnSI")
const sectionBefore = document.querySelector("#beforLogin")

fetch("https://ex-kerst-2025.onrender.com/user/")
.then(resultaat => resultaat.json())
.then((gebruikers) => {
    console.log(gebruikers);
    gebruikers.forEach(gebruiker => {   // find() wou niet werken dus vervangen met forEach()
        if (gebruiker.login == usernameInpt.value && gebruiker.password == passwordInpt.value) {
            btnSignIn.addEventListener("click", () => {
                console.log(usernameInpt.value);
            })
        }
    });
})

