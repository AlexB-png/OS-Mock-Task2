import { useRouter } from "vue-router";

export default {
  name: 'LoginPage',
  props: {

  },
  setup(props, { emit }) {
    const router = useRouter();
    
    function buttonPress() {
      emit("updateBookingType", event.target.id)
      router.push("/zoobookingpage")
    }
    
    return {buttonPress}
}
}