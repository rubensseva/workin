<template>
  <div class='container'>
    <div> Workout details </div>
    <div class='workoutDetailsContainer workoutContainer'>
      <div>
        <div> Id: </div>
        <div> {{ workout.id }} </div>
      </div>
      <div>
        <div> Name: </div>  
        <div> {{ workout.name }} </div> 
      </div>
      <div>
        <div> Created: </div>
        <div> {{ workout.created }} </div> 
      </div>
      <div> 
        <div> Time of workout: </div> 
        <div> {{ workout.workout_at }} </div> 
      </div>
      <div> 
        <div> Duration: </div>
        <div> {{ workout.workout_duration }} </div> 
      </div>
      <div> 
        <div> Type: </div>
        <div> {{ workout.workout_type }} </div>
      </div>
      <div>
        Exercises in this workout:
      </div>
    </div>
    <div class='workoutEntriesContainer workoutContainer'>
      <li v-for='workout_entry in workout.workout_entries' :key='workout_entry.id'>
        {{ workout_entry.entry_type }} | {{ workout_entry.amount_per_set }} | {{ workout_entry.num_sets }}
      </li>
    </div>
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

.container {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}

.workoutContainer {
  width: 60%;
}

.workoutDetailsContainer {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  width: 60%;
  padding: 20px 0px 20px 0px;
}

.workoutDetailsContainer > div:not(last-of-type) {
  border-bottom: 1px solid rgba(50, 50, 50, .2);
}

.workoutDetailsContainer > div:last-of-type {
  margin-bottom: 50px;
}

.workoutDetailsContainer > div {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  margin: 10px 0 0 0;
  padding: 10px 0 0 0;
}

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
