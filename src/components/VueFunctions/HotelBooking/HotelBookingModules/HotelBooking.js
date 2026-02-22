import { ref , watch } from 'vue'
import { useRouter } from "vue-router";

export default {
  name: "Booking",
  props: {
    'userName': String,
    'totalPrice': Number,
  },
  setup(props, { emit }) {
    // Variables
    const guests = ref(0);
    const single = ref(0);
    const double = ref(0);
    const startDate = ref("");
    const endDate = ref("");
    const errorMessage = ref("");
    const router = useRouter();
    const buttonDisabled = ref(true);
    //

    // This controls the button that sends you to payment page //
    const paymentButton = ref(true)
    //

    // When these variables change it will be executed
    watch([guests, single, double, startDate, endDate], () => {
      // Single Beds = 1 Guest && Double Beds = 2 Guests
      var slots_in_use = 0;
      slots_in_use = (1 * single.value) + (2 * double.value);
      //
      
      // Just check that everything has had an input EXCEPT only one of double or single has to be done
      if (guests.value > 0 && ((single.value >= 0) && (double.value >= 0)) && startDate.value != "" && endDate.value != "") {
        // if there are more guests that amount of "Bed Points"
        if (guests.value > slots_in_use) {
          errorMessage.value = "You don't have enough beds to fit everyone!";
          buttonDisabled.value = true;
          emit("updatePrice", NaN);
        // else calculate the price
        } else {
          // Clear error message
          errorMessage.value = "";
          //
          
          // Get the total cost of the room
          var newTotal = ((guests.value * 25) + (single.value*25) + (double.value*50));
          //

          // Calculate Days Between Dates Selected
          const dateStart = new Date(startDate.value);
          const dateEnd = new Date(endDate.value);

          const date1 = new Date(dateStart);
          const date2 = new Date(dateEnd);

          const diffTime = Math.abs(date2 - date1);
          const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
          //

          // Multiply day cost by amount of days
          newTotal = newTotal * diffDays;
          //

          if (date1 > date2) {
            buttonDisabled.value = true;
            errorMessage.value = "Your Dates Are In The Wrong Order!"
          } else if (newTotal != 0) {
            emit("updatePrice", newTotal)
            console.log(guests.value)
            buttonDisabled.value = false;
          } else {
            buttonDisabled.value = true;
          }
        }
        //
      
      } else {
        emit("updatePrice", NaN);
        buttonDisabled.value = true;
      }
      //
    })
    //

  async function ButtonPress() {
    let username = props.userName;
    let start = startDate.value;
    let end = endDate.value;

    let guestCount = guests.value;
    let singleBed = single.value;
    let doubleBed = double.value;

    console.log(guests.value)

    let request = await fetch("http://127.0.0.1:5001/hotelbooking", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user: username,
        start: start,
        end: end,
        guests: guestCount,
        singles: singleBed,
        doubles: doubleBed,
        totalPrice: props.totalPrice
      })
    })

    request = await request.json()

    var RoomNum = request["rowid"]
    var statusBool = request["Success"]
    var StatusMessage = request["Status"]

    errorMessage.value = (StatusMessage) + ("<br>") + ("Room Num: ") + (RoomNum)
    paymentButton.value = !statusBool
    emit("updateBookingRoomId", RoomNum)
    emit("updateBookingType", "hotel")
  }

  function PaymentTime() {
    router.push("/payment")
  }
  
  return { guests , single , double , startDate , endDate , errorMessage, buttonDisabled , paymentButton , ButtonPress, PaymentTime};
}
}