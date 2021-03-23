<template>
  <div class="loader">
    <div class="loading_1"></div>
    <div class="loading_2">...loading...</div>
  </div>
</template>

<style scoped>
.loader {
  width: 50%;
  margin: 150px auto 70px;
  position: relative;
}

.loader .loading_1 {
  position: relative;
  width: 100%;
  height: 10px;
  border: 1px solid #e9492e;
  border-radius: 10px;
  animation: turn 4s linear 1.75s infinite;
}

.loader .loading_1:before {
  content: "";
  display: block;
  position: absolute;
  width: 0;
  height: 100%;
  background-color: #e9492e;
  animation: load 2s linear infinite;
}

.loader .loading_2 {
  position: absolute;
  width: 100%;
  top: 10px;
  color: #e9492e;
  font-size: 22px;
  text-align: center;
  animation: bounce 2s linear infinite;
}

@keyframes load {
  0% {
    width: 0%;
  }

  87.5% {
    width: 100%;
  }
}

@keyframes turn {
  0% {
    transform: rotateY(0deg);
  }

  6.25%,
  50% {
    transform: rotateY(180deg);
  }

  56.25%,
  100% {
    transform: rotateY(360deg);
  }
}

@keyframes bounce {
  0%,
  100% {
    top: 10px;
  }

  12.5% {
    top: 30px;
  }
}
</style>

<script>
export default {
  name: "loader"
};
</script>
