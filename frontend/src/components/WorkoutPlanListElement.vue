<template>
  <div class='workoutPlanCardContainer'>
    <p class='workoutPlanCardText'> 
      {{ workoutPlan.name }}
    </p>
    <hr class='cardLine'/>
    <p class='workoutPlanCardText'>
      Some text about the plan
    </p>
  </div>
</template>


<script>
export default {
  name: 'WorkoutPlanListElement',
  props: ['workoutPlan']
}
</script>


<style scoped>

.cardLine {
  position: relative;
  z-index: 12;
  width: 85%;
  margin: auto;
  opacity: 0.5;
}


.workoutPlanCardContainer {
  position: relative;
  height: 170px;
  width: 150px;
  background-color: rgb(255, 255, 255);
  border: 1px solid grey;
  border-radius: 3px;
  -moz-box-shadow: 0 0 3px #ccc;
  -webkit-box-shadow: 0 0 3px #ccc;
  box-shadow: 0 0 3px #ccc;
  transform: rotateX(0deg);
  transition: 1s;
  overflow: hidden;
  z-index: 10;
}

.workoutPlanCardContainer:hover {
  transform: rotateX(10deg) translateZ(30px);
  -moz-box-shadow: 0 0 20px #ccc;
  -webkit-box-shadow: 0 0 20px #ccc;
  box-shadow: 0 0 20px #ccc;
}

.workoutPlanCardContainer:before {
  position: absolute;
  content: " ";
  top: -10%;
  left: -10%;
  width: 120%;
  height: 55%;
  z-index: 11;
  background-color: #FFF;
  opacity: 1;
  transform: rotate(10deg);
  transition: 1s;
}

.workoutPlanCardContainer:hover:before {
  height: 62%;
}

.workoutPlanCardText {
  position: relative;
  z-index: 12;
}

</style>
