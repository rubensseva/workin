<template>
  <div>
    <div> Workout details </div>
    <div>
      {{ workout.id }} | {{ workout.name }} | {{ workout.created }} | {{ workout.workout_at }} | {{ workout.workout_duration }} | {{ workout.workout_type }}
    </div>
    <li v-for='workout_entry in workout.workout_entries' :key='workout_entry.id'>
      {{ workout_entry.id }} | {{ workout_entry.entry_type }} | {{ workout_entry.amount_per_set }} | {{ workout_entry.num_sets }}
    </li>
    
  </div>
</template>


<script>
export default {
  name: 'WorkoutDetails',
  data: function() {
    return {
      workout: {}
    }
  },
  mounted() {
    console.log(this.$route.params)
    console.log(this.$store.state.user.user.workouts)
    if (!this.$store.state.user.isAuthenticated) {
      alert('Error when attempting to parse workout id url param as int')
      this.$router.push('login')
    }
    let workoutId = parseInt(this.$route.params.id);
    if (!workoutId) {
      alert('Error when attempting to parse workout id url param as int')
      this.$router.push('/')
    }
    let allWorkouts = this.$store.state.user.user.workouts;
    let workout = allWorkouts.filter(workout => workout.id === workoutId)[0]
    this.workout = workout
  }
}
</script>

<style scoped>

li {
  list-style-type: none;
  font: 150 15px/1.5 Helvetica, Verdana, sans-serif;
  border-bottom: 1px solid #ccc;
  transition: 0.5s;
  background-color: rgba(230, 230, 250, 0.5);
  padding: 4px 0px 0px 0px;
  width: 100%
}
 
li:last-child {
  border: none;
}

li:hover {
  background-color: rgba(230, 230, 250, 1);
}

</style>
