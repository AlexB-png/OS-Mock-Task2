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
          <span class="welcomeUser montserrat">Payment Page!</span>

            <span class="roomNum montserrat">Room Number: {{ bookedRoomId }}</span>
        </div>
        
        <div class="column">
          <div class="columnOne">
            <div class="row">
              <span class="inputText montserrat">Cardholder Name:</span>
              <input type="text" placeholder="Your Name Here!">
            </div>

            <div class="row">
              <span class="inputText montserrat">Card Number:</span>
              <input type="number" placeholder="Your Card Number!">
            </div>

            <div class="row">
              <span class="inputText montserrat">CVV Number:</span>
              <input type="password" placeholder="Your CVV Number!">
            </div>

            <div class="row">
              <span class="inputText montserrat">Expiration Date:</span>
              <input type="date">
            </div>

            <div class="row">
              <span class="inputText montserrat">Billing Address!</span>
              <input type="text" placeholder="Your Billing Address!">
            </div>
          </div>

          <div class="columnTwo">
            
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
  export default {
    name: 'PaymentPage',
    props: {
      'bookedRoomId': String 
    },
    setup(props) {

      return {}
    }
  }
</script>