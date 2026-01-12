<style>
  html, body {
    margin: 0;
    padding: 0;
    scrollbar-gutter: stable;
    font-size: clamp(5px,2vw,13px);
  }
</style>

<style scoped>
  main {
    background-image: none;
  }

    .content {
      background-color: rgb(180, 255, 242);
      
      padding-top: 10vh;
      
      width: 100%;

      display: flex;
      flex-direction: column;
      gap: 3vh;

      align-items: center;
      justify-content: center;

      .row1, .row2 {
        display: flex;
        flex-direction: row;
        gap: 3vw;
      }

      .row {
        display: flex;
        flex-direction: row;
      }

      .hotel, .zoo {
        height: 80vh;
        width: 35vw;
        background-color: coral;
        border-radius: 20px;

        backdrop-filter: blur(4px);

        display: flex;
        justify-content: center;
        align-items: center;

        flex-direction: column;
      }

      .hotelImg {
        width: 30vw;
        border-radius: 10px;
      }

      .hotelText, .zooText {
        padding-left: 2vw;
        padding-right: 2vw;
        text-align: center;

        font-size: 2rem;
      }

      .hotelLink {
        padding-bottom: 2.5vh;
        font-size: 2rem;
      }

      .zooImage {
        width: 25vw;
        border-radius: 10px;
      }

      .zooTextDiv {
        padding-bottom: 4vh;
      }

      .hugeGiraffeImage {
        width: 100%;
        padding-top: 10vh;
      }

      
  }
</style>

<template>
  <div class="content">
    <div class="row1">
      <div class="hotel">
        <p class="hotelText montserrat">
          You can book a stay at the Ridget Zoo Adventures hotel for a very reasonable price, with included view of the entire zoo and the animals from the balcony as well as an included 24/7 pass to the zoo as well as an included animal feeding opportunity, and free breakfast from 6-9 AM.
        </p>
        <img class="hotelImg" src="../../assets/hotelRoom.avif" alt="Hotel">
      </div>
      
      <div class="zoo">
        <div class="zooTextDiv">
          <p class="zooText montserrat">
            If you come and visit our zoo then you can meet a wide variety of animals! This ranges from animals like lions and tigers and bears to even smaller animals like hedgehogs and creepy crawlies like tarantulas!
          </p>
        </div>
        <img src="../../assets/redPanda.jpg" alt="Red Panda" class="zooImage">
      </div>
    </div>

    <img src="../../assets/giraffe.jpg" alt="Giraffe" class="hugeGiraffeImage">
  </div> 
</template>

<script>
  export default {
    name: "HomePage"
  }
</script>