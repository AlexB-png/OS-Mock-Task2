<style scoped lang="scss">
  main {
    background-color: var(--green-light);
    height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    .content {
      width: 60%;
      height: 80%;

      display: flex;
      justify-content: space-evenly;
      align-items: center;

      border-radius: 20px;

      background-color: var(--green);
    }
  }
</style>


<template>
  <body>
    <main>
      <div class="content">
        <h1>{{adminStatus}}!</h1>
      </div>
    </main>
  </body>
</template>


<script>
  import { onMounted } from 'vue';
  import { useRouter } from "vue-router";
  import { ref } from 'vue';

  export default {
    props: {
      userName : String
    },
    setup(props) {
      const adminStatus = ref(false)
      
      onMounted(() => {
        console.log("Beep Boop checking you are an admin")

        // Just send them back to / if they arent logged in
        if (! props.userName) {
          router.push("/")
        } else {
          // Check they are an admin
          checkAdmin()
        }
      })

      async function checkAdmin() {
        let request = await fetch("http://127.0.0.1:5001/checkadmin", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: props.userName,
          })
        })

        adminStatus.value = (await request.json())['status']
      }

      const router = useRouter()

      return { checkAdmin , adminStatus }
    }
  }
</script>