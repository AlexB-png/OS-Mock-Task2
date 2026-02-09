import LoginPage from './components/VueFunctions/LoginPage/LoginPage.vue'
import { createWebHistory, createRouter } from 'vue-router'
import Homepage from './components/VueFunctions/HomePage/HomePage.vue'
import Booking from './components/VueFunctions/HotelBooking/HotelBooking.vue'
import ZooBooking from './components/VueFunctions/ZooBooking/ZooBooking.vue'
import PaymentPage from './components/VueFunctions/ZooPayment/PaymentPage.vue'

const routes = [
  { path: '/login', component: LoginPage },
  { path: '/', component: Homepage},
  { path: '/hotelbooking', component: Booking},
  { path: '/zoobooking', component: ZooBooking},
  { path: '/payment', component: PaymentPage}
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
