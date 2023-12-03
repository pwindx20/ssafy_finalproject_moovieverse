<template>
  <div class="box basic-background">
    <span class="link" @click="goCategory">{{ articleStore.article?.category.name }}></span>
    <p class="" v-if="articleStore.article?.movie !== null"> [ {{ articleStore.article?.movie.title }} ] </p>
    <h3>{{ articleStore.article?.title }}</h3>
    <div class="box1">
      <span @click="goProfile" class="item article-small">{{ articleStore.article?.nickname }}</span>
      <span class="item article-small">{{ articleStore.article?.created_at.replace('T',' ').slice(0,16) }}</span>
    </div>
    <hr>
    <div class="box2">
      <span class="item article-small">댓글💬 {{ articleStore.article?.comment_count }}개</span>
      <span class="item article-small">좋아요❤{{ articleStore.article?.article_liked_user_count }}개</span>
    </div>
    <hr>
    <div class="content">
      {{ articleStore.article?.content }}
    </div>
    <hr>
    <div class="box3">
      <div v-if="articleStore.article?.username!==accountStore.myProfile?.userSerializer.username" class="likes" @click="likeArticle">❤</div>
      <div v-else>
        <button class="item button" @click="updateArticle">수정</button>
        <button class="item button" @click="deleteArticle">삭제</button>
      </div>
  </div>
    <hr>
    <div class="box4">
      <span class="item">댓글💬 {{ articleStore.article?.comment_count }}개</span>
      <span class="item">좋아요❤{{ articleStore.article?.article_liked_user_count }}개</span>
      <hr>
    </div>
    <div class="box5">
      <CommentCreate 
      :nickname="accountStore.myProfile?.userSerializer.nickname"
      />
      <p></p>
      <div v-if="articleStore.article?.comment_set">
        <CommentList 
        :comment_set="articleStore.article.comment_set"
        :nickname="accountStore.myProfile?.userSerializer.nickname"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import CommentList from '@/components/articles/CommentList.vue'
import CommentCreate from '../../components/articles/CommentCreate.vue';
import { useAccountStore } from '../../stores/account';
import { useArticleStore } from '../../stores/article';
import { useRouter, useRoute } from 'vue-router'
import { onMounted } from 'vue';
const accountStore = useAccountStore()
const articleStore = useArticleStore()
const router = useRouter()
const route = useRoute()

onMounted(()=>{
  articleStore.getDetail(route.params.articleId)
  accountStore.getMyProfile()
})

const goCategory = function(){
  console.log(articleStore.article.category.id)
  articleStore.goCategory(articleStore.article.category.id)
}

const goProfile = function(){
  console.log(articleStore.article.username)
  router.push({name:'MyPage', params:{username:articleStore.article.username}})
}

const likeArticle = function(){
  articleStore.likeArticle(route.params.articleId)
}

const updateArticle = function(){
  router.push({name:'ArticleUpdate', params:{articleId:route.params.articleId}})  
}

const deleteArticle = function(){
  articleStore.deleteArticle(route.params.articleId)
}

</script>

<style scoped>
.article-small{
  font-size: 15px;
  color: ghostwhite;
}
.item{
  margin: 5px;
}
.box3{
  text-align: end;
}
.box4{
  text-align: end;
}
.likes{
  color: red;
  text-align: center;
  font-size: 30px;
  cursor: pointer;
}
.box5{
  display: flex;
  flex-direction: column;
}

.button{
  width: fit-content;
  font-size: 20px;
  color: rgb(255, 255, 255);
  border: 1px rgb(255, 255, 255) solid;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  padding-left: 10px;
  padding-right: 10px;
  text-decoration: none;
  margin-left: 10px;
}
</style>