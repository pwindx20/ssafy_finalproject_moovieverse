<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/main/NavBar.vue';
import { useAccountStore } from '@/stores/account'
import { ref, computed } from 'vue'

const store = useAccountStore()
</script>

<template>
  <div>
    <div class="header" v-if="store.isLogin">
      <Navbar />
      <hr class="mt-0">
    </div>
    <RouterView />
    <div class="bg-video">
      <div class="background_opacity"></div>
      <video class="bg-video__content" autoplay muted loop>
        <source src="@/assets/space_video.mp4" type="video/mp4" />
      </video>
    </div>
  </div>
</template>

<style scoped>
.bg-video {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: -1;
}
.bg-video__content {
  height: 100%;
  width: 100%;
  object-fit: cover
}
.background_opacity {
  position: fixed;
  bottom: 0;
  left: 0;
  border-radius: 5px;
  background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.5));
  height: 100%;
  width: 100%;
}
</style>

<style>
/* 폰트 */
@import url(//fonts.googleapis.com/earlyaccess/nanumgothic.css);
@font-face {
    font-family: 'Giants-Inline';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-1@1.1/Giants-Inline.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
  }
@font-face {
  font-family: 'Giants-Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-1@1.1/Giants-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
* {
  color: white;
  font-family: 'Nanum Gothic';
}
.font-link {
  text-decoration: none;
  color: white;
  font-size: 35px;
  font-family: 'Giants-Inline';
}
.font-title {
  font-family: 'Giants-Bold'
}
.link {
  cursor: pointer;
}

/* 바탕 */
.box {
  display: flex;
  flex-direction: column;
}
.basic-background{
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  min-height: 50vh;
  padding: 30px;
  margin-left: 10%;
  margin-right: 10%;
}
input {
  color: rgb(4, 20, 44);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
}

select{
  font-size: 20px;
  color: rgb(4, 20, 44);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
}

option{
  color: rgb(4, 20, 44);
}
textarea{
  color: rgb(4, 20, 44);
}
</style>