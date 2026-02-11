import LoginPage from './components/VueFunctions/LoginPage/LoginPage.vue'
import { createWebHistory, createRouter } from 'vue-router'
import Homepage from './components/VueFunctions/HomePage/HomePage.vue'
import Booking from './components/VueFunctions/HotelBooking/HotelBooking.vue'
import ZooBookingAll from './components/VueFunctions/ZooBooking/ZooBookingAll.vue'
import ZooBookingPage from './components/VueFunctions/ZooPayment/ZooBookingPage.vue'
import Dashboard from './components/VueFunctions/Dashboard/Dashboard.vue'
import PaymentPage from './components/VueFunctions/PaymentPage/PaymentPage.vue'

const routes = [
  { path: '/login', component: LoginPage },
  { path: '/', component: Homepage},
  { path: '/hotelbooking', component: Booking},
  { path: '/zoobooking', component: ZooBookingAll},
  { path: '/zoobookingpage', component: ZooBookingPage},
  { path: '/dashboard', component: Dashboard},
  { path: '/payment', component: PaymentPage}
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
