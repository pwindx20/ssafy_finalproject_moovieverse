<template>
  <div class="container">
    <div>
      <p class="font-title doctitle">게시글 작성</p>
      <hr>
    </div>
    <form class="row" @submit.prevent="createArticle">
      <div class="col-8">
        <div class="item">
          <select class="option" v-model="category" name="category" id="category">
            <option disabled value="">게시판을 선택해 주세요.</option>
            <option value=2>영화감상</option>
            <option value=3>자유게시판</option>
            <option value=4>이벤트</option>
          </select>
          <!-- <form class="option"  > -->
          <div v-if="category==2">
            <input v-model="searched" type="text" placeholder="영화 검색">
            <input @click="search" type="button" value="검색">
            <select v-model="movie" name="movie" id="movie">
              <option disabled value="" selected>검색결과</option>
              <option class="item" 
              v-for="filtermovie in movieStore?.searchedList"
              :key="filtermovie.id"
              :value="filtermovie.id"
              >{{ filtermovie.title }}</option>
            </select> 
          </div>
        </div>
        <input class="col-12 item title" v-model="title" type="text" id="title" placeholder="제목입력">
        <textarea class="col-12 item content" v-model="content" name="content" id="content" placeholder="내용을 적어주세요."></textarea>
      </div>
      <div class="col-4 right">
        <p class="option"> ㅤ</p>
        <input class="item" type="submit" value="입력">
        <div class="spoiler">
          <label class="item" for="isSpoiler">스포일러</label>
          <input v-model="isSpoiler" type="checkbox" name="isSpoiler" id="isSpoiler">
          <p class="item">스포일러인가요? 체크박스에 체크하시면 저희가 가려드릴게요.</p>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAccountStore } from '../../stores/account';
import { useArticleStore } from '../../stores/article';
import { useMovieStore } from '../../stores/movies';
const accountStore = useAccountStore()
const articleStore = useArticleStore()
const movieStore = useMovieStore()

const title = ref(null)
const movie = ref(null)
const category = ref('')
const content = ref(null)
const isSpoiler = ref(false)
const searched = ref(null)

const createArticle = function() {
  const payload = {
    title : title.value, 
    movie : movie.value,
    category : Number(category.value),
    content : content.value, 
    isSpoiler : isSpoiler.value,
    isNotice : false
  }
  articleStore.createArticle(payload)
}

const search = function(){
  movieStore.searchMovie(searched.value)
}

</script>

<style scoped>
.container {
  color: white;
}
.item{
  margin : 10px;
}
.option{
  font-size: 20px ;
}
.content{
  height: 50vh;
}

.spoiler{
  border: 1px solid black;
  border-radius: 15px;
  background-color: rgba(255, 255, 255, 0.5);
  margin: 20px;
}

.right{
  display: flex;
  flex-direction: column;
}
.doctitle{
  font-size: 30px;
}
</style>
