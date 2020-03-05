<template>
  <div>
    <div> Create a new workout? </div>
    <input v-model='name' placeholder='name'/>
    <input v-model='duration' placeholder='duration'/>
    <input v-model='workout_at' placeholder='time'/>
  </div>
</template>



<script>
export default {
  name: 'CreateWorkoutForm',
  data: function() {
    return {
      name: '',
      duration: null,
      workout_at: null,
    }
  }
}
</script>

<style scoped>
input {
  margin: 10px;
}
</style>
