<template>
  <div class="container">
    <p class="row link" @click="goDetail(article.id)">
      <span class="item col-1 article-id">{{ article.id }}</span>
      <span class="item col-5">
        {{ article.title }}
        <span class="comment">[{{ article.comment_count }}]</span>
      </span>
      <span class="item col-2 article-small">{{ article.nickname }}</span>
      <span class="item col-3 article-small">{{ createdAt }}</span>
      <span class="item col-1 article-likes">
        <span v-if="article.review_liked_user_count">❤️</span>
        <span v-else>🤍</span>
        {{ article.review_liked_user_count }}
      </span>
    </p>
  </div>
</template>

<script setup>
import { useArticleStore } from '../../stores/article';

const articleStore = useArticleStore()

const articleData = defineProps({
  article:Object
})

const goDetail = function(article_id){
  articleStore.goDetail(article_id)  
}

const createdAt = articleData.article.created_at.replace('T',' ').slice(0,16);

</script>

<style scoped>
.container {
  color: white;
  font-size: 20px;
}
.article-small{
  color: ghostwhite;
  font-size: 17px;
  text-align: center;
}
.comment{
  color: red;
  font: bolder;
}
.article-likes{
  text-align:end;
}
.link{
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>