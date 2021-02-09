<template>
  <div class="main">
    <div class="main-title">{{ msg }}</div>
    <div class="user-count">
      <div class="count">{{ count }}</div>
      Users
    </div>
    <div class="wrapper">
      <div class="row">
        <div class="col-lg-6">
          <div v-for="user in users" :key="user.name" class="card">
            <div class="body-card">
              <div class="title">Name</div>
              <div class="name">{{ user.name }}</div>
              <div class="wrapper-card">
                <div>
                  <div class="title">Email</div>
                  <div class="email">{{ user.email }}</div>
                </div>
                <div>
                  <div class="title">Phone</div>
                  <div class="phone">{{ user.phone }}</div>
                </div>
                <div>
                  <div class="title">Website</div>
                  <div class="website">{{ user.website }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "Users",
  props: {
    msg: String,
  },
  computed: {
    ...mapState(["lists"]),
    users() {
      return this.$store.getters.getData;
    },
    count() {
      return this.$store.getters.getCountData;
    },
  },
  mounted() {
    axios
      .get("https://jsonplaceholder.typicode.com/users")
      .then((response) => {
        this.setData(response.data);
      })
      .catch((error) => console.log(error));
  },
  methods: {
    setData(data) {
      this.$store.dispatch("setData", data);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main {
  background-color: #f5f7fa;
  padding: 10px;
}
.count {
  color: #83dd8b;
  font-weight: 800;
  margin-right: 10px;
}
.user-count {
  border-bottom: 1px solid #e1e1e7;
  color: #646464;
  display: flex;
}
.main-title {
  font-size: 36px;
  font-weight: bold;
}
.title {
  color: #bfbfbf;
  font-size: 14px;
}
.name {
  color: #404040;
  font-weight: bold;
  font-size: 20px;
}
.email {
  font-size: 14px;
}
.phone {
  font-size: 14px;
}
.website {
  font-size: 14px;
  color: #4dff4d;
}
</style>