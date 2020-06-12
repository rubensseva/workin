<template>
  <div id="app">
    <v-dialog />
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/workouts">Workouts</router-link>
      <router-link to="/workout_plans">Workout plans</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
:root {
--main-color: #0D5062;
--main-color-shaded-1: #1FC0ED;
--main-color-shaded-2: #178DAD;
--main-color-shaded-3: #0E596E;
--main-color-shaded-4: #0D5062;

--second-color: #1EBBA4;
--second-color-shaded-1: #26EDCF;
--second-color-shaded-2: #1CAD98;
--second-color-shaded-3: #126E60;
--second-color-shaded-4: #1EBBA4;

--action-color: #F4871E;
--action-color-shaded-1: #ED811C;
--action-color-shaded-2: #AD5F15;
--action-color-shaded-3: #6E3C0D;
--action-color-shaded-4: #F4871E;
}

@font-face {
/* font-family: "Alcubierre"; */
font-family: "SourceSansPro-Regular";
src: url("assets/fonts/SourceSansPro-Regular.ttf");
src:
url("assets/fonts/SourceSansPro-Regular.ttf") format("ttf"),
}

body {
  margin: 0;
}

#app {
  margin: 0;
  padding: 0;
  font-family: SourceSansPro-Regular, Alcubierre, Avenir, Helvetica, Arial, sans-serif, Alcubierre;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  position: relative;
  padding: 20px 0px 20px 0px;
  margin: 0px 0px 100px 0px;
  box-shadow: 0 0 10px rgba(0,0,0,0.8);
  -moz-box-shadow: 0 0 10px rgba(0,0,0,0.8);
  -webkit-box-shadow: 0 0 10px rgba(0,0,0,0.8);
  -o-box-shadow: 0 0 10px rgba(0,0,0,0.8);
}

#nav:after {
  content: '';
  display: block;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  background-color: var(--main-color-shaded-4);
  z-index: 9;

}
  
#nav a {
  position: relative;
  margin: 20px;
  padding: 10px;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2em;
  color: rgba(255, 255, 255, 1);
  z-index: 99;
}

#nav a:after{
  content: '';
  display: block;
  border-bottom: 1.3px solid var(--second-color);
  width: 0;
  position: absolute;
  left: 0;
  top: 37px;
  -webkit-transition: 1s ease;
  transition: 1s ease;
}

#nav a:hover:after { 
  width: 100%; 
}

#nav a.router-link-exact-active:after {
  width: 100%;
  background-color: rgba(100, 100, 100, 0.5);
}

/* Custom global styles */
.primaryButton {
  margin: 10px 0px 10px 0px;
  background-color: var(--main-color);
  background-position: center;
  border: none;
  border-radius: 5px;
  color: white;
  padding: 10px 15px;
  text-align: center;
  text-decoration: none;
  font-size: 14px;
  cursor:pointer;
  transition: background 0.8s;
  box-shadow: 0 0 4px #999;
  outline: none;
}

.primaryButton:hover {
  background: var(--main-color-shaded-3) radial-gradient(circle, transparent 1%, var(--main-color-shaded-4) 1%) center/15000%;
}

.primaryButton:active {
  background-color: var(--main-color-shaded-2);
  background-size: 100%;
  transition: background 0s;
}




</style>
