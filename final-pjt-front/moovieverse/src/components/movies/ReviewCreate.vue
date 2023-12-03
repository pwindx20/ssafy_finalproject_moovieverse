<template>
  <div>
    <form class="row gap-3" @submit.prevent="goCreate">
      <span class="col-1 item">{{ nickname }}
      </span>
      <input class="col-7 comment item" placeholder="한 줄 평을 입력하세요." v-model="content" type="text">
      <select class="col-2 rank" v-model="rank" placeholder="별점">
        <option>별점 선택</option>
        <option value="1">🌟</option>
        <option value="2">🌟🌟</option>
        <option value="3">🌟🌟🌟</option>
        <option value="4">🌟🌟🌟🌟</option>
        <option value="5">🌟🌟🌟🌟🌟</option>
      </select>
      <input class="col-1 button item" type="submit" value="입력">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '../../stores/account';
import { useArticleStore } from '../../stores/article';
import { useMovieStore } from '../../stores/movies';
const articleStore = useArticleStore()
const accountStore = useAccountStore()
const movieStore = useMovieStore()
const route = useRoute()
const content = ref(null)
const rank = ref(null)

defineProps({
  nickname: String
})

const goCreate = function(){
  const payload = {
    content:content.value,
    movieId:route.params.movie_id,
    rank:rank.value,
  }
  movieStore.reviewCreate(payload)
  content.value=null
}
</script>

<style scoped>
/* .comment{
  width: 50%;
} */
.button{
  width: fit-content;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding-left: 10px;
  padding-right: 10px;
  margin-left: 1%;
  text-decoration: none;
}
.row{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>