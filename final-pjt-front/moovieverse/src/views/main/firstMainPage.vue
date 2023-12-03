<template>
  <div class="box basic-background main">
    <article v-if="!accountStore.isLogin">  
      <p class="font-link">moovieverse에 오신 것을 환영합니다!</p>
      <p class="font-link">무비버스와 함께 새로운 우주로 떠나보세요.</p>
      <hr>
      <div class="font-link links">
        <button class="mx-3" @click="signup()">회원가입</button>
        <button class="mx-3" @click="login()">로그인</button>
      </div>
    </article>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router"
import { useAccountStore } from '@/stores/account'

const router = useRouter()
const accountStore = useAccountStore()

const signup = () => {
  router.push({
    path: "/signup",
  });
};

const login = () => {
  router.push({
    path: "/login",
  });
};
</script>

<style scoped>
.main {
  margin-top: 10%;
  justify-content: center;
  align-items: center;
}

.links{
  text-align: center;
}

button {
  font-size: 25px;
  width: 40%;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  text-decoration: none;
}

</style>