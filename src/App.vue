<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

  .montserrat {
    font-family: "Montserrat", sans-serif;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
  }
  
  .navBar {
    position: fixed;
    height: 5vh;
    width: 100%;

    top: 0px;
    left: 0px;

    z-index: 9999;

    background-color: rgba(235, 217, 209,0.5);
    backdrop-filter: blur(4px);

    .navBarText {
      display: flex;
      align-items: center;
      justify-content: right;
      gap: 5vw;

      height: 5vh;
    }
  }
</style>

<template>
  <main>
    <div class="navBar montserrat">
      <div class="navBarText">
        <h1 v-bind:style="{color:color}" class="montserrat" style="font-size: 1rem;">{{ usernameTopBar }}</h1>
        <RouterLink to="/login">Login!</RouterLink>
        <RouterLink to="/">Homepage!</RouterLink>
        <RouterLink to="/hotelbooking">Hotel Booking!</RouterLink>
        <h1>Zoo Bookings!</h1>

      </div>
    </div>

    <router-view @updateTopBar="updateTopBar" :user-name="username"></router-view>
  </main>
</template>

<script>
  import { ref } from 'vue';
  import { RouterLink } from 'vue-router';
  import LoginPage from './components/VueFunctions/LoginPage.vue';

  export default {
    components: {
      LoginPage
    },
    setup() {
      const username = ref("")
      const usernameTopBar = ref("Not Logged In");
      const color = ref("rgb(100,0,0)");

      // Update the username on the top bar
      const updateTopBar = (user) => {
        usernameTopBar.value = user;
        username.value = user;
        color.value = "rgb(0,100,0)"
        console.log(user)
      }

      return { username , usernameTopBar , color , updateTopBar};
    }
  }
</script>
