<template>
  <div>
    <div> This is the workout page </div>
    <CreateWorkoutForm/>
    <ViewUserWorkouts/>
  </div>
</template>


<script>
import CreateWorkoutForm from '@/components/CreateWorkoutForm.vue'
import ViewUserWorkouts from '@/components/ViewUserWorkouts.vue'

export default {
  name: 'Workouts',
  components: {
    CreateWorkoutForm,
    ViewUserWorkouts,
  },
  data: function() {
    return {
      workouts: []
    }
  },
  mounted() { 
    /* if (!this.$store.state.user.isAuthenticated) { */
    /*   alert('please login first, redirecting...'); */
    /*   this.$router.push('login') */
    /* } */

    console.log('page is ready')

  }
}
</script>
