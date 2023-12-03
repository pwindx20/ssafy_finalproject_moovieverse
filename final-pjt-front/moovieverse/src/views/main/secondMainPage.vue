<template>
  <div class="box basic-background">
    <article>
      <div>
        <p class="font-link">오직 리뷰만으로 영화를 판단한다!</p>
        <div>
          <OneLineReview />
        </div>
      </div>
      <hr>
      <div>
        <p class="font-link">찾으시는 영화가 있나요?</p>
        <div class="search-bar row gap-3">
          <input class=" col-6" v-model="searched" type="text" placeholder="영화 제목을 입력해주세요.">
          <button class="col-1" @click="movieStore.searchMovie(searched)">검색</button>
        </div>
        <hr>
        <div class="search-result" v-show="movieStore.searchedList !== null">
          <p class="font-title">검색결과</p>
          <div v-if="movieStore.searchedList?.length===0">
            <p>검색결과가 없습니다.</p>
          </div>
          <div class="row">
            <div
            class="col-2 search-result-item"
            v-for="filtermovie in movieStore?.searchedList"
            :key="filtermovie.id"
            @click="movieStore.goDetail(filtermovie.id)"
            >
              <img :src="`https://image.tmdb.org/t/p/w500/${filtermovie.poster_path}`" alt="poster">
              {{ filtermovie.title }}
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup>
import OneLineReview from '../../components/main/OneLineReview.vue'
import { ref, onMounted } from 'vue'
import { useAccountStore } from '@/stores/account'
import { useMovieStore } from '../../stores/movies'

const accountStore = useAccountStore()
const movieStore = useMovieStore()

const searched = ref(null)

onMounted(()=>{
  accountStore.getMyProfile()
})

</script>

<style scoped>

button {
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px;
  bottom: 30px;
  text-decoration: none;
}
img{
  width: 16rem;
  height: 23rem;
  border-radius: 15px;
}
.search-result-item{
  display: flex;
  flex-direction: column;

}
</style>