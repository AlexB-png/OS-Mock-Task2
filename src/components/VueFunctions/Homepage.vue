<style>
  html, body {
    margin: 0;
    padding: 0;
    scrollbar-gutter: stable;
    font-size: 1vw
  }
</style>

<style scoped>
  main {
    background-image: none;
  }

    .content {
      background-color: rgba(265, 247, 239);
      
      padding-top: 10vh;
      
      width: 100%;

      display: flex;
      flex-direction: column;
      gap: 3vh;

      

      align-items: center;
      justify-content: center;

      .row1, .row2, .row3 {
        display: flex;
        flex-direction: row;
        gap: 3vw;

        @media (max-width: 1024px) {
          flex-direction: column;
        }
      }

      .row {
        display: flex;
        flex-direction: row;
      }

      .hotel, .zoo {
        height: clamp(0px,80vw,600px);
        width: 35vw;
        background-color: #A8BBA3;

        color: rgb(91, 108, 62);
        border-radius: 20px;

        backdrop-filter: blur(4px);

        display: flex;
        justify-content: center;
        align-items: center;

        flex-direction: column;

        @media (max-width: 1024px) {
          width: 60vw;
        }
      }

      .hotelImg {
        width: 30vw;
        border-radius: 10px;

        @media (max-width: 1024px) {
          width: 40vw;
        }
      }

      .hotelText, .zooText {
        padding-left: 2vw;
        padding-right: 2vw;
        text-align: center;

        font-size: 1.5rem;

        @media (max-width: 1024px) {
          font-size: 3rem;
        }
      }

      .hotelLink {
        padding-bottom: 2.5vh;
        font-size: 2rem;
      }

      .zooImage {
        width: 25vw;
        border-radius: 10px;

        @media (max-width: 1024px) {
          width: 35vw;
        }
      }

      .zooTextDiv {
        padding-bottom: 4vh;
      }

      .hugeGiraffeImage {
        width: 100%;
        padding-top: 10vh;
      }

      .hotelEvent, .zooEvent {
        height: clamp(0px,80vw,600px);;
        width: 35vw;
        background-color: #B87C4C;
        
        border-radius: 20px;

        backdrop-filter: blur(4px);

        display: flex;
        justify-content: center;
        align-items: center;

        flex-direction: column;

        @media (max-width: 1024px) {
          width: 60vw;
        }

        h2 {
          font-size: 1.5rem;
          color: rgb(154, 74, 16);

          @media (max-width: 1024px) {
            font-size: 2.5rem;
          }
        }

        h1 {
          color: rgb(124, 74, 16);
          font-size: 3rem;

          @media (max-width: 1024px) {
            font-size: 5.5rem;
          }
        }
      }

      .row3 {
        background-color: #A8BBA3;
        width: 73vw;
        height: clamp(0px,60vw,600px);
        border-radius: 20px;

        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        text-align: center;
        

        h1 {
          color: #437057;

          @media (max-width: 1024px) {
            font-size: 5.5rem;
          }
        }

        p {
          font-size: 2rem;

          color: rgb(91, 108, 62);

          @media (max-width: 1024px) {
            font-size: 3rem;
          }
        }

        .row3Text {
          padding-left: 2vw;
          padding-right: 2vw;
        }
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

    <div class="row2">
      <div class="hotelEvent">
        <h1 style="text-decoration: underline; padding-bottom: 5vh; font-size: 3rem;" class="montserrat">Hotel Events</h1>
        <h2 class="montserrat">6 Am - 12 Pm  -  Breakfast</h2>
        <h2 class="montserrat">12 Pm - Bar Opens</h2>
        <h2 class="montserrat">12 Pm - 1 Pm - Lunch</h2>
        <h2 class="montserrat">1 Pm - 6 Pm - Dinner</h2>
        <h2 class="montserrat">7 Pm - Party Rooms Open</h2>
        <h2 class="montserrat">2 Am - Final drinks</h2>
      </div>

      <div class="zooEvent">
        <h1 style="text-decoration: underline; padding-bottom: 5vh;" class="montserrat">Zoo Events</h1>
        <h2 class="montserrat">January 17th - Bird Watching</h2>
        <h2 class="montserrat">January 23rd - Tractor Ride</h2>
        <h2 class="montserrat">January 31st - Honey Tasting</h2>
        <h2 class="montserrat">February 5th - 24 hour open</h2>
        <h2 class="montserrat">February 11th - Bear Woods Opens</h2>
      </div>
    </div>

    <div class="row3">
      <div class="row3Text">
        <h1 style="text-decoration: underline;" class='montserrat'>Educational Trips</h1>
        <p class="montserrat">We also offer educational trips for large school groups (8+ students) with extra views of all of our animals, extra interactions with the animals and an experienced and educated professional to educate students about the animals diets and the way they act both in containment and in the wild.</p>
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