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
          font-size: 2rem;
        }
      }
    }
  }
</style>


<template>
  <main>
    <div class="content">
      <h1 v-if="userName">Welcome {{ userName }}</h1>
      <h1 v-else>You Are Not Logged In!</h1>

      <div v-if="dashboardOption == 'bookings'">
        <h1>Hello From The Bookings Page!</h1>
      </div>

      <div v-else-if="dashboardOption == 'cancel'">
        <h1>Hello From The cancel Page!</h1>
      </div>

      <div v-else-if="dashboardOption == 'settings'" class="settings">
        <button v-on:click="deleteButton" class="montserrat">{{ deleteText }}</button>
      </div>

      <div v-else>
        <h1>Your Selection Has Been Lost, Please Try Again!</h1>
      </div>
    </div>

    
    
  </main>
</template>


<script>
  import { ref , watch } from 'vue'
  
  export default {
    name: "Dashboard",
    props: {
      'userName' : String,
      'dashboardOption' : String
    },
    setup(props) {
      const deleteText = ref("Delete Account!")

      var deleteCount = -1

      const deleteButton = () => {
        var messages = ["Are You sure?", "Are you REALLY sure?"]

        deleteCount += 1

        console.log("Works")

        if (deleteCount < 2) {
          deleteText.value = messages[deleteCount]
        } else {
          deleteText.value = "Account Deleted!"
        }
      }

      return {deleteText, deleteButton}
    }
  }
</script>