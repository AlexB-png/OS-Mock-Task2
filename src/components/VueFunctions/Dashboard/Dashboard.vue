<style scoped lang="scss">
  * {
    padding: 0;
    margin: 0;
  }

  main {
    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    height: 100vh;

    background-color: var(--green);


    .content {

      background-color: var(--green-light);
      border-radius: 20px;

      width: 90vw;
      height: 30vw;

      padding-top: 3vw;
      padding-bottom: 3vw;

      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;

      .row {
        display: flex;
        flex-direction: row;
        align-items: center;

        gap: 2vw;
      }

      .bookings {
        width: 100%;
        height: 100%;

        display: flex;
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;

        .title {
          font-size: 2rem;
          color: var(--green-text);
          text-decoration: underline;
        }

        .columns {
          width: 100%;
          
          display: flex;
          flex-direction: row;
          justify-content: space-evenly;
          align-items: center;

          .column1, .column2 {
            .columnTitle {
              color: var(--green-text);
              font-size: 1.5rem;
              text-decoration: underline;
            }
            
            width: 50%;

            display: flex;
            justify-content: center;
            align-items: center;

            flex-direction: column;
          }

          .column1 {
            .hotelBookings {
              display: flex;
              flex-direction: column;
              color: var(--green-text);

              justify-content: center;
              align-items: center;

              .HotelDates {
                display: flex;
                justify-content: space-evenly;

                padding-top: 1vw;
                width: 40vw;

                .object {
                  display: flex;
                  flex-direction: row;
                  gap: 1vw;

                  font-size: 0.75rem;
                }
              }
            }

            
          }

          .column2 {
            .zooBookings {
              display: flex;
              flex-direction: column;
              color: var(--green-text);

              justify-content: center;
              align-items: center;
              .zooDates {
                display: flex;
                justify-content: space-evenly;

                padding-top: 1vw;
                width: 40vw;
              .object {
                  display: flex;
                  flex-direction: row;
                  gap: 1vw;

                  color: var(--green-text);

                  font-size: 0.75rem;
                }
              }
            }
          }
        }
      }

      .cancel {
        height: 100%;

        display: flex;
        flex-direction: column;

        justify-content: space-evenly;
        align-items: center;
        
        .title {
          font-size: 2rem;

          text-decoration: underline;
          color: var(--green-text);
        }

        .welcome {
          font-size: 1.5rem;
          color: var(--green-text);

        }

        select {
          width: 50%;
          height: 5%;

          font-size: 1rem;
        }

        option {
          font-size: 1rem;
        }

        input {
          height: 150%;
        }

        .IdSpan {
          font-size: 1rem;
        }

        button {
          width: 20vw;
          height: 2vw;
          font-size: 1rem;
        }
      }

      .settings {
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;

        height: 100%;

        button {
          width: 20vw;
          height: 4vw;
          font-size: 1.5rem;
        }
      }
    }
  }
</style>


<template>
  <main>
    <div class="content">
      <div v-if="dashboardOption == 'bookings'" class="bookings">
        <span class="montserrat title">Bookings Page</span>

        <div class="columns">
          <div class="column1">
            <span class="montserrat columnTitle">Hotel Bookings</span>

            <div class="hotelBookings">
              <div v-for="x in HotelBookings" class="HotelDates">
                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Start Date</span>
                  <span class="montserrat">{{ x.start_date }}</span>
                </div>
                
                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">End Date</span>
                  <span class="montserrat">{{ x.end_date }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Booking ID</span>
                  <span class="montserrat">{{ x.Booking_ID }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Room Number</span>
                  <span class="montserrat">{{ x.room_number }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Cost</span>
                  <span class="montserrat">{{ x.cost }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="column2">
            <span class="montserrat columnTitle">Zoo Bookings</span>

            <div class="zooBookings">
              <div v-for="y in ZooBookings" class="zooDates">
                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Date</span>
                  <span class="montserrat">{{ y.Date }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Adult</span>
                  <span class="montserrat">{{ y.Adult }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Child</span>
                  <span class="montserrat">{{ y.Child }}</span>
                </div> 

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Cost</span>
                  <span class="montserrat">{{ y.Cost }}</span>
                </div>

                <div class="object">
                  <span style="text-decoration: underline;" class="montserrat">Booking ID</span>
                  <span class="montserrat">{{ y.Booking_ID }}</span>
                </div> 
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else-if="dashboardOption == 'cancel'" class="cancel">
        <span class="title montserrat">Cancel Your Bookings!</span>
        <span class="welcome montserrat">Welcome {{ userName }}!</span>

        <select class="montserrat" v-model="BookingType">
          <option class="montserrat" value="hotel">Hotel</option>
          <option class="montserrat" value="zoo">Zoo</option>
        </select>

        <div class="row">
          <span class="montserrat IdSpan">Booking ID:</span>
          <input class="montserrat" v-model="BookingId" type="number">
        </div>

        <button class="montserrat" v-on:click="deleteBooking" :disabled="!(BookingType && BookingId)">Delete Your Booking!</button>
      </div>

      <div v-else-if="dashboardOption == 'settings'" class="settings">
        <button v-on:click="deleteBankingData" class="montserrat" :disabled="! userName">{{ BankButtonText }}</button>
        <button v-on:click="adminCheck" class="montserrat" :disabled="! userName">Admin Panel!</button>
        <button v-on:click="deleteButton" class="montserrat" :disabled="! userName">{{ deleteText }}</button>
      </div>

      <div v-else>
        <h1>Your Selection Has Been Lost, Please Try Again!</h1>
      </div>
    </div>
  </main>
</template>


<script>
  import { ref , watch } from 'vue'
  import { useRouter } from "vue-router";
  
  export default {
    name: "Dashboard",
    props: {
      'userName' : String,
      'dashboardOption' : String
    },
    setup(props, {emit}) {
      const deleteText = ref("Delete Account!")
      const router = useRouter()
      
      var deleteCount = -1

      // Delete account button in settings //
      async function deleteButton() {
        var messages = ["Are You sure?", "Are you REALLY sure?"]

        deleteCount += 1

        console.log("Works")

        if (deleteCount < 2) {
          deleteText.value = messages[deleteCount]
        } else {
          let request = await fetch("http://127.0.0.1:5001/deleteaccount", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              username: props.userName,
              })
          })

          var response = await request.json()

          deleteText.value = "Goodbye!"

          if (response['Status'] == false) {
            deleteText.value = "Failed!"
            alert(response['message'])
          } else {
            console.log(response["Status"])
            console.log(response["message"])
            await new Promise(resolve => setTimeout(resolve, 1000));

            emit("logOut")
            router.push("/login")
          }
        }
      }
      // End of delete account button //

      // Delete Booking Button //
      const BookingType = ref("")
      const BookingId = ref(0)
      
      async function deleteBooking() {
        let request = await fetch("http://127.0.0.1:5001/cancel", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            Username: props.userName,
            BookingType : BookingType.value,
            BookingId : BookingId.value
          })
        })
        
        console.log(request)
      }
      // End of delete booking button //

      // Get the bookings //
      const HotelBookings = ref("")
      const ZooBookings = ref("")
      async function GetBookings() {
        let request = await fetch("http://127.0.0.1:5001/checkbookings", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        UserName : props.userName,
      })
      })
      request = await request.json()
      HotelBookings.value = request["hotel"]
      ZooBookings.value = request["zoo"]
      }
      
      // End of getting bookings //

      // This runs if rendered page is bookings //
      watch(() => props.dashboardOption, (NewValue) => {
        if (NewValue === 'bookings') {
          console.log("Get Bookings");
          GetBookings()
        }
        else {
          console.log("No fetch :(");
        }
      }, { immediate : true })

      // Delete Bank Details //
      const BankButtonText = ref("Delete Banking Data")
      async function deleteBankingData() {
        let request = await fetch("http://127.0.0.1:5001/deletebankdetails", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            UserName : props.userName,
          })
          })
          request = await request.json()

          console.log(request)
          
          BankButtonText.value = request["message"]
        }

      async function adminCheck() {
        router.push('/admin')
      }

      return {deleteText, BookingId, BookingType, HotelBookings, ZooBookings, BankButtonText, deleteButton, deleteBankingData, adminCheck, deleteBooking}
    }
  }
</script>