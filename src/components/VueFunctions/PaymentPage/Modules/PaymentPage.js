export default {
  name: 'LoginPage',
  props: {
    'userName': String,
    'bookingType': String,
  },
  setup(props, { emit }) {    
    const button = () => {
      console.log(props.bookingType)
    }

    return {button}
}
}