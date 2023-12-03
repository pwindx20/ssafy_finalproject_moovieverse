<template>
    <nav class="navbar navbar-dark navbar-expand-lg bg-body-tertiary px-4 pt-4">
      <div class="container-fluid gap-5">
        <a class="navbar-brand logo link" @click.prevent="goHome">
          <img src="@/assets/moovieverse_logo_white.png" alt="logo">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarSupportedContent">
            <ul class="navbar-nav">
                <RouterLink class="font-link pe-4" :to="{ name:'secondMainPage'}">Home</RouterLink>
                <a class="font-link link pe-4" @click="goArticle">게시판</a>
                <a class="font-link link pe-4" @click="goRecommend">장르 추천</a>
                <!-- <RouterLink class="font-link" :to="{ name:'RecommendPage'}">장르 추천</RouterLink> -->
              </ul>
              <ul class="navbar-nav gap-2">
              <a class="font-link link mypage" @click="accountStore.goMyProfile()">My Page</a>
              <!-- <RouterLink class="font-link mypage" :to="{ name:'MyPage', params: {username: accountStore.username_onlogin }}">MyPage</RouterLink> -->
              <RouterLink class="font-link mypage" @click="accountStore.logOut()" :to="{ name:'firstMainPage'}">로그아웃</RouterLink>
            </ul>
        </div>
      </div>
    </nav>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account'
import { useArticleStore } from '../../stores/article';
import { useMovieStore } from '../../stores/movies';
const accountStore = useAccountStore()
const articleStore = useArticleStore()
const movieStore = useMovieStore()
const router = useRouter()

const goHome = function(){
  router.push({name:'secondMainPage'})
}
const goArticle = function(){
  articleStore.getArticles()
  router.push({name:'ArticleMain'})
}
const goRecommend = function(){
  movieStore.recommendCheck = null
  movieStore.favorite_genres = null
  movieStore.challenge_genres = null
  movieStore.recommendedList = null
  router.push({name:'RecommendPage'})
}
</script>

<style scoped>
.logo > img {
  width: 200px;
  height: auto;
  object-fit: contain;
  background-size: cover;
  }

.mypage{
  font-size: 20px;
  color: rgb(4, 20, 44);
  border: 1px rgb(4, 20, 44) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 5px;
}

</style>