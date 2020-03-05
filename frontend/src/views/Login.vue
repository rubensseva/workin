<template>
  <div class='root'>
    <LoginTest/>
    <div class='container'>
      <p> Welcome to Workin! Please login below </p>
      <input placeholder='username' v-model='firstName'/>
      <input placeholder='password' v-model='password'/>
      <button class='primaryButton' v-on:click='loginSubmit'>Submit</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import LoginTest from '@/components/LoginTest'

export default {
  name: 'Login',
  components: {
    LoginTest
  },
  data: function() {
    return {
    firstName: '',
    password: '',
    }
  },
  methods: {
    loginSubmit() {
      axios({
        method: 'post',
        url: 'user/login',
        timeout: 4000, // Let's say you want to wait at least 4 mins
        data: {
          username: this.firstName,
          password: this.password
        }
      })
      .then((response) => {
        console.log(response);
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
        console.log(response)
        this.$store.commit('setCurrentUser', response.data)
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
