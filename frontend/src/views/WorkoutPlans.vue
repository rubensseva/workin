<template>
  <div class='container'>
    <div class='workoutPlansContainer'>
      <div> Workout plans </div>
      <CreateWorkoutPlanForm/>
      <ViewWorkoutPlans v-bind:workoutPlans='this.$store.state.user.user.workout_plans'/>
    </div>
  </div>
</template>


<script>
import CreateWorkoutPlanForm from '@/components/CreateWorkoutPlanForm.vue'
import ViewWorkoutPlans from '@/components/ViewWorkoutPlans.vue'

export default {
  name: 'WorkoutDetails',
  components: {
    CreateWorkoutPlanForm,
    ViewWorkoutPlans
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
  },
  methods: {
    createWorkoutPlan() {
      this.$store.dispatch('createWorkoutPlan')
    }
  }
}
</script>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.workoutPlansContainer {
  width: 70%;
}

</style>
