<template>
  <div class='container'>
    <h1> Workout page </h1>
    <div class='workouts-container'>
      <CreateWorkoutForm class='workout-form'/>
      <ViewWorkouts class='view-workouts' v-bind:workouts='this.$store.state.user.user.workouts'/>
    </div>
  </div>
</template>


<script>

import CreateWorkoutForm from '@/components/CreateWorkoutForm.vue'
import ViewWorkouts from '@/components/ViewWorkouts.vue'

export default {
  name: 'Workouts',
  components: {
    CreateWorkoutForm,
    ViewWorkouts,
  },
  data: function() {
    return {
      workouts: []
    }
  },
  mounted() { 
    if (!this.$store.state.user.isAuthenticated) {
      this.$store.dispatch('tokenLogin')
        .then(() => {
          if (!this.$store.state.user.isAuthenticated) {
            alert('You need to log in to view the workouts page');
            this.$router.push('login');
          }
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
}

.workouts-container {
  display: flex;
  justify-content: space-between;
}
.workout-form {
  flex-grow: 1;
  margin: 10px;
}
.view-workouts {
  flex-grow: 3;
  margin: 10px;
}
</style>
