<style scoped src="./Modules/PaymentPageScoped.css"></style>

<style src="./Modules/PaymentPage.css"></style>

<template >
  <main>
  <div class="content">
    <div v-if="bookingType">
      <div class="visitor" v-if="bookingType == 'visitor' | bookingType == 'member'">
        <h1 class="welcome">Welcome {{ bookingType }}!</h1>
        
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
          <input type="number" v-model="membershipNum">
        </div>

        <button v-on:click="button" class="montserrat" :disabled="!(adult && date) | !userName">Click Me!</button>

        <h1 class="monstserrat">Total Cost: {{ totalPrice }}</h1>
      
        <h1 v-if="!userName" style="color: var(--red);">You Are Not Logged In!</h1>

        <div class="status">
          <h1>{{ statusText }}</h1>
        </div>
      </div>

      <div class="education" v-else>
        <h1 class="title">Education Bookings!</h1>
        
        <div class="row">
          <div class="text">
            <h1 class="montserrat">Teachers:</h1>
          </div>
          <input type="number" v-model="adult">
        </div>

        <div class="row">
          <div class="text">
            <h1 class="montserrat">Students:</h1>
          </div>
          <input type="number" v-model="child">
        </div>

        <div class="row">
          <div class="text">
            <h1 class="montserrat">School Name:</h1>
          </div>
          <input type="text" v-model="school" placeholder="Input School Name">
        </div>

        <div class="row">
          <div class="text">
            <h1 class="montserrat">Date:</h1>
          </div>
          <input type="date" v-model="date">
        </div>

        <button v-on:click="button" :disabled="!(userName && adult && child && date)" class="montserrat">Submit!</button>

        <h1 class="monstserrat">Total Cost: {{ totalPrice }}</h1>

        <h1 v-if="!userName" style="color: var(--red);">You Are Not Logged In!</h1>

        <div class="status">
          <h1>{{ statusText }}</h1>
        </div>
      </div>
    </div>

    <div v-else>
      <h1>Your Selection Has Been Lost, Please Reinput Your Booking Type</h1>
    </div>
  </div>
</main>
</template>

<script src="./Modules/PaymentPage.js"></script>