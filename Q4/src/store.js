import Vuex from "vuex";
import Vue from "vue";
import { SET_DATA } from "./mutation-types";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    lists: []
  },

  getters: {
    getData: (state) => {
      return state.lists;
    },
    getCountData: (state) => {
        return state.lists.length;
    }
  },

  mutations: {
    [SET_DATA](state, data) {
      state.lists = data
    },
  },

  actions: {
    setData(context, data) {
      context.commit("SET_DATA", data);
    },
  },
});
