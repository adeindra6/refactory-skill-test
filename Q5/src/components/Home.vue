<template>
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <div class="header">
    <div class="logo">
      <img src="../assets/logo.png" width=50 height=50>
    </div>
    <img src="../assets/img_avatar.png" width=50 height=50 class="avatar">
    <p class="nama">Samsul Arifin</p>
    <div class="settings-icon">
      <i class="material-icons">settings</i>
    </div>
  </div>
  <div class="hello-box">
    <table>
      <tr>
        <td rowspan="2"><img src="../assets/clipboard.jpg" width=50 height=50></td>
        <td><p class="hello">Hallo, Sam!</p></td>
      </tr>
      <tr>
        <td><p class="hello-sub">You have 2 tasks left for today, Already completed Task today?</p></td>
      </tr>
    </table>
  </div>
  <p class="tft">Task for Today</p>
  <button @click="newTask()" type="button" class="btn-create-new">+ Create New</button>
  <input type="text" placeholder="Cari" class="input-cari" />
  <div class="calendar">
    <datepicker></datepicker>
  </div>
  <div class="task1">
    <p class="task-title">Daily Stand Up <span class="checked">&#10004; Complete</span></p>
    <p class="task-list">
      1. Dont forget prepare your report and any blocker in Front end.
      <br>
      2. Telling Project Manager for new assignment.
    </p>
    <span class="option">
      <i class="material-icons">delete</i>
    </span>
    &nbsp;
    <span class="option">
      <i class="material-icons">edit</i>
    </span>
  </div>
  <div class="task2">
    <p class="task-title">Meeting With Client A</p>
    <p class="task-list">
      1. Loream Ipsum Dolor Amet
      <br>
      2. Loream Ipsum Dolor Amet
    </p>
    <span class="option">
      <i class="material-icons">delete</i>
    </span>
    &nbsp;
    <span class="option">
      <i class="material-icons">edit</i>
    </span>
  </div>
  <div class="task3">
    <p class="task-title">Meeting With Client B</p>
    <p class="task-list">
      1. Loream Ipsum Dolor Amet
      <br>
      2. Loream Ipsum Dolor Amet
    </p>
    <span class="option">
      <i class="material-icons">delete</i>
    </span>
    &nbsp;
    <span class="option">
      <i class="material-icons">edit</i>
    </span>
  </div>
  <HomeForm v-show="popupActive" @close="closeModal()" />
</template>

<script>
import HomeForm from './HomeForm.vue';
import datepicker from 'vue3-datepicker';

  export default {
    name: "Home",
    components: {
      HomeForm,
      datepicker,
    },
    props: {
     msg: String
	},
    data() {
      return {
        popupActive: false,
      };
    },
    methods: {
      closeModal() {
        this.popupActive = false;
      },
      newTask() {
        this.popupActive = true;
      },
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  position: absolute;
  width: 1440px;
  height: 94px;
  left: 0px;
  top: 0px;
  background: #0442D0;
}

.logo {
  position: absolute;
  width: 83px;
  height: 26px;
  left: 44px;
  top: 28px;
}

.avatar {
  position: absolute;
  border-radius: 50%;
  width: 52px;
  height: 52px;
  left: 1080px;
  top: 22px;
}

.nama {
  position: absolute;
  width: 141px;
  height: 26px;
  left: 1150px;
  top: 15px;

  font-style: normal;
  font-weight: bold;
  font-size: 22px;
  line-height: 26px;
  color: #FFFFFF;
}

.settings-icon {
  position: absolute;
  color: #FFFFFF;
  top: 38px;
  right: 100px;
}

.hello-box {
  position: absolute;
  width: 394px;
  height: 168px;
  left: 49px;
  top: 138px;

  background: #0442D0;
  border-radius: 20px;
}

table {
  margin: 0 auto;
}

.hello {
  font-style: normal;
  font-weight: 900;
  font-size: 22px;
  line-height: 26px;
  color: #FABE2C;
  text-align: left;
  margin-left: 10%;
}

.hello-sub {
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 23px;
  color: #FFFFFF;
  text-align: left;
  margin-left: 10%;
}

.tft {
  position: absolute;
  width: 257px;
  height: 26px;
  left: 503px;
  top: 148px;

  font-style: normal;
  font-weight: bold;
  font-size: 35px;
  line-height: 41px;
  color: #525C77;
}

.btn-create-new {
  position: absolute;
  width: 157px;
  height: 43px;
  left: 510px;
  top: 230px;

  background: #0442D0;
  border-radius: 15px;
  border: none;

  font-style: normal;
  font-weight: 500;
  font-size: 15px;
  line-height: 18px;
  color: #FFFFFF;
}

.input-cari {
  position: absolute;
  width: 650px;
  height: 43px;
  left: 683px;
  top: 231px;

  border: 1px solid #0442D0;
  box-sizing: border-box;
  border-radius: 15px;
  text-align: center;
}

.calendar {
  position: absolute;
  left: 49px;
  top: 352px;

  background: #FFFFFF;
  box-shadow: 10px 10px 50px 10px #EEF3FD;
  border-radius: 31px;
}

.task1 {
  position: absolute;
  width: 894px;
  height: 146px;
  left: 506px;
  top: 306px;
  background: #FFFFFF;
  box-shadow: 10px 10px 50px 10px #EEF3FD;
  border-radius: 15px;
}

.task2 {
  position: absolute;
  width: 894px;
  height: 134px;
  left: 506px;
  top: 492px;
  background: #FFFFFF;
  box-shadow: 10px 10px 50px 10px #EEF3FD;
  border-radius: 15px;
}

.task3 {
  position: absolute;
  width: 894px;
  height: 144px;
  left: 506px;
  top: 666px;
  background: #FFFFFF;
  box-shadow: 10px 10px 50px 10px #EEF3FD;
  border-radius: 15px;
}

.task-title {
  font-style: normal;
  font-weight: bold;
  font-size: 25px;
  line-height: 29px;
  text-align: left;
  color: #525C77;
}

.task-list {
  font-style: normal;
  font-weight: normal;
  font-size: 15px;
  line-height: 18px;
  text-align: left;
  color: #525C77;
}

.checked {
  width: 82px;
  height: 25px;
  background: #FEEAEB;
  border-radius: 5px;
  font-style: normal;
  font-weight: bold;
  font-size: 10px;
  line-height: 12px;
  color: FB3453;
}

.option {
  float: right;
}
</style>