<template>
  <div class='root'>
    <form class='container' v-on:submit:prevent='createUser'>
      <p> Create a new user </p>
      <input required type='text' placeholder='username' v-model='username'/>
      <input required type='email' placeholder='email' v-model='email'/>
      <input required type='password' placeholder='password' v-model='password'/>
      <input class='primaryButton' type='submit' value='Create user'/>
    </form>
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

</style>
