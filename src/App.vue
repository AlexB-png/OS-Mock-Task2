<style lang="scss">
  :root {
  --green : #A8BBA3;
  --white : #F7F4EA;
  --pink : #EBD9D1;
  --orange : #B87C4C;
  --red : #b84e4c;

  --green-hover : #8aa783;

  --green-light : rgb(208, 227, 203);

  --green-text : rgb(108, 127, 103);

  --green-lighter : rgb(188, 207, 183);
  }

  :root.contrast {
    --green : #495146;
    --white : #8f8d89;
    --pink : #8e6958;
    --orange : #5b3e26;


    --red : #682c2b;

    --green-hover : #455342;

    --green-light : rgb(122, 134, 119);

    --green-text : rgb(79, 69, 82) ;

    --green-lighter : rgb(102, 114, 99)
  }
  
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
      width: 30%;
      height: 80%;

      @media (max-width: 1024px) {
        height: 70%;
        width: 80%;
      }

      h1 {
        margin: 0;
        color: var(--red);
      }

      border-radius: 10px;

      .overlayTopBar {
        display: flex;
        justify-content: right;
        align-items: end;
        width: 100%;

        height: 2vw;

        .hideButton {
          width: 2vw;
          height: 2vw;

          border-radius: 10px;

          border: none;
          cursor:pointer;

          font-size: 1rem;

          background-color: var(--green-light);

          transition: all 0.1s ease-in-out;
        }

        .hideButton:hover {
          background-color: var(--green-hover);
        }
      }

      .overlayContentButtons {
        display: flex;
        height: 90%;

        flex-direction: column;

        justify-content: space-evenly;
        align-items: center;

        gap: 1vw;

        button {
          width: 20vw;
          height: 4vw;

          font-size: 1rem;

          @media (max-width: 1024px) {
            width: 40vw;
            height: 8vw;

            font-size: 2rem;
          }
        }
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
          <button v-on:click="showOverlay" class="hideButton">X</button>
        </div>

        <div class="overlayContentButtons">
          <h1 v-if="! username">You are not logged in!</h1>
          <button v-on:click="logOut" :disabled="! username">Log Out!</button>
          <button id="bookings" v-on:click="dashBoardButton" :disabled="! username">See Your Bookings!</button>
          <button id="cancel" v-on:click="dashBoardButton" :disabled="! username">Cancel Bookings!</button>
          <button id="settings" v-on:click="dashBoardButton" :disabled="! username">Settings!</button>
          <button id="settings" v-on:click="darkMode">Dark Mode!</button>
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

    <router-view 
      @updateTopBar="updateTopBar" 
      @updatePrice="updatePrice"
      @updateBookingType = "updateBookingType"
      @logOut = "logOut"
      @updateBookingRoomId = "UpdateBookedRoomID"
      :user-name="username"
      :total-price="totalPrice"
      :booking-type="bookingType"
      :dashboard-option="dashBoardOption"
      :booked-room-id="BookedRoomID"
    ></router-view>
  </main>
</template>

<script>
  import { ref } from 'vue';
  import LoginPage from './components/VueFunctions/LoginPage/LoginPage.vue';
  import { useRouter } from "vue-router";

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

      // These are the variables for the payment page and updating //
      const BookedRoomID = ref(0)

      const UpdateBookedRoomID = (BookedRoom) => {
        BookedRoomID.value = BookedRoom
      }
      //

      const router = useRouter();

      const dashBoardOption = ref("")
      const overlayShown = ref("none")

      const darkMode = () => {
        document.documentElement.classList.toggle("contrast");
      }

      // Update the username on the top bar
      // Emit message from LoginPage.vue //
      const updateTopBar = (user) => {
        usernameTopBar.value = user;
        username.value = user;
        color.value = "rgb(0,100,0)"
      }

      const logOut = () => {
        username.value = ""
        usernameTopBar.value = "Not Logged In"
        color.value = "rgb(100,0,0)"
      }

      // Emit message from HotelBooking.vue //
      const updatePrice = (newPrice) => {
        totalPrice.value = newPrice;
      }

      const updateBookingType = (booking) => {
        bookingType.value = booking
      }

      const showOverlay = () => {
        if (overlayShown.value == "flex") {
          overlayShown.value = "none";
        } else {
          overlayShown.value = "flex";
        }
        
      }

      const dashBoardButton = () => {
        dashBoardOption.value = event.srcElement.id;

        showOverlay()

        router.push("/dashboard")
      }

      return { username,
              usernameTopBar,
              color,
              updateTopBar,
              totalPrice,
              updatePrice,
              updateBookingType,
              bookingType,
              showOverlay,
              overlayShown,
              logOut,
              dashBoardOption,
              dashBoardButton,
              BookedRoomID,
              UpdateBookedRoomID,
              darkMode
            };
    }
  }
</script>
