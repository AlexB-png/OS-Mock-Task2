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
        width: 80vw;
        height: 100vh;

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
          display: flex;
          flex-direction: column;

          align-items: center;
        }

        .selections {
          display: flex;
          flex-direction: column;
          justify-content: space-evenly;

          gap: 5vh;

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

          .submit {
            button {
              width: 20vw;
              height: 3vw;
              font-size: 1rem;
            }
          }

          .guests , .double , .single , .date {
            h1 {
              width: 20vw;
              font-size: 2rem;

              color: var(--green-text);
            }

            input {
              width: 38.5vw;
              height: 3rem;
              font-size: 2rem;

              border-radius: 10px;

              font-family: "montserrat";
              font-weight: 500;
            }
          }
          .date {
            input {
              width: 18vw;
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
        

        <div class="selections">
          <div class="helloStatus">
            <h1 class="hotelSign" style="color: var(--green-text); text-decoration: underline;">Hotel Bookings!</h1>
            <h1 class="welcomeUser" v-if="userName" style="color: var(--green-text);">Welcome {{ userName }}!</h1>
            <h1 class="welcomeUser" v-else style="color: var(--red);">You are not logged in!</h1>
          </div>
          
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
            <h1>Start Date - End Date</h1>
            <input v-model="startDate" type="date">
            <input v-model="endDate" type="date">
          </div>
          <div class="price">
            <h1 class="montserrat">The total price is £{{ totalPrice }}</h1>
          </div>
          <div class="submit">
            <button class="montserrat" :disabled="buttonDisabled || userName === ''" >Continue!</button>
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
  import { ref , watch } from 'vue'
  
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
      const startDate = ref("");
      const endDate = ref("");
      const errorMessage = ref("");

      const buttonDisabled = ref(true);

      watch([guests, single, double, startDate, endDate], () => {
        var slots_in_use = 0;
        slots_in_use = (1 * single.value) + (2 * double.value);
        if (guests.value > 0 && ((single.value > 0) || (double.value > 0)) && startDate.value != "" && endDate.value != "") {
          if (guests.value > slots_in_use) {
            errorMessage.value = "You don't have enough beds to fit everyone!";
            buttonDisabled.value = true;
            emit("updatePrice", NaN);
          } else {
            console.log(guests.value, slots_in_use)
            errorMessage.value = "";
            var newTotal = ((guests.value * 25) + (single.value*25) + (double.value*50));

            const dateStart = new Date(startDate.value);
            const dateEnd = new Date(endDate.value);

            const date1 = new Date(dateStart);
            const date2 = new Date(dateEnd);
            const diffTime = Math.abs(date2 - date1);
            const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24)); 

            newTotal = newTotal * diffDays;

            if (newTotal != 0) {
              emit("updatePrice", newTotal)
              buttonDisabled.value = false;
            } else {
              emit("updatePrice", "N/A");
              buttonDisabled.value = true;
            }
          }
      } else {
        emit("updatePrice", NaN);
        buttonDisabled.value = true;
      }
    })

      return { guests , single , double , startDate , endDate , errorMessage, buttonDisabled};
  }}
</script>