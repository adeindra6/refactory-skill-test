<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal"
                 role="dialog"
                 aria-labelledby="modalTitle"
                 aria-describedby="modalDescription">
                <header
                    class="modal-header"
                    id="modalTitle">
                    <slot name="header">
                        <p class="label">New Task</p>
                        <button type="button" class="btn-close" @click="close" aria-label="Close modal">x</button>
                    </slot>
                </header>
                <section class="modal-body" id="modalDescription">
                    <slot name="body">
                        <form>
                            <div class="form-group">
                                <p class="label">Title</p>
                                <input
                                    type="textfield"
                                    class="input-form"
                                    placeholder="Fill Title">
                            </div>
                            <div class="form-group">
                                <p class="label">Description</p>
                                <textarea
                                     class="textarea-form"
                                     placeholder="Fill Description">                                 
                                </textarea>
                            </div>
                            <div class="form-group">
                                <p class="label">Choose Date</p>
                                <div class="calendar">
                                  <datepicker></datepicker>
                                </div>
                            </div>
                            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                            <button class="btn-cancel">Cancel</button>
                            <button class="btn-create">Create Task</button>
                            <br><br><br><br><br><br>
                        </form>
                    </slot>
                </section>
            </div>
        </div>
    </transition>
</template>

<script>
import datepicker from 'vue3-datepicker';

  export default {
    name: "HomeForm",
    components: {
      datepicker,
    },
    props: {
      msg: String
    },
    methods: {
      close() {
        this.$emit("close");
      },
    },
  }
</script>

<style>
.label {
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 29px;
  color: #525C77;
  text-align: left;
}

.modal-backdrop {
    position: fixed;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    width: 100%;
    height: 100%;
    justify-content: center;
    align-items: center;
}

.modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: hidden;
    width: 1000px;
    height: 600px;
    display: flex;
    flex-direction: column;
    border-radius: 20px;
}

.modal-header {
    display: flex;
}

.modal-header {
    border-bottom: 1px solid #000000;
    color: #000000;
    justify-content: space-between;
}

.modal-body {
    position: relative;
}

.btn-close {
    border: none;
    font-size: 20px;
    padding: 20px;
    cursor: pointer;
    font-weight: bold;
    color: #000000;
    background: transparent;
}

.modal-fade-enter, .modal-fade-leave-active {
  opacity: 0;
}

.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity .5s ease
}

.input-form {
  width: 100%;
  height: 40px;
  left: 427px;
  top: 315px;
  background: #FFFFFF;
  border: 1px solid rgba(207, 222, 252, 0.6);
  box-sizing: border-box;
  border-radius: 10px;
}

.textarea-form {
  width: 100%;
  height: 90px;
  left: 427px;
  top: 315px;
  background: #FFFFFF;
  border: 1px solid rgba(207, 222, 252, 0.6);
  box-sizing: border-box;
  border-radius: 10px;
}

.btn-create {
  width: 139px;
  height: 49px;
  left: 725px;
  top: 1160px;
  background: #0442D0;
  border-radius: 10px;
  border: none;
  font-weight: 500;
  font-size: 20px;
  line-height: 23px;
  color: #FFFFFF;
}

.btn-cancel {
  width: 139px;
  height: 49px;
  left: 725px;
  top: 1160px;
  background: #FFFFFF;
  border-radius: 10px;
  border: none;
  font-weight: 500;
  font-size: 20px;
  line-height: 23px;
  color: #0442D0;
}

.calendar {
  position: absolute;
  background: #FFFFFF;
  border: 1px solid #CFDEFC;
  box-sizing: border-box;
  border-radius: 10px;
}
</style>