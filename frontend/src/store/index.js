import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      user: {},
      isAuthenticated: false,
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
  },
  modules: {
  }
})
