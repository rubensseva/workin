<template>
  <div>
    <div> Create a new workout? </div>
    <li v-for='workout in workouts' :key='workout.id'>
      {{ workout.name }}
    </li>
  </div>
</template>

<script>
export default {
  name: 'ViewUserWorkouts',
  data: function() {
    return {
      workouts: this.$store.state.workouts
    }
  }
}
</script>
