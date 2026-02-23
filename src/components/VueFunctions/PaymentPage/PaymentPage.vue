<style scoped lang="scss">
  body {
    height: 100vh;
    width: 100vw;
  }
  
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    
    background-color: var(--green);
    height: 100%;

    .content {
      .title {
        display: flex;
        flex-direction: column;
        height: 10vw;
        justify-content: space-evenly;
        
        color: var(--green-text);
        text-align: center;

        .welcomeUser {
          text-decoration: underline;
          font-size: 2.5rem;
        }

        .roomNum {
          font-size: 1.5rem;
          text-decoration: none;
        }
      }
      
      height: 75%;
      width: 80%;

      display: flex;
      justify-content: space-evenly;
      align-items: center;

      flex-direction: column;

      background-color: var(--green-light);
      border-radius: 20px;

      .row {
        display: flex;
        flex-direction: row;
        width: 100%;

        gap: 2vw;

        justify-content: space-evenly;
        align-items: center;

        input {
          height: 2vw;
          font-size: 2rem;
        }

        h1 {
          font-size: 2rem;
        }
      }

      .column {
        display: flex;
        flex-direction: row;

        justify-content: space-evenly;
        align-items: center;

        width: 90%;

        .columnOne, .columnTwo {
          display: flex;
          
          flex-direction: column;
          justify-content: space-evenly;
          align-items: center;
          
          height: 30vw;

          span {
            width: 20vw;
            text-align: center;
          }
          
          .inputText {
            font-size:1.5rem;

            color: var(--green-text);
          }

          input {
            font-size: 1rem;
            width: 50%;
          }
        }
      }
    }
  }
</style>


<template>
  <body>
    <main>
      <div class="content" v-if="bookedRoomId">
        <div class="title">
          <span class="welcomeUser montserrat">Payment Page!!</span>

            <span class="roomNum montserrat">Booking ID: {{ bookedRoomId }}</span>
        </div>
        
        <div class="column">
          <div class="columnOne">
            <div class="row">
              <span class="inputText montserrat">Cardholder Name:</span>
              <input type="text" v-model="CardholderName" placeholder="Your Name Here!">
            </div>

            <div class="row">
              <span class="inputText montserrat">Card Number:</span>
              <input type="text" v-model="CardNum" placeholder="Your Card Number!">
            </div>

            <div class="row">
              <span class="inputText montserrat">CVV Number:</span>
              <input type="password" v-model="CVV" placeholder="Your CVV Number!">
            </div>

            <div class="row">
              <span class="inputText montserrat">Expiration Date:</span>
              <input type="date" v-model="ExpiryDate">
            </div>

            <div class="row">
              <span class="inputText montserrat">Billing Address!</span>
              <input type="text" v-model="BillAddress" placeholder="Your Billing Address!">
            </div>
          </div>

          <div class="columnTwo">
            <button :disabled="!(CardholderName && CardNum && CVV && ExpiryDate && BillAddress)" v-on:click="CardInputButton">Submit</button>

            <button :disabled="!!(CardholderName && CardNum && CVV && ExpiryDate && BillAddress)" v-on:click="ClaimLoyalty">Claim Loyalty!</button>
          </div>
        </div>
      </div>

      <div v-else>
        <h1>Your Selection Has Been Lost, Please Go Back To Login</h1>
      </div>
    </main>
  </body>
</template>


<script>
  import { ref } from "vue"
  import { useRouter } from "vue-router";

  export default {
    name: 'PaymentPage',
    props: {
      'bookedRoomId': String,
      'bookingType': String,
      'userName': String,
    },
    setup(props) {
      const CardholderName = ref("")
      const CardNum = ref("")
      const CVV = ref("")
      const ExpiryDate = ref("")
      const BillAddress = ref("")
      const router = useRouter();

      async function CardInputButton() {
        let request = await fetch("http://127.0.0.1:5001/payment", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            RoomNumber : props.bookedRoomId,

            CardName : CardholderName.value,
            CardNum : CardNum.value,
            CVV : CVV.value,
            Expiry : ExpiryDate.value,
            BillAddress : BillAddress.value,
            BookingType : props.bookingType,
            Loyalty: false,

            Username : props.userName,
          })
        })

        request = await request.json()
        console.log(request["message"])

        if (request["message"] == 'Success!') {
          router.push("/")
        }
      }

      async function ClaimLoyalty() {
        let request = await fetch("http://127.0.0.1:5001/claimloyalty", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            Username : props.userName,
          })
        })

        request = await request.json()
        
        if (request[0] === true) {
          let request = await fetch("http://127.0.0.1:5001/payment", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            RoomNumber : props.bookedRoomId,

            CardName : "",
            CardNum : "",
            CVV : "",
            Expiry : "",
            BillAddress : "",
            BookingType : props.bookingType,
            Loyalty: true,

            Username : props.userName,
          })
        })
        console.log(request)
        } else {
          console.log("Nope!")
        }
      }

      return { CardholderName , CardNum , CVV , ExpiryDate , BillAddress , CardInputButton , ClaimLoyalty}
    }
  }
</script>