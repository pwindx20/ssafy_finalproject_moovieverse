<template>
  <div class="box basic-background main">
      <p class="font-link title">회원가입</p>
      <p class="font-title">회원가입을 통해 더 넓은 영화 세계를 경험하세요!</p>
      <form class="form" @submit.prevent="signUp">
        <label class="font-title" for="username">아이디 :</label>
        <input type="text" id="username" v-model.trim="username"><br><br>
        
        <label class="font-title" for="password1">비밀번호 :</label>
        <input type="password" id="password1" v-model.trim="password1"><br><br>
        
        <label class="font-title" for="password2">비밀번호 확인 :</label>
        <input type="password" id="password2" v-model.trim="password2"><br><br>
        
        <label class="font-title" for="email"> 이메일 : </label>   
          <span class="emailInt" id="emailBox"> <input type="text" id="email" maxlength="20" v-model.trim="email" > 
            <label for="emailSelect">@</label> 
            <!-- 이메일 택일 -->
            <select v-model="mail_Select" id="emailSelect">
              <option>이메일 선택</option>
              <option value="@naver.com">naver.com</option>
              <option value="@gmail.com">gmail.com</option>
              <option value="@daum.net">daum.net</option>
              <option value="@hanmail.net">hanmail.net</option>
              <option value="@hotmail.com">hotmail.com</option>
              <option value="@nate.com">nate.com</option>
              <option value="@yahoo.co.kr">yahoo.co.kr</option>
              <option value="@empas.com">empas.com</option>
              <option value="@freechal.com">freechal.com</option>
              <option value="@lycos.co.kr">lycos.co.kr</option>
              <option value="@korea.com">korea.com</option>
              <option value="@hanmir.com">hanmir.com</option>
              <option value="@dreamwiz.com">dreamwiz.com</option>
              <option value="@paran.com">paran.com</option>
            </select>
          </span><br><br>
          
          
          
          <label class="font-title" for="nickname">닉네임 :</label>
          <input type="text" id="nickname" v-model.trim="nickname"><br><br>
          
          <input class="submitBtn" type="submit" value="가입하기">
        </form>
      </div>
    </template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const store = useAccountStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const nickname = ref(null)
const mail_Select = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value + mail_Select.value,
    nickname: nickname.value,
  }
  store.signUp(payload)
}

</script>

<style scoped>
p {
  font-size: 30px;
}
.main {
  position: relative;
  justify-content: center;
  align-items: center;
  height: 90%;
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
  bottom: 10%;
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
  margin-top: 5%;
  text-align: end;
}


</style>