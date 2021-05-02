const form = document.querySelector("#form");


form.onsubmit = (event) => {

    event.preventDefault()

    const usernameEl = document.querySelector("#username");
    const passwordEl = document.querySelector("#password");

    const credentials = {
        username: usernameEl.value,
        password: passwordEl.value
    }

    sendCredentialsToApi(credentials)

}

async function sendCredentialsToApi(credentials) {

    const request = await fetch('/api/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })

    const response = await request.json()

    if (response.message === 'Logging successful!') {
        window.location.href = '/secret'

    } else {
        console.log(response)
    }
}