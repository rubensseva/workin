<template>
  <div class='container'>
    <div> Create a new workout? </div>
    <input v-model='name' placeholder='name'/>
    <input v-model='workoutType' placeholder='workoutType'/>
    <input v-model='duration' placeholder='duration'/>
    <input type='datetime-local' v-model='workoutAt'/>
    <button class='primaryButton' v-on:click='createWorkoutSubmit'>Create workout</button>
  </div>
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
