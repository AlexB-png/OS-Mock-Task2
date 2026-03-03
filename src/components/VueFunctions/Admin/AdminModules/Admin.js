  import { onMounted } from 'vue';
  import { useRouter } from "vue-router";
  import { ref } from 'vue';

  export default {
    props: {
      userName : String
    },
    setup(props) {
      const router = useRouter()
      const adminStatus = ref(false)
      
      onMounted(() => {
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
      const CancelOption = ref("")
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
            BookingType : CancelOption.value,
            BookingId : HotelCancelId.value
          })
        })

        StatusMessage.value = (await request.json())["message"]
      }

      return { checkAdmin , adminStatus , HotelDeleteBooking, HotelCancelUser , HotelCancelId , StatusMessage , CancelOption}
    }
  }