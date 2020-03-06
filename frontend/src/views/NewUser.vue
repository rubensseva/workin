<template>
  <div class='root'>
    <div class='container'>
      <p> Create a new user </p>
      <input placeholder='username' v-model='username'/>
      <input type='email' placeholder='email' v-model='email'/>
      <input type='password' placeholder='password' v-model='password'/>
      <button class='primaryButton' v-on:click='createUser'>Create user</button>
    </div>
    <div v-if='this.userWasCreated'> User was successfully created </div>
  </div>
</template>


<script>
export default {
  name: 'NewUser',
  data: function() {
    return {
      username: '',
      email: '',
      password: '',
      userWasCreated: false,
    }
  },
  mounted() {
    this.$store.dispatch('tokenLogin')
      .catch(err => console.log(err))
  },
  methods: {
    createUser() {
      this.$store.dispatch('createUser', { 
        username: this.username, 
        email: this.email,
        password: this.password
      })
        .then(() => {this.userWasCreated = true})
        .catch(err => alert('An error occured:', err))
    }
  }
}
</script>


<style scoped>
.root {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.container {
  display: flex;
  align-items: center;
  flex-direction: column;
  flex-wrap: nowrap;
  width: 400px;
  background-color: rgba(56, 56, 80, 0.5);
  border-radius: 5px;
}

.container > input {
  margin: 0px 0px 10px 0px;
  border: 0;
  color: inherit;
  font: inherit;
  outline: 0;
  -webkit-transition: background-color .3s;
  transition: background-color .3s;
}

.container > input:last-child {
  margin: 0px 0px 20px 0px
}

</style>
