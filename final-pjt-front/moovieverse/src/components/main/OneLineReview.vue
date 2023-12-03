<script>
import { defineComponent } from 'vue'
import { Carousel, Pagination, Slide } from 'vue3-carousel'

import 'vue3-carousel/dist/carousel.css'

export default defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
  },
})

</script>
<template>
  
  <Carousel :items-to-show="3.95" :wrap-around="true">
    <Slide v-for="review in movieStore.randomReview10" :key="review.id">
      <div class="carousel__item">
        <div class="review-box" style="width: 25rem;">
            {{ review.content }}         
            <a @click="goDetail(review)" class="font-title detailBtn">보러가기</a>
        </div>
      </div>
    </Slide>

    <template #addons>
      <Pagination />
    </template>
  </Carousel>
</template>



<script setup>
import { onMounted } from 'vue';
import { useMovieStore } from '@/stores/movies'

const movieStore = useMovieStore()
onMounted(()=>{
  movieStore.getReview()
})

const goDetail = function(review){
  movieStore.goDetail(review.movie)  
}
</script>



<style scoped>
.review-box{
  position: relative;
  height: 300px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 20px;
  background-color: rgba(4, 20, 44, 0.5);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content:space-around;
  align-items: center;
}
.detailBtn{
  position: absolute;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px;
  bottom: 30px;
  text-decoration: none;
}
</style>