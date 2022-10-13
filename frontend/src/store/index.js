import { createStore } from 'vuex'

export default createStore({
  state: {
    token:"",
    contactPerson:"",
    IsAuthenticated:false,
    IsContactAvailable:false
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("contactPerson") && localStorage.getItem("token")) {

        state.contactPerson= localStorage.getItem("contactPeson")
        state.IsContactAvailable=true
        state.token=localStorage.getItem("token")
        state.IsAuthenticated=true
      } 
      else if(localStorage.getItem("contactPerson")){
        state.contactPerson=localStorage.getItem("contactPerson")
        state.IsContactAvailable=true
        state.token=""
        state.IsAuthenticated=false
      }
      else {
        state.contactPerson=""
        state.IsContactAvailable=false
        state.token=""
        state.IsAuthenticated=false
      }
    },
    setContactName(state,contactPerson) {
      state.contactPerson=contactPerson
      state.IsContactAvailable=true
    },
    setToken(state,token) {
      state.token=token
      state.IsAuthenticated=true
    },
    removeToken(state) {
      state.token=''
      state.IsAuthenticated=false
    }
  },
  actions: {
  },
  modules: {
  }
})
