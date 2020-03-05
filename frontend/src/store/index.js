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
    }
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
    getCurrentUser(context) {
      if (!localStorage.getItem('jwt')) {
        context.commit('userLoggedOut')
        context.commit('setCurrentUser', {})
        return
      }
      axios({
        method: 'get',
        url: 'user/verify_token',
        headers: {
          Authorization: `Basic ${localStorage.getItem('jwt')}`
        }
      })
      .then((response) => {
        context.commit('userLoggedIn')
        context.commit('setCurrentUser', response.data.payload)
      })
      .catch(err => {
        context.commit('userLoggedOut')
        context.commit('setCurrentUser', {})
        console.log(err)
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
        context.commit('userLoggedIn')
        return axios({
          method: 'get',
          url: 'user',
          params: {
            username: username
          },
          headers: {
            Authorization: `Basic ${response.data.jwt}`
          }
        })
      })
      .then(response => {
        context.commit('setCurrentUser', response.data.payload[0])
      })
        .catch(err => {
          context.commit('userLoggedOut')
          context.commit('setCurrentUser', {})
          console.log(err)
        })
    }
  },
  modules: {
  }
})
