<style>
  :root {
    --green : #A8BBA3;
    --white : #F7F4EA;
    --pink : #EBD9D1;
    --orange : #B87C4C;
    --red : #b84e4c;

    --green-light : rgb(208, 227, 203);

    --green-text : rgb(108, 127, 103);
  }
</style>

<style scoped>
  body {
    height: 120vh;
    background-color: var(--green);

    display: flex;
    justify-content: center;
    align-items: center;

    .content {
      
      display: flex;
      justify-content: center;
      align-items: center;
      
      .box {
        height: 100vh;
        width: 80vw;

        display: flex;
        justify-content: center;
        align-items: center;

        flex-direction: column;
        
        background-color: var(--green-light);
        border-radius: 20px;

        .welcomeUser {
          font-size: 2rem;
          padding-top: 4vh;
        }

        .hotelSign {
          font-size: 3rem;
          padding-top: 2vh;
        }

        .helloStatus {
          height: 25vh;

          display: flex;
          flex-direction: column;

          align-items: center;
        }

        .selections {
          height: 55vh;

          display: flex;
          flex-direction: column;
          justify-content: space-evenly;

          .row {
            display: flex;
            flex-direction: row;
            gap: 2.5vw;
          }

          .submit , .status , .price{
            display: flex;
            justify-content: center;
            align-items: center;

            color: var(--green-text);
          }

          .guests , .double , .single , .date {
            h1 {
              width: 20vw;
              font-size: 2rem;

              color: var(--green-text);
            }

            input {
              width: 18vw;
              height: 3rem;
              font-size: 2rem;

              border-radius: 10px;

              font-family: "montserrat";
              font-weight: 500;
            }
          }
        }

        h1 {
          margin: 0;
        }

        
      }
    }
  }
</style>

<template>
  <body>
    <div class="content">
      <div class="box">
        <div class="helloStatus">
          <h1 class="hotelSign" style="color: var(--green-text); text-decoration: underline;">Hotel Bookings!</h1>
          <h1 class="welcomeUser" v-if="userName" style="color: var(--green-text);">Welcome {{ userName }}!</h1>
          <h1 class="welcomeUser" v-else style="color: var(--red);">You are not logged in!</h1>
        </div>

        <div class="selections">
          <div class="guests row">
            <h1>Guests:</h1>
            <input type="number" id="guests" value="0" v-model="guests">
          </div>
          <div class="single row">
            <h1>Single Beds:</h1>
            <input v-model="single" type="number" value="0">
          </div>
          <div class="double row">
            <h1>Double Beds:</h1>
            <input v-model="double" type="number" value="0">
          </div>
          <div class="date row">
            <h1>Date of stay:</h1>
            <input v-model="date" type="date">
          </div>
          <div class="price">
            <h1 class="montserrat">The total price is {{ totalPrice }}</h1>
          </div>
          <div class="submit">
            <button class="montserrat" v-on:click="updatePrice(guests)" :disabled="userName === ''" >Continue!</button>
          </div>
          <div class="status">
            <h1 class="montserrat">{{ errorMessage }}</h1>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
  import { ref } from 'vue'
  
  export default {
    name: "Booking",
    props: {
      'userName': String,
      'totalPrice': Number,
    },
    setup(props, { emit }) {
      const guests = ref(0);
      const single = ref(0);
      const double = ref(0);
      const date = ref("")
      const errorMessage = ref("")
      
      const updatePrice = (newTotal) => {
        if (guests.value > 0 && ((single.value > 0) || (double.value > 0)) && date.value != "") {
          emit("updatePrice", newTotal)
        } else {
          errorMessage.value = "Missing Inputs!";
        };
        
        
      }

      return { updatePrice , guests , single , double , date , errorMessage};
  }};
</script>