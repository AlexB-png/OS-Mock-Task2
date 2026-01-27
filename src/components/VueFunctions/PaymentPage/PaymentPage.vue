<style scoped src="./Modules/PaymentPageScoped.css"></style>

<style src="./Modules/PaymentPage.css"></style>

<template >
  <main>
  <div class="content">
    <div v-if="bookingType">
      <div class="visitor" v-if="bookingType == 'visitor' | bookingType == 'member'">
        Welcome {{ bookingType }}!
      </div>

      <button v-on:click="button">CLICK!</button>
    </div>

    <div v-else>
      <h1>Your Selection Has Been Lost, Please Reinput Your Booking Type</h1>
    </div>
  </div>
</main>
</template>

<script src="./Modules/PaymentPage.js"></script>