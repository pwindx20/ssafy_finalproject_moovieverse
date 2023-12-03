<template>
  <div class="box basic-background">
    <div class="title">
      <p class="font-title m-0">{{ accountStore.myProfile.userSerializer.nickname }}님의 취향에 맞는 영화를 추천해드릴게요! </p>
      <div v-if="movieStore.recommendCheck !== null">
        <div v-if="movieStore.recommendCheck==1">
        <p class="font-title mb-0">{{ accountStore.myProfile.userSerializer.nickname }}님의 최애 장르는... </p>
        <p class="font-title mb-0"><span class="font-link genre mb-0">{{ movieStore.favorite_genres.join(', ') }}</span>입니다.</p>
      </div>
      <div v-if="movieStore.recommendCheck==2">
        <p class="font-title mb-0">{{ accountStore.myProfile.userSerializer.nickname }}님의 도전 장르는... </p>
        <p class="font-title genre mb-0"><span class="font-link genre mb-0">{{ movieStore.challenge_genres.join(', ') }}</span>입니다.</p>
      </div>
      </div>
      <div v-else>
        <p class="font-title">아래 버튼을 눌러보세요</p>
      </div>
    </div>
    <hr>
    <div class="buttons">
      <button class="font-link" @click=movieStore.genreRecommend()>최애 장르 추천받기!</button>
      <button class="font-link" @click=movieStore.newGenreRecommend()>새로운 장르 도전하기!</button>
    </div>
    <hr>
    <div class="row" v-if="movieStore.recommendedList !== null">
      <img v-for="movie in movieStore.recommendedList"
      :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" 
      alt="poster" @click="movieStore.goDetail(movie.id)"
      class="col-2 mb-4 link">
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAccountStore } from '@/stores/account';
import { useMovieStore } from '../../stores/movies';
const accountStore = useAccountStore()
const movieStore = useMovieStore()

onMounted(()=>{
  movieStore.recommendCheck = null
  console.log(accountStore.myProfile.userSerializer.nickname)
})

</script>
<style scoped>
.title{
  font-size: 30px;
}

button{
  font-size: 30px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  text-decoration: none;
  margin-left: 10px;
}

.buttons {
  text-align: center;
}
img{
  border-radius: 30px;
}

img :hover{
  color: white;
}
</style>