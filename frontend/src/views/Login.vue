<template>
  <div class='root'>
    <form class='container' v-on:submit.prevent='loginSubmit'>
      <p> Welcome to Workin! Please login below </p>
      <input required type=name placeholder='username' v-model='userName'/>
      <input required type=password placeholder='password' v-model='password'/>
      <input
        class='primaryButton'
        type='submit'
        value='Submit'
      />
      <div class='loggedInText' v-if='this.$store.state.user.isAuthenticated'> You are logged in as: {{this.$store.state.user.user.username}} </div>
      <div class='loggedOutText' v-if='this.$store.state.user.isAuthenticated' v-on:click='logOut'> Click here to log out </div>
    </form>
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
      console.log('logging in');
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
  margin: 40px 0px 0px 0px;
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;
  flex-wrap: nowrap;
  width: 400px;
  border-radius: 5px;
}

.container::after {
    content:'';
    height: 100%;
    width: 100%;
    background-color: var(--main-color);
    position:absolute;
    top:0;
    left:0;
    box-shadow: 0 0 10px rgba(0,0,0,0.8);
    -moz-box-shadow: 0 0 10px rgba(0,0,0,0.8);
    -webkit-box-shadow: 0 0 10px rgba(0,0,0,0.8);
    -o-box-shadow: 0 0 10px rgba(0,0,0,0.8);
    opacity:0.2;
    z-index: -1;
}

.container > input {
  margin: 0px 0px 10px 0px;
  border: 0;
  outline: 0;
  -webkit-transition: background-color .3s;
  transition: background-color .3s;
}

.container > input:last-child {
  margin: 0px 0px 20px 0px
}

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
