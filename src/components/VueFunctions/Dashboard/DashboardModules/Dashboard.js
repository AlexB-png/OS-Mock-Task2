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
            await new Promise(resolve => setTimeout(resolve, 1000));

            emit("logOut")
            router.push("/login")
          }
        }
      }
      // End of delete account button //

      // Delete Booking Button //
      const BookingStatus = ref("")
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
        
        request = await request.json()
        BookingStatus.value = request['message']
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

      // Get Loyalty Points //
      const LoyaltyPoints = ref("")
      async function GetLoyalty() {
        let request = await fetch("http://127.0.0.1:5001/checkloyalty", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            Username : props.userName,
          })
        })

        request = await request.json()
        LoyaltyPoints.value = request[0]
      }

      // This runs if rendered page is bookings //
      watch(() => props.dashboardOption, (NewValue) => {
        if (NewValue === 'bookings') {
          GetBookings()
          GetLoyalty()
        }
      }, { immediate : true })


      async function adminCheck() {
        router.push('/admin')
      }

      return {deleteText, BookingId, BookingType, HotelBookings, ZooBookings, BookingStatus, LoyaltyPoints, GetLoyalty, deleteButton, adminCheck, deleteBooking}
    }
  }