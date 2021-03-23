<template>
  <div class="my-footer text-center">
    <div class="row m-4">
      <div class="col-12">
        <small>
            <a href="https://github.com/Nyior/clipit" target="_blank">
                <i
                    class="fa fa-github m-0 p-0"
                    aria-hidden="true"
                >
               contribute to clipit on Github
               </i>
            </a>
        </small>
        <hr>
        <small>
            <a href="https://www.nyior.tech/" target="_blank">
                <i class="fa fa-heart-o" aria-hidden="true">
                    made by Nyior Clement :)
                </i>
            </a>
        </small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.my-footer {
  font-weight: bold;
  letter-spacing: 1px;
  width: 100%;
  margin-top: 2rem;
  position: relative;
  bottom: 0px;
}

</style>
