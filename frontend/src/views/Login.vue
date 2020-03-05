<template>
  <div class='root'>
    <div class='container'>
      <p> Welcome to Workin! Please login below </p>
      <input placeholder='username' v-model='firstName'/>
      <input placeholder='password' v-model='password'/>
      <div v-if='this.$store.state.user.isAuthenticated'> You are logged in! </div>
      <button class='primaryButton' v-on:click='loginSubmit'>Submit</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function() {
    return {
    firstName: '',
    password: '',
    }
  },
  mounted() {
    if (localStorage.getItem('jwt') !== null) {
      axios({
        method: 'get',
        url: 'user/verify_token',
        headers: {
          Authorization: `Basic ${localStorage.getItem('jwt')}`
        }
      })
      .then((response) => {
        this.$store.commit('userLoggedIn')
        this.$store.commit('setCurrentUser', response.data.payload)
      })
      .catch(err => console.log(err))
    }
  },
  methods: {
    loginSubmit() {
      axios({
        method: 'post',
        url: 'user/login',
        data: {
          username: this.firstName,
          password: this.password
        }
      })
      .then((response) => {
        localStorage.setItem('jwt', response.data.jwt);
        this.$store.commit('userLoggedIn')
        return axios({
          method: 'get',
          url: 'user',
          params: {
            username: this.firstName
          },
          headers: {
            Authorization: `Basic ${response.data.jwt}`
          }
        })
      })
      .then(response => {
        this.$store.commit('setCurrentUser', response.data.payload[0])
      })
      .catch(err => console.log(err))
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
