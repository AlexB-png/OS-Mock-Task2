<style scoped>
  * {
    padding: 0;
    margin: 0;
  }

  main {
    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    height: 100vh;

    background-color: var(--green);

    .content {
      background-color: var(--green-light);
      border-radius: 20px;

      width: 80vw;
      height: 35vw;

      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;

      .settings {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        button {
          width: 20vw;
          height: 4vw;
          font-size: 1.5rem;
        }
      }
    }
  }
</style>


<template>
  <main>
    <div class="content">
      <div v-if="dashboardOption == 'bookings'">
        <h1>Hello From The Bookings Page!</h1>
      </div>

      <div v-else-if="dashboardOption == 'cancel'">
        <h1>Hello From The cancel Page!</h1>
      </div>

      <div v-else-if="dashboardOption == 'settings'" class="settings">
        <button v-on:click="deleteButton" class="montserrat" :disabled="! userName">{{ deleteText }}</button>
      </div>

      <div v-else>
        <h1>Your Selection Has Been Lost, Please Try Again!</h1>
      </div>
    </div>

    
    
  </main>
</template>


<script>
  import { ref , watch } from 'vue'
    import { useRouter } from "vue-router";
  
  export default {
    name: "Dashboard",
    props: {
      'userName' : String,
      'dashboardOption' : String
    },
    setup(props, {emit}) {
      const deleteText = ref("Delete Account!")

      const router = useRouter()

      var deleteCount = -1

      async function deleteButton() {
        var messages = ["Are You sure?", "Are you REALLY sure?"]

        deleteCount += 1

        console.log("Works")

        if (deleteCount < 2) {
          deleteText.value = messages[deleteCount]
        } else {
          let request = await fetch("http://127.0.0.1:5001/deleteaccount", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: props.userName,
          })
          })

          var response = await request.json()

          deleteText.value = "Goodbye!"

          if (response['Status'] == false) {
            deleteText.value = "Failed!"
            alert(response['message'])
          } else {
            console.log(response["Status"])
            console.log(response["message"])
            await new Promise(resolve => setTimeout(resolve, 1000));

            emit("logOut")
            router.push("/login")
          }
        }
      }

      return {deleteText, deleteButton}
    }
  }
</script>