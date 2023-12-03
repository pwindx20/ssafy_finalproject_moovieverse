<template>
  <div>
    <form class="row" @submit.prevent="goCreate">
      <span class="col-1 item">{{ nickname }}</span>
      <input class="col-9 comment item" placeholder="댓글을 입력하세요." v-model="content" type="text">
      <input class="col-1 button item" type="submit" value="입력">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useAccountStore } from '../../stores/account';
import { useArticleStore } from '../../stores/article';
const articleStore = useArticleStore()
const accountStore = useAccountStore()
const route = useRoute()
const content = ref(null)

defineProps({
  nickname: String
})

const goCreate = function(){
  const payload = {
    content:content.value,
    articleId:route.params.articleId
  }
  articleStore.commentCreate(payload)
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