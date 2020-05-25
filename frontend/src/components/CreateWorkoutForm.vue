<template>
  <form class='container' @submit='createWorkoutSubmit'>
    <div> Create a new workout? </div>
    <input required type=text v-model='name' placeholder='name'/>
    <input required type=text v-model='workoutType' placeholder='workoutType'/>
    <input required type=number v-model='duration' placeholder='duration'/>
    <input required pattern='/\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z)/' type='datetime-local' v-model='workoutAt'/>
    <input
      class='primaryButton'
      type='submit'
      value='Submit'
    >
  </form>
</template>



<script>
export default {
  name: 'CreateWorkoutForm',
  data: function() {
    return {
      name: '',
      workoutType: '',
      duration: null,
      workoutAt: null,
    }
  },
  methods: {
    createWorkoutSubmit() {
      console.log(this.workoutAt);
      this.$store.dispatch('createWorkout', { 
        name: this.name, 
        workoutType: this.workoutType,
        duration: this.duration,
        workoutAt: this.workoutAt,
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
