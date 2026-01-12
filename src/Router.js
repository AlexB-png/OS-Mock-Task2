import LoginPage from './components/VueFunctions/LoginPage.vue'
import { createWebHistory, createRouter } from 'vue-router'
import Homepage from './components/VueFunctions/Homepage.vue'
import Booking from './components/VueFunctions/HotelBooking.vue'

const routes = [
  { path: '/login', component: LoginPage },
  { path: '/', component: Homepage},
  { path: '/hotelbooking', component: Booking}
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
