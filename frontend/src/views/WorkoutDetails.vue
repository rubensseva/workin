<template>
  <div class='container'>
    <h1> Workout details </h1>
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
    </div>
      <div>
        Exercises in this workout
      </div>
      <div class='entryWrapper workoutContainer'>
        <div class='entryField'>
          type
        </div>
        <div class='entryLine'>
          |
        </div>
        <div class='entryField'>
          amount per set
        </div>
        <div class='entryLine'>
          | 
        </div>
        <div class='entryField'>
          num sets 
        </div>
        <div class='entryLine'>
          |
        </div>
        <div class='entryField'>
          duration 
        </div>
        <div class='entryLine'>
          |
        </div>
        <div class='entryField'>
          weight
        </div>
      </div>
    <div class='workoutEntriesContainer workoutContainer'>
      <li v-for='workout_entry in workout.workout_entries' :key='workout_entry.id'>
        <div class='entryWrapper'>
          <div class='entryField'>
            {{ workout_entry.entry_type }}
          </div>
          <div class='entryLine'>
            |
          </div>
          <div class='entryField'>
            {{ workout_entry.amount_per_set }}
          </div>
          <div class='entryLine'>
            | 
          </div>
          <div class='entryField'>
            {{ workout_entry.num_sets }}
          </div>
          <div class='entryLine'>
            |
          </div>
          <div class='entryField'>
            {{ workout_entry.duration }}
          </div>
          <div class='entryLine'>
            |
          </div>
          <div class='entryField'>
            {{ workout_entry.weight }}
          </div>
        </div>
      </li>
    </div>

    <button class='primaryButton' v-on:click="openModal">
      Add an entry
    </button>

    <modal name="hello-world">
      <form class="addWorkoutEntryMiniForm" @submit='createWorkoutEntry'>
        <input required type="text" placeholder="entry type" v-model='newWorkoutEntry.type'/>
        <input required type="number" placeholder="amount per set" v-model='newWorkoutEntry.amountPerSet'/>
        <input required type="number" placeholder="number of sets" v-model='newWorkoutEntry.numSets'/>
        <input required type="number" placeholder="duration" v-model='newWorkoutEntry.duration'/>
        <input required type="number" placeholder="weight" v-model='newWorkoutEntry.weight'/>
        <input class='primaryButton' type='submit' value='Add new entry to workout'/>
      </form>
    </modal>

  </div>
</template>


<script>
export default {
  name: 'WorkoutDetails',
  data: function() {
    return {
      workout: {},
      newWorkoutEntry: {
        type: null,
        amountPerSet: null,
        numSets: null,
        duration: null,
        weight: null,
      }
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
          this.workoutEntryUpdateCounter += 1;
        })
        .catch(err => console.log(err))
    }
    let workoutId = parseInt(this.$route.params.id);
    if (!workoutId) {
      alert('Error when attempting to parse workout id url param as int')
      this.$router.push('/')
    }
    let allWorkouts = this.$store.state.user.user.workouts;
    let workout = allWorkouts.filter(workout => workout.id === workoutId)[0]
    this.workout = workout
  },
  methods: {
    openModal() {
      this.$modal.show('hello-world');
    },
    createWorkoutEntry() {
      this.$store.dispatch('createWorkoutEntry', { 
        type: this.newWorkoutEntry.type, 
        amountPerSet: this.newWorkoutEntry.amountPerSet,
        numSets: this.newWorkoutEntry.numSets,
        duration: this.newWorkoutEntry.duration,
        weight: this.newWorkoutEntry.weight,
        workoutId: this.$route.params.id
      })
        .then(() => {
          return this.$store.dispatch('tokenLogin')
        })
        .then(() => {
          let workoutId = parseInt(this.$route.params.id);
          if (!workoutId) {
            alert('Error when attempting to parse workout id url param as int')
            this.$router.push('/')
          }
          let allWorkouts = this.$store.state.user.user.workouts;
          let workout = allWorkouts.filter(workout => workout.id === workoutId)[0]
          this.workout = workout
          console.log('completed')
        })
        .catch(err => console.log(err))
    }
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
  margin-top: 20px;
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

.entryWrapper {
  display: flex;
  justify-content: space-evenly;
}

.entryField {
  width: 150px;
}

.entryLine {
  width: 10px
}

.addWorkoutEntryMiniForm {
  display: flex;
  flex-direction: column;
  place-items: center;
}

.addWorkoutEntryMiniForm input {
  margin: 10px;
}

</style>
