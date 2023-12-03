<template>
  <div class="box">
    <ReViewListItem 
      v-for="review in movieStore.reviewSet"
      :key="review.id"
      :review="review"
      :nickname="nickname"    
    />
  </div>
</template>

<script setup>
import ReViewListItem from './ReViewListItem.vue';
import { useMovieStore } from '../../stores/movies';

const movieStore = useMovieStore()

const data = defineProps({
  nickname:String
})

</script>

<style scoped>

</style>