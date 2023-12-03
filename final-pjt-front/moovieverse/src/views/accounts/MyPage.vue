<template>
  <div class="box basic-background">
    <p class="font-link">마이페이지</p>
    <div class="profile-header">
      <div class="name">
        <p class="font-title" v-if="accountStore.profile?.username !== accountStore.username_onlogin">{{ accountStore.profile?.nickname }}의 프로필</p>
        <p class="font-title" v-else> {{ accountStore.profile?.nickname }}</p>
      </div>
      <div class="checkbar gap-3">
        <div @click="gocheck1">📝</div>
        <div @click="gocheck2">❤</div>
        <div @click="gocheck3">🎥</div>
      </div>
      <div class="follow gap-2 mt-3">
        <div class="font-title">팔로워 : {{ accountStore.profile?.followers_count }} </div> <br>
        <div class="font-title">팔로잉 : {{ accountStore.profile?.followings_count }} </div> <br>
      </div>
      <div class="follow-btn" v-if="accountStore.username_onlogin!==accountStore.profile?.username">
        <button class="font-title"  @click="follow" v-if="!accountStore.isFollowed">팔로우하기</button>
        <button class="font-title" @click="follow" v-else>언팔로우</button> 
      </div>
    </div>
    <hr>
    <div class="row justify-content-center" v-if="check===1">
      <div class="col-3">
        <p class="font-title">내가 쓴 리뷰</p>
        <div v-if="accountStore.everything?.myreviewSerializer">
          <div
          v-for="myreview in accountStore.everything?.myreviewSerializer"
          :key="myreview.id">
          {{ myreview.content }}
          <hr>
        </div>
        </div>
      </div>
      <div class="col-3">
        <p class="font-title">내가 쓴 게시글</p>
        <div v-if="accountStore.everything?.myarticleSerializer">
          <div
          v-for="myarticle in accountStore.everything?.myarticleSerializer"
          :key="myarticle.id">
            {{ myarticle.title }} 
            <hr>
          </div>
        </div>
      </div>
      <div class="col-3">
        <p class="font-title">내가 쓴 댓글</p>
        <div v-if="accountStore.everything?.mycommentSerializer">
          <div
          v-for="mycomment in accountStore.everything?.mycommentSerializer"
          :key="mycomment.id">
          {{ mycomment.content }} 
          <hr>
          </div>
        </div>
      </div>
    </div>

    <div class="row justify-content-center" v-if="check===2">
      <div class="col-4">
        <p class="font-title">좋아요한 리뷰</p>
        <div v-if="accountStore.everything?.reviewSerializer"
        v-for="review in accountStore.everything?.reviewSerializer">
        {{ review.content }} 
        <hr>
      </div>
      </div>
      <div class="col-4">
        <p class="font-title">좋아요한 게시글</p>
        <div v-if="accountStore.everything?.articleSerializer">
          <div
          v-for="article in accountStore.everything?.articleSerializer">
          {{ article.title }}
          <hr> 
          </div>
        </div>
      </div>
    </div>
    
    <div class="row" v-if="check===3">
      <p class="font-title ms-2">보고싶어요</p>
      <div class="row"
      v-if="accountStore.everything?.movieSerializer !== null" 
      >
        <img 
        v-for="movie in accountStore.everything?.movieSerializer"
       :key="movie.id" 
        :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster"
        @click="movieStore.goDetail(movie.id)" class="col-2 mb-4 link">
      </div>
    </div>
  
   <br>
   
  </div>

 

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '../../stores/movies';

const accountStore = useAccountStore()
const movieStore = useMovieStore()
const route = useRoute()
const check = ref(2)

onMounted(() => {
  accountStore.getProfile(route.params.username)
  
})

const follow = function(){
  console.log(route.params)
  accountStore.follow(accountStore.profile.id, route.params.username)
  // accountStore.getProfile(route.params.username)
}

const gocheck1 = function() {
  check.value = 1
}

const gocheck2 = function() {
  check.value = 2
}

const gocheck3 = function() {
  check.value = 3
}
</script>

<style  scoped>
.name{
  font-size: 30px;
  text-decoration: underline;
}
.profile-header{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.checkbar {
  font-size: 20px;
  display: flex;
  width: fit-content;
  border-radius: 15px;
  padding: 5px;
  border: 1px solid white;
  background-color: rgba(255, 255, 255, 0.5);
}

.checkbar >div:hover, .checkbar >div:active{
  background-color: white;
  border-radius: 15px;
  color: rgb(4, 20, 44);
  height: 100%;
}
.follow{
  display: flex;
  justify-content: center;
  align-items: center;
}
img{
  border-radius: 30px;
}

img :hover{
  color: white;
}
.follow-btn{
  font-size: 20px;
  color: rgb(4, 20, 44);
  border: 1px rgb(4, 20, 44) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 5px;
}
</style>