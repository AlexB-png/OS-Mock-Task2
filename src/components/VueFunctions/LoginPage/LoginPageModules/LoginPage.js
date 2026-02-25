import { ref } from 'vue'

  export default {
    name: 'LoginPage',
      setup(_, { emit }) {
        const status = ref("")
        const statusColor = ref("rgb(0,0,0)")
        const username = ref("")
        const password = ref("")

      async function createAccount() {
        // Make a request with username and password as parameters
        let request = await fetch("http://127.0.0.1:5001/createaccount", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value
          })
        })
        //

        // Turn response into a JSON
        request = await request.json()
        //

        // Updates the status text
        status.value = request["Status"]
        statusColor.value = request["Color"]
        //
      }

      async function loginButton() {
        // Make a request with username and password as parameters
        let request = await fetch("http://127.0.0.1:5001/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value
          })
        })
        //

        // Turn response into a JSON
        request = await request.json()
        //

        // Update the status text
        status.value = request["Message"]
        statusColor.value = request["Color"]
        //

        if (status.value == 'Successfully Logged In') {
          emit('updateTopBar', username.value)
        }
      }

      return { username, password, status, statusColor, loginButton, createAccount }
    }
  }