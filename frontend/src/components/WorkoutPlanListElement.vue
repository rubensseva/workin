<template>
  <div class='container'>
    Name: {{ workoutPlan.name }}
  </div>
</template>


<script>
export default {
  name: 'WorkoutPlanListElement',
  props: ['workoutPlan']
}
</script>


<style scoped>
.container {
  margin: 20px 0 20px 0;
  padding: 10px 0 0 0;
  height: 30px;
  background-color: rgba(230, 230, 255, 1);
  border: solid 1px rgba(50, 50, 50, 0.5);
  border-radius: 3px;
}
</style>
