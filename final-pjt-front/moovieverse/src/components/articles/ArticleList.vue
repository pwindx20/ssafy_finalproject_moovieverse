<template>
  <div>
    <p class="row mb-0">
      <span class="item col-1 article-id"></span>
      <span class="item col-5">제목</span>
      <span class="item col-2 article-nickname">작성자</span>
      <span class="item col-3 article-small">작성시간</span>
      <span class="item col-1 article-likes">좋아요</span>
    </p>
    <hr class="mt-0">
  </div>
  <div>
    <ArticleListItem 
    v-for="article in articleStore.articles"
    :article="article"
    />
    <hr>
  </div>
</template>

<script setup>
import ArticleListItem from './ArticleListItem.vue';
import { useArticleStore } from '../../stores/article';
import { RouterLink } from 'vue-router';

const articleStore = useArticleStore()

</script>

<style scoped>
.row{
  text-align: center;
  font-size: 17px;
}
</style>