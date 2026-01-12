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

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5vw;

    top: 0px;
    left: 0px;

    z-index: 9999;

    background-color: rgba(113, 115, 255, 0.5);
    backdrop-filter: blur(4px);
  }
</style>

<template>
  <main>
    <div class="navBar montserrat">
      <RouterLink to="/login">Login!</RouterLink>
      <RouterLink to="/">Homepage!</RouterLink>
      <RouterLink to="/hotelbooking">Hotel Booking!</RouterLink>
      <h1>Zoo Bookings!</h1>
    </div>

    <router-view></router-view>
  </main>
</template>

<script>
  import { RouterLink } from 'vue-router';
</script>
