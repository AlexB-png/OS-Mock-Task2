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
    
    const button = () => {
      console.log(adult.value, child.value, date.value, membershipNum.value)
    }

    return {button,adult,child,date,membershipNum}
}
}