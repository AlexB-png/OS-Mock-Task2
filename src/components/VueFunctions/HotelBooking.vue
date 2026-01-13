<style>
  :root {
    --green : #A8BBA3;
    --white : #F7F4EA;
    --pink : #EBD9D1;
    --orange : #B87C4C;

    --green-light : rgb(208, 227, 203);

    --green-text : rgb(108, 127, 103);
  }
</style>

<style scoped>
  body {
    height: 100vh;
    background-color: var(--green);

    display: flex;
    justify-content: center;
    align-items: center;

    .content {
      display: flex;
      justify-content: center;
      align-items: center;
      
      .box {
        height: 80vh;
        width: 80vw;

        display: flex;
        justify-content: center;

        flex-direction: column;
        
        background-color: var(--green-light);
        border-radius: 20px;

        .helloStatus {
          height: 5vh;
        }

        .selections {
          height: 75vh;
        }
      }
    }
  }
</style>

<template>
  <body>
    <div class="content">
      <div class="box">
        <div class="helloStatus">
          <h1 v-if="userName" style="color: var(--green-text);">Welcome {{ userName }}!</h1>
          <h1 v-else>You are not logged in!</h1>
        </div>

        <div class="selctions">
          <h1>1</h1>
          <h1>2</h1>
          <h1>3</h1>
          <h1>4</h1>
          <h1>5</h1>
          <h1>6</h1>
          <h1>7</h1>
          <h1>8</h1>
          <h1>9</h1>
          <h1>10</h1>
          
        </div>
      </div>
    </div>
  </body>
</template>

<script>
  export default {
    name: "Booking",
    props: {
      'userName': String,
    },
    setup(props) {
  }};
</script>