<template>
  <div class="box basic-background main">
      <p class="font-link title">로그인</p>
      <form class="form" @submit.prevent="logIn">
        <div>
          <label class="font-title mx-2" for="username">아이디 : </label>
          <input type="text" id="username" v-model.trim="username"><br>
        </div>
        <div>
          <label class="font-title mx-2" for="password">비밀번호 : </label>
          <input type="password" id="password" v-model.trim="password"><br>
        </div>
        <input class="submitBtn font-title" type="submit" value="로그인">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'
const store = useAccountStore()

const logIn = function () {
  const payload ={
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

const username = ref(null)
const password = ref(null)

</script>

<style scoped>
.main {
  position: relative;
  margin-top: 10%;
  justify-content: center;
  align-items: center;
}
.title{
  position:absolute;
  top: 10%;
  font-size: 50px;
}
label{
  font-size: 30px
}

.submitBtn{
  position: absolute;
  bottom: 20%;
  left: 40%;
  font-size: 25px;
  width: 20%;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px;
  text-decoration: none;
}

.form{
  text-align: end;
}

</style>