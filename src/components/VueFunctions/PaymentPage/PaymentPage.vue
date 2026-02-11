<style scoped>
  body {
    height: 100vh;
    width: 100vw;
  }
  
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    
    background-color: var(--green);
    height: 100%;

    .content {
      height: 75%;
      width: 50%;

      display: flex;
      justify-content: center;
      align-items: center;

      background-color: var(--green-light);
      border-radius: 20px;

      .row {
        display: flex;
        flex-direction: row;
        width: 90%;

        justify-content: space-evenly;
        align-items: center;
        
        * {
          width: 35%;
        }

        input {
          height: 2vw;
          font-size: 2rem;
        }

        h1 {
          font-size: 2rem;
        }
      }
    }
  }
</style>


<template>
  
  <body>
    <main>
      <div class="content">
        <div class="row">
          <h1>Hello from row!</h1>
          <input type="text">
        </div>
      </div>
    </main>
  </body>

</template>


<script>

</script>