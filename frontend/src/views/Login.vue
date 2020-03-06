<template>
  <div class='root'>
    <div class='container'>
      <p> Welcome to Workin! Please login below </p>
      <input placeholder='username' v-model='userName'/>
      <input placeholder='password' v-model='password'/>
      <button class='primaryButton' v-on:click='loginSubmit'>Submit</button>
      <div class='loggedInText' v-if='this.$store.state.user.isAuthenticated'> You are logged in as: {{this.$store.state.user.user.username}} </div>
      <div class='loggedOutText' v-if='this.$store.state.user.isAuthenticated' v-on:click='logOut'> Click here to log out </div>
    </div>
    <router-link v-bind:to="'/user/new'">No user? No problem! Click here to create a new one</router-link>
  </div>
</template>


<script>
export default {
  name: 'Login',
  data: function() {
    return {
    userName: '',
    password: '',
    }
  },
  mounted() {
    this.$store.dispatch('tokenLogin')
      .catch(err => console.log(err))
  },
  methods: {
    loginSubmit() {
      this.$store.dispatch('login', { 
        username: this.userName, 
        password: this.password
      })
    },
    logOut() {
      this.$store.dispatch('logout')
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

/* .loggedText { */
/*   margin: 0 0 15px 0 */
/* } */
.loggedOutText {
  margin: 0 0 15px 0
}
.loggedOutText:hover {
  margin: 0 0 15px 0;
  cursor: pointer;
}

a {
  text-decoration: none;
  font-size: 15px;
  margin: 20px 0 0 0;
  opacity: 0.6;
  transition: 0.3s;
}
a:hover {
  opacity: 1;
  cursor:pointer;
}

</style>
