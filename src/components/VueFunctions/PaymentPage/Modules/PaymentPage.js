import { ref , watch , onMounted} from 'vue'


export default {
  name: 'LoginPage',
  props: {
    'userName': String,
    'bookingType': String,
    'totalPrice': Number
  },
  setup(props, { emit }) {    
    const adult = ref(0);
    const child = ref(0)
    const date = ref("")
    const membershipNum = ref(0)

    // Only used in education booking
    const school = ref("");
    //

    // Remove variable when mounted
    onMounted(() => {
      emit("updatePrice", NaN)
    })

    watch([adult, child, date], () => {
      console.log("Change Detected!")

      if (adult.value && child.value && date.value) {
        if (props.bookingType == "student") {
          emit("updatePrice", (adult.value * 15 + child.value * 5))
        } else if (props.bookingType == "visitor") {
          emit("updatePrice", (adult.value * 20 + child.value * 5))
        } else {
          emit("updatePrice", 0)
        }
      } else {
        emit("updatePrice", NaN)
      }
    })
    
    async function button() {
      let request = await fetch("http://127.0.0.1:5001/test", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
      })
      console.log(request)
    }

    return {button,adult,child,date,membershipNum,school}
}
}