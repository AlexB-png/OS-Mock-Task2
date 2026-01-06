
<style scoped>

</style>

<template>
  <main>
    <div>
      <h1>Login Page!</h1>
    </div>

    <div>
      <h2>Username:</h2>
      <input type="text" name="username" id="userInput">
    </div>

    <div>
      <h2>Password:</h2>
      <input type="password" id="passInput">
    </div>

    <div>
      <button v-on:click="button">Execute!</button>
      <button v-on:click="createAccount">Create Account!</button>
    </div>

    <div>
      <h1>{{ status }}</h1>
    </div>
  </main>
</template>

<script setup>
  import { ref } from 'vue'
  
  const status = ref("Status Message Here")
  
  async function createAccount() {
    let username = "ABC"
    let password = 123
    
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

    request = await request.json()

    console.log(request["Status"])
    status.value = request["Status"]
  }
</script>