<template>
<div class="row px-md-5 px-3">
    <div class="col-12">
        <div v-if="showRegularForm" id="regular-form">
            <RegularForm @hide-form="toggle"/>
        </div>

        <div v-else id="advanced-form">
             <AdvancedForm  @hide-form="toggle"/>
        </div>
    </div>
</div>
</template>

<script>
import RegularForm from "./RegularForm.vue";
import AdvancedForm from "./AdvancedForm.vue";

export default {
    name: "Form",

    data(){
      return{
          showRegularForm: true
      }
    },

    components: {
        RegularForm,
        AdvancedForm
    },

    methods: {
        toggle(){
            this.showRegularForm = !this.showRegularForm
        }
    },
}
</script>

<style scoped>

</style>
