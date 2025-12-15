// nodige variabelen ophalen
const usernameInpt = document.querySelector("#username")
const passwordInpt = document.querySelector("#password")
const btnSignIn = document.querySelector("#btnSI")
const sectionBefore = document.querySelector("#beforLogin")
const sectionAfter = document.querySelector("#afterLogin")


// object ophalen
fetch("https://ex-kerst-2025.onrender.com/user/")
.then(resultaat => resultaat.json())
.then((gebruikers) => {
    // functie geven aan je object
    console.log(gebruikers);
    gebruikers.forEach(gebruiker => {   // find() wou niet werken dus vervangen met forEach()
        if (gebruiker.login == usernameInpt.value && gebruiker.password == passwordInpt.value) {
            btnSignIn.addEventListener("click", () => {
                sectionBefore.hidden = true
                sectionAfter.hidden = false
            })
        }
    });
})