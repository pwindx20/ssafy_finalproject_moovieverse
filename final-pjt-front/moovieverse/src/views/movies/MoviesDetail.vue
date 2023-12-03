<template>
  <div class="box basic-background">
    <div>
      <p class="font-title movie-title">{{ movieStore.movie?.title }}</p>
      <div>
        <div class="row">
          <div class="col-4">
            <img :src="`https://image.tmdb.org/t/p/w500/${movieStore.movie?.poster_path}`" alt="poster">
          </div>
          <div class="col-8">
            <div>
              <p class="my-0">
                {{ movieStore.movie?.release_date }} | 
                {{ countries }} 
              </p>
              <div>
                <span v-for="genre in movieStore.movie?.genres" :key="genre.id" >
                  {{ genre.name }} |
                </span>
                {{ movieStore.movie?.runtime }}분
              </div>
              <p class="font-title tagline my-5" v-if="movieStore.movie?.tagline">"{{ movieStore.movie?.tagline }}" </p>
              <div>
                {{ movieStore.movie?.overview }}
              </div>
            </div>
            <div>
              <button class="button1" @click="movieWatch" v-if="!movieStore.movie_watch">보고싶어요</button>
              <button class="button2" @click="movieWatch" v-else>✔</button> 
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="box5">
      <ReviewCreate 
      :nickname="accountStore.Myprofile?.userSerializer.nickname"
      />
      <hr>
      <p class="my-0">💬{{ movieStore.movie?.review_count }}개의 리뷰가 있어요</p>
      <hr class="mt-1">
      <div v-if="movieStore.movie?.review_set">
        <ReviewList 
        :review_set="movieStore.movie?.review_set"
        :nickname="accountStore.Myprofile?.userSerializer.nickname"
        />
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { useMovieStore } from '../../stores/movies';
import { useAccountStore } from '@/stores/account'
import ReviewCreate from '@/components/movies/ReviewCreate.vue'
import ReviewList from '@/components/movies/ReViewList.vue'

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const route = useRoute()
const router = useRouter()
const countries = computed(() => {  
  if (movieStore.movie) {
    const payload = movieStore.movie.production_countries
    console.log(1, movieStore.movie)
    const test = payload.replace("[", "").replace("]", "").replaceAll("'", "").replaceAll(",", " ")
    console.log(2, test)
    return test 
  }
 
  return ''
})

onMounted(() => {
  movieStore.getMovie(route.params.movie_id)
  accountStore.getMyProfile()
})

const movieWatch = function(){
  movieStore.movieWatch(route.params.movie_id)
}


</script>

<style scoped>

.tagline {
  font-size: 30px;
}

.box5{
  display: flex;
  flex-direction: column;
}
.movie-title{
  font-size: 40px;
}
img{
  width: 100%;
}

.button1{
  position: absolute;
  top: 13%;
  right: 13%;
  width: 150px;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  text-decoration: none;
  margin-left: 10px;
}
.button2{
  position: absolute;
  top: 13%;
  right: 13%;
  width: 150px;
  font-size: 20px;
  padding: 10px;
  text-decoration: none;
  margin-left: 10px;
  color: rgb(4, 20, 44);
  border: 1px rgb(4, 20, 44) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.8);
}

</style>