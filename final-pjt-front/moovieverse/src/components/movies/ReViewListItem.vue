<template>
  <div class="row justify-content-md-center">
    <span class="col-1">{{ review.nickname }}</span>
    <span class="col-1">{{ review.rank }}점</span>
    <span class="col-7">{{ review.content }}</span>
    <span class="col-2 date">{{ review.updated_at.replace('T',' ').slice(0,16) }}</span>
    <span class="col-1">좋아요 {{ review.review_liked_user_count }}개</span>
    <div v-if="nickname !== review.nickname" class="likes delete offset-11 col-1 link" @click="goLike">❤</div>
    <div @click="goDelete"
    v-if="nickname===review.nickname"
    class="delete offset-11 col-1 link">🗑</div>
    <hr>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useMovieStore } from '../../stores/movies';

const route = useRoute()
const movieStore = useMovieStore()

const data = defineProps({
  review:Object,
  nickname:String
})

const goLike = function(){
  const payload = {
    reviewId: data.review.id,
    movieId: route.params.movie_id,
  }
  movieStore.likeReview(payload)
  console.log(review)
}

const goDelete = function(){
  // console.log(data.review)
  const payload = {
    content: data.review.content,
    reviewId: data.review.id,
    movieId:route.params.movie_id,
    rank: data.review.rank,
  }
  movieStore.reviewDelete(payload)
}

</script>

<style scoped>
div {
  display: flex;
  align-items: center;
  justify-content: center;
}
.date{
  font-size: 15px;
  color: ghostwhite;
  text-align: end;
}
.delete{
  width: 10px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center; 
}


</style>