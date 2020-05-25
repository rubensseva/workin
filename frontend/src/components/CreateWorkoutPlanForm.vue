<template>
  <form class='container' @submit='createWorkoutSubmit'>
    <div> Create a new workout plan? </div>
    <input required type=text v-model='name' placeholder='name'/>
    <input required type=number v-model='weekDayStart' placeholder='week day start'/>
    <input
      class='primaryButton'
      type='submit'
      value='Create workout plan'
    >
  </form>
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
