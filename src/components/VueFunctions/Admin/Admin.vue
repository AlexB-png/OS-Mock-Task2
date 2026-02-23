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

      .AdminContent {
        height: 100%;
        
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;

        .title {
          font-size: 3rem;
          color: var(--green-text);
          text-decoration: underline;
        }

        .object {
          background-color: var(--green-light);
          padding: 3vw;
          padding-top: 5vw;
          padding-bottom: 5vw;

          display: flex;
          justify-content: space-evenly;
          align-items: center;

          flex-direction: column;

          border-radius: 10px;

          .ObjectTitle {
            color: var(--green-text);
            font-size: 2.5rem;

            text-decoration: underline;
          }

          .HotelCancelButton {
            width: 100%;
            height: 3vw;

            font-size: 2rem;

            color: var(--green-text);
          }

          .ObjectColumns {
            display: flex;
            flex-direction: row;
            gap: 2vw;

            .ColumnsObject {
              display: flex;
              flex-direction: row;

              align-items: center;
              justify-content: center;
              
              color: var(--green-text);
              gap: 2vw;

              input {
                height: 2vw;
                font-size: 2rem;
                width: 10vw;
              }
            }
          }
        }
      }
    }
  }
</style>


<template>
  <body>
    <main>
      <div class="content">
        <div v-if="adminStatus != false" class="AdminContent">
          <span class="title montserrat">Welcome Admin!</span>

          <div class="objects">
            <div class="object">
              <span class="ObjectTitle montserrat">Cancel Hotel Booking</span>
              
              <div class="ObjectColumns">
                <div class="ColumnsObject">
                  <h1>Booking ID:</h1>
                  <input type="number" class="montserrat" v-model="HotelCancelId">
                </div>

                <div class="ColumnsObject">
                  <h1>Username:</h1>
                  <input type="number" v-model="HotelCancelUser" class="montserrat">
                </div>
              </div>

              <button class="HotelCancelButton montserrat" v-on:click="HotelDeleteBooking">{{StatusMessage}}</button>
              
            </div>
          </div>
        </div>
        
        <div v-else>
          <h1>You are not an admin!</h1>
        </div>
        
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

      // Hotel Delete Booking Button //
      const HotelCancelId = ref(0)
      const HotelCancelUser = ref("")
      const StatusMessage = ref("Submit")
      async function HotelDeleteBooking() {
        let request = await fetch("http://127.0.0.1:5001/cancel", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            Username: HotelCancelUser.value,
            BookingType : 'hotel',
            BookingId : HotelCancelId.value
          })
        })

        StatusMessage.value = (await request.json())

      }

      const router = useRouter()

      return { checkAdmin , adminStatus , HotelDeleteBooking, HotelCancelUser , HotelCancelId , StatusMessage}
    }
  }
</script>