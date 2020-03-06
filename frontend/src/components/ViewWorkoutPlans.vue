<template>
  <div>
    Workout plans viewer
    <li v-for='workoutPlan in workoutPlans' :key='workoutPlan.id'>
      <WorkoutPlanListElement v-bind:workoutPlan='workoutPlan'/>
    </li>
  </div>
</template>


<script>
import WorkoutPlanListElement from '@/components/WorkoutPlanListElement.vue'
export default {
  name: 'ViewWorkoutsPlans',
  components: {
    WorkoutPlanListElement
  },
  props: ['workoutPlans']
}
</script>


<style scoped>
li {
  list-style-type: none;
}
</style>
