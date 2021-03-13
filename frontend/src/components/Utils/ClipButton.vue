<template>
  
    <button 
        type="submit" 
        class="clip-button btn-block shadow text-center"
        :class="{ 'is-loading': isLoading }"
    >
        <div class="text">
            <i 
            class="fa fa-scissors" 
            aria-hidden="true" 
            >
            </i> 
            clip
        </div>

        <div class="loading-icon mr-5">
            <i 
                class="fa fa-spinner fa-spin" 
                aria-hidden="true">
            </i>
        </div>
    </button>
       
</template>

<style scoped>

.clip-button {
    background-color:#e9492e;
	color: white !important;
	font-weight: bold;
	font-size: 2rem;
    color: white;
    border: none;
    cursor: pointer;
}

button > .text {
    will-change: transform, opacity;
    transition: all 0.3s ease-in-out;
    opacity: 1;
    border: none;
}
button > .loading-icon {
    position: absolute;
    left: 0;
    right: 0;
    transition: all 0.3s ease-in-out;
    will-change: transform, opacity;
    opacity: 0;
}
button.is-loading > .text {
    transform: translateY(-100px);
    opacity: 0;
    border: none;
}
button.is-loading > .loading-icon {
    transform: translateY(-100%);
    opacity: 1;
}

</style>

<script>
export default {
  name: "ClipButton",

  props: {
      isLoading: {
          type: Boolean,
          required: true,
      }
  }

}
</script>

