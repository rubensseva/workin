<template>
  <div>
    Workout plans viewer
    <div class='workoutPlanContainer'>
      <div class='workoutPlanItem' v-for='workoutPlan in workoutPlans' :key='workoutPlan.id'>
        <WorkoutPlanListElement v-bind:workoutPlan='workoutPlan'/>
      </div>
    </div>
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

.workoutPlanContainer {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  place-items: center;
  perspective: 1000px;
}

.workoutPlanItem {
  margin: 20px;
  
}


li {
  list-style-type: none;
}
</style>
