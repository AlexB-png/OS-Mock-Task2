
<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

  .montserrat {
    font-family: "Montserrat", sans-serif;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
  }

  body {
    margin: 0;
  }
  
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    margin:0;

    background-image: url(./assets/giraffe.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;

    height: 100vh;
  }
  
  .content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
    width: 35vw;

    background-color: rgba(200,200,200,0.5);
    backdrop-filter: blur(4px);
    border-radius: 20px;

    flex-direction: column;
    gap: 5vh;

    h1 , h2 {
      color: rgb(65, 57, 0);
    }

    button {
      width: 10vw;
      height: 5vh;

      border-radius: 5px;
    }
  }
</style>

<template>
  <main>
    <div class="content">
      <h1 class="montserrat">Login Page!</h1>

      <div>
        <h2>Username:</h2>
        <input type="text" name="username" id="userInput">
      </div>

      <div>
        <h2>Password:</h2>
        <input type="password" id="passInput">
      </div>

      <div style="display: flex; gap: 2vw;">
        <button v-on:click="loginButton">Login!</button>
        <button v-on:click="createAccount">Create Account!</button>
      </div>

      <div>
        <h1>{{ status }}</h1>
      </div>
    </div>
  </main>
</template>

<script setup>
  import { ref } from 'vue'
  
  const status = ref("")
  
  async function createAccount() {
    // Get username and password from the inputs 
    let username = document.getElementById("userInput").value
    let password = document.getElementById("passInput").value
    //
    
    // Make a request with username and password as parameters
    let request = await fetch("http://127.0.0.1:5001/createaccount", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username,
        password: password
      })
    })
    //

    // Turn response into a JSON
    request = await request.json()
    //

    // Updates the status text
    status.value = request["Status"]
    //
  }

  async function loginButton() {
    // Get username and password from the inputs 
    let username = document.getElementById("userInput").value
    let password = document.getElementById("passInput").value
    //

    // Make a request with username and password as parameters
    let request = await fetch("http://127.0.0.1:5001/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username,
        password: password
      })
    })
    //

    // Turn response into a JSON
    request = await request.json()
    //

    // Update the status text
    status.value = request["Message"]
    //
  }
</script>