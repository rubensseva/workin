<template>
  <div class='container'>
    <div> Create a new workout plan? </div>
    <input v-model='name' placeholder='name'/>
    <input v-model='weekDayStart' placeholder='week day start'/>
    <button class='primaryButton' v-on:click='createWorkoutSubmit'>Create workout plan</button>
  </div>
</template>



<script>
export default {
  name: 'CreateWorkoutForm',
  data: function() {
    return {
      name: '',
      weekDayStart: '',
    }
  },
  methods: {
    createWorkoutSubmit() {
      console.log(this.name, this.weekDayStart);
      this.$store.dispatch('createWorkoutPlan', { 
        name: this.name, 
        weekDayStart: this.weekDayStart,
      })
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}
input {
  margin: 10px;
}
</style>
