<style scoped src="./Modules/PaymentPageScoped.css"></style>

<style src="./Modules/PaymentPage.css"></style>

<template >
  <main>
  <div class="content">
    <div v-if="bookingType">
      <div class="visitor" v-if="bookingType == 'visitor' | bookingType == 'member'">
        <h1>Welcome {{ bookingType }}!</h1>
        
        <div class="row">
          <div class="text">
            <h1>Adults:</h1>
          </div>
          <input type="number" v-model="adult">
        </div>

        <div class="row">
          <div class="text">
            <h1>Children:</h1>
          </div>
          <input type="number" v-model="child">
        </div>

        <div class="row">
          <div class="text">
            <h1>Date:</h1>
          </div>
          <input type="date" v-model="date">
        </div>

        <div class="row" v-if="bookingType == 'member'">
          <div class="text">
            <h1>Input Membership Number:</h1>
          </div>
          <input type="number">
        </div>

        <button v-on:click="button" class="montserrat" :disabled="!(adult && date)">Click Me!</button>
      </div>

      <div class="education" v-else>
        <button v-on:click="button" class="montserrat">Click me!</button>
      </div>

      <h1></h1>

      
    </div>

    <div v-else>
      <h1>Your Selection Has Been Lost, Please Reinput Your Booking Type</h1>
    </div>
  </div>
</main>
</template>

<script src="./Modules/PaymentPage.js"></script>