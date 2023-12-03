<template>
  <div class="box basic-background">
    <div>
      <div class="row">
        <div class="col-1 category">
          <p class="category-link font-title" @click="goMain">전체 게시글</p>
          <p class="category-link font-title" @click="goCategory(1)">공지사항</p>
          <p class="category-link font-title" @click="goCategory(2)">영화리뷰</p>
          <p class="category-link font-title" @click="goCategory(3)">자유게시판</p>
          <p class="category-link font-title" @click="goCategory(4)">이벤트</p>
        </div>
        <div class="col-9">
          <ArticleList />
        </div>
        <button class="font-title button" @click="goCreate">게시물 작성</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import ArticleList from '@/components/articles/ArticleList.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'

const articleStore = useArticleStore()
const router = useRouter()

// onMounted(()=>{
//   articleStore.getArticles()
// })

const goMain = function(){
  articleStore.getArticles()
}

const goCategory = function(category_id){
  articleStore.goCategory(category_id)
}

const goCreate = function(){
  router.push({name:'ArticleCreate'})
}

</script>

<style  scoped>
.category{
  color: #ffffff;
  border: 1px gainsboro solid;
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  text-decoration: none;
  height: fit-content;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.category-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: white;
  text-decoration: none;
  cursor: pointer;
}

.category-link:hover{
  background-color: #ffffff;
  color: rgba(4, 20, 44, 0.5);
  border-radius: 45px;
  width: 100%;
  border: #ffffff 2px solid;
}

.button{
  position: absolute;
  top: 13%;
  right: 13%;
  width: fit-content;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px gainsboro solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 10px;
  text-decoration: none;
  margin-left: 10px;
}

.button:active, .button:hover{
  background-color: #ffffff;
  color: rgba(4, 20, 44, 0.5);
  border-radius: 45px;
  border: #ffffff 2px solid;
}
</style>