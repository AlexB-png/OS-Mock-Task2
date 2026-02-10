<style lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');

  .montserrat {
    font-family: "Montserrat", sans-serif;
    font-optical-sizing: auto;
    font-weight: 700;
    font-style: normal;
  }

  .overlay {
    position: fixed;
    display: none;
    width: 100%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    background-color: rgba(0, 0, 0, 0.5);
    
    z-index: 3;

    .overlayContent {
      background-color: var(--green);
      width: 30vw;
      height: 30vw;

      .overlayTopBar {
        align-items: right;
        width: 100%;
      }
    }
  }
  
  .navBar {
    position: fixed;
    height: 5vh;
    width: 100%;

    top: 0px;
    left: 0px;

    z-index: 2;

    background-color: rgba(235, 217, 209,0.5);
    backdrop-filter: blur(4px);

    .navBarText {
      display: flex;
      align-items: center;
      justify-content: right;
      gap: 5vw;

      padding-right: 5vw;

      height: 5vh;

      select {
        width: 2vw;
        height: 2vw;
        border-radius: 100px;
      }

      button {
        width: 2vw;
        height: 2vw;
        border-radius: 2vw;
        background-image: url('./assets/pfp.png');

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
      }
    }
  }
</style>

<template>
  <main>
    <div class="overlay" v-bind:style="{display: overlayShown }">
      <div class="overlayContent">
        <div class="overlayTopBar">
          <button v-on:click="showOverlay">X</button>
        </div>
      </div>
    </div>
    <div class="navBar montserrat">
      <div class="navBarText">
        <h1 v-bind:style="{color:color}" class="montserrat" style="font-size: 1rem;">{{ usernameTopBar }}</h1>
        <RouterLink to="/login">Login!</RouterLink>
        <RouterLink to="/">Homepage!</RouterLink>
        <RouterLink to="/hotelbooking">Hotel Booking!</RouterLink>
        <RouterLink to="/zoobooking">Zoo Booking!</RouterLink>
        <button v-on:click="showOverlay"></button>
      </div>
    </div>

    <router-view @updateTopBar="updateTopBar" 
      @updatePrice="updatePrice"
      @updateBookingType = "updateBookingType"
      :user-name="username"
      :total-price="totalPrice"
      :booking-type="bookingType"
    ></router-view>
  </main>
</template>

<script>
  import { ref } from 'vue';
  import { RouterLink } from 'vue-router';
  import LoginPage from './components/VueFunctions/LoginPage/LoginPage.vue';

  export default {
    components: {
      LoginPage
    },
    setup() {
      const username = ref("")
      const usernameTopBar = ref("Not Logged In");
      const color = ref("rgb(100,0,0)");
      const totalPrice = ref(0);
      const bookingType = ref("")

      const overlayShown = ref("none")

      // Update the username on the top bar
      // Emit message from LoginPage.vue //
      const updateTopBar = (user) => {
        usernameTopBar.value = user;
        username.value = user;
        color.value = "rgb(0,100,0)"
        console.log(user)
      }

      // Emit message from HotelBooking.vue //
      const updatePrice = (newPrice) => {
        totalPrice.value = newPrice;
      }

      const updateBookingType = (booking) => {
        bookingType.value = booking
        console.log(bookingType.value)
      }

      const  showOverlay = () => {
        console.log("Overlay Active")
        if (overlayShown.value == "flex") {
          overlayShown.value = "none";
        } else {
          overlayShown.value = "flex";
        }
        
      }

      return { username , usernameTopBar , color , updateTopBar, totalPrice, updatePrice, updateBookingType, bookingType, showOverlay, overlayShown};
    }
  }
</script>
