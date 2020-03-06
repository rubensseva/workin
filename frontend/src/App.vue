<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> | 
      <router-link to="/login">Login</router-link> |
      <router-link to="/workouts">Workouts</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

/* Custom global styles */
.primaryButton {
  margin: 10px 0px 10px 0px;
  background-color: rgba(56, 56, 100, 1); /* Blue */
  border: 0;
  border-radius: 5px;
  color: white;
  padding: 10px 15px;
  text-align: center;
  text-decoration: none;
  /* display: inline-block; */
  font-size: 14px;
  cursor:pointer;
  opacity: 0.8;
  transition: 0.5s;
}

.primaryButton:hover {
  opacity: 1;
}

</style>
