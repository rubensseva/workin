import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      user: {},
      isAuthenticated: false,
      workouts: {},
    },
  },
  mutations: {
    userLoggedIn(state) {
      state.user.isAuthenticated = true
    },
    userLoggedOut(state) {
      state.user.isAuthenticated = false
    },
    setCurrentUser(state, payload) {
      state.user.user = payload
    }
  },
  actions: {
    tokenLogin(context) {
      return new Promise((resolve, reject) => {
        if (!localStorage.getItem('jwt')) {
          context.commit('userLoggedOut')
          context.commit('setCurrentUser', {})
          return resolve()
        }
        axios({
          method: 'get',
          url: '/user/verify_token',
          headers: {
            Authorization: `Basic ${localStorage.getItem('jwt')}`
          }
        })
        .then((response) => {
          context.commit('userLoggedIn')
          context.commit('setCurrentUser', response.data.payload)
          return resolve()
        })
        .catch(err => {
          context.commit('userLoggedOut')
          context.commit('setCurrentUser', {})
          console.log(err)
          return reject()
        })
      })
    },
    login(context, { username, password }) {
      axios({
        method: 'post',
        url: 'user/login',
        data: {
          username: username,
          password: password
        }
      })
      .then((response) => {
        localStorage.setItem('jwt', response.data.jwt);
        return context.dispatch('tokenLogin')
      })
      .catch(err => console.log(err))
    },
    logout(context) {
      localStorage.removeItem('jwt');
      context.commit('userLoggedOut')
    },
    createUser(context, { username, email, password }) {
      return new Promise((resolve, reject) => {
        axios({
          method: 'post',
          url: '/user',
          data: {
            username: username,
            email: email,
            password: password
          }
        })
          .then((response) => resolve(response))
          .catch(err => reject(err))
      })
    },
    createWorkout(context, {name, workoutType, duration, workoutAt}) {
      let data = {
        user_id: context.state.user.user.id,
        name: name,
        workout_type: workoutType,
        duration: duration,
        workout_at: workoutAt,
      }
      console.log('data', data)
      axios({
        method: 'post',
        url: 'workout',
        data: data,
        headers: {
          Authorization: `Basic ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => context.dispatch('tokenLogin'))
        .catch(err => console.log(err))
    },
    createWorkoutEntry(context, {type, amountPerSet, numSets, duration, weight, workoutId}) {
      let data = {
        type: type,
        amount_per_set: amountPerSet,
        num_sets: numSets,
        duration: duration,
        weight: weight,
        workout_id: workoutId
      }
      return axios({
        method: 'post',
        url: '/workout_entry',
        data: data,
        headers: {
          Authorization: `Basic ${localStorage.getItem('jwt')}`
        }
      })
    },
    createWorkoutPlan(context, {name, weekDayStart}) {
      let data = {
        name: name,
        week_day_start: weekDayStart,
        user_id: context.state.user.user.id,
      }
      console.log('here', data)
      axios({
        method: 'post',
        url: '/workout_plan',
        data: data,
        headers: {
          Authorization: `Basic ${localStorage.getItem('jwt')}`
        }
      })
        .then(() => context.dispatch('tokenLogin'))
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
