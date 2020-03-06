<template>
  <div class='root'>
    <div class='container'>
      <p> Welcome to Workin! Please login below </p>
      <input placeholder='username' v-model='userName'/>
      <input placeholder='password' v-model='password'/>
      <div v-if='this.$store.state.user.isAuthenticated'> You are logged in! </div>
      <button class='primaryButton' v-on:click='loginSubmit'>Submit</button>
    </div>
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
  },
  methods: {
    loginSubmit() {
      this.$store.dispatch('login', { 
        username: this.userName, 
        password: this.password
      })
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
