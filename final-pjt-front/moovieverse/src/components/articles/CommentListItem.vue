<template>
  <div class="row justify-content-md-center">
    <span class="col-1">{{ comment.nickname }}</span>
    <span class="col-9">{{ comment.content }}</span>
    <span class="col-2 date">{{ comment.updated_at.replace('T',' ').slice(0,16) }}</span>
    <button @click="goDelete"
    v-if="nickname===comment.nickname"
    class="delete offset-11 col-1">삭제</button>
  </div>
  <hr>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '../../stores/article';

const route = useRoute()
const articleStore = useArticleStore()
const data = defineProps({
  comment:Object,
  nickname:String
})

const goDelete = function(){
  // console.log(data.review)
  const payload = {
    content: data.comment.content,
    commentId: data.comment.id,
    articleId:route.params.articleId,
  }
  articleStore.commentDelete(payload)
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

button{
  width: fit-content;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
}
</style>