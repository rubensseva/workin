<template>
  <div class="hello">
    <h1>Welcome to Workin!</h1>
    <p>
      Hear you can log workouts, and create workout plans (upcoming feature)
    </p>
    <h3>This site is intended to be use as supplement to Stready</h3>
    <p>
      Stready is a workout motivional service where you invest in your goals. You can use
      this site to log workouts for stready (upcoming feature)
    </p>
    <ul>
      <li><a href="http://get.stready.com" target="_blank" rel="noopener">Stready info page</a></li>
      <li><a href="http://stready.com" target="_blank" rel="noopener">Stready main page</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
