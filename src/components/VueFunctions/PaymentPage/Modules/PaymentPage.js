import { ref } from 'vue'


export default {
  name: 'LoginPage',
  props: {
    'userName': String,
    'bookingType': String,
  },
  setup(props, { emit }) {    
    const adult = ref(0);
    const child = ref(0)
    const date = ref("")
    const membershipNum = ref(0)

    // Only used in education booking
    const school = ref("")
    //
    
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