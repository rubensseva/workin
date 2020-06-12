<template>
  <div class='container'>
    <li v-for='workout in workouts' :key='workout.id'>
      <router-link v-bind:to="'/workout/' + workout.id">
        <div>
          {{ workout.name }}
        </div>
        <div>
          |
        </div>
        <div>
          {{ formatCreatedTime(workout.created) }}
        </div>
      </router-link>
    </li>

  </div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'ViewWorkouts',
  props: ['workouts'],
  methods: {
            formatCreatedTime : function (date) {
                return moment(date).format('ddd DD MMM YY');
            }
        }
}
</script>


<style scoped>
 
.container {
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  justify-content: center;
  align-items: center;
  max-width:500px;
}

a {
  display: flex;
  justify-content: space-evenly;
}

a div {
  width: 200px;
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
  cursor:pointer;
}

li a {
  text-decoration: none;
  color: rgba(50, 50, 50, 0.8)
}
 
 
</style>
