import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from '@/stores/account'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const accountStore = useAccountStore()
  const token = accountStore.token
  const route = useRoute()
  const router = useRouter()

  const movie = ref(null)
  const movie_id = ref(null)
  const movie_watch = ref(null)
  const searchedList = ref(null)
  const favorite_genres = ref(null)
  const challenge_genres = ref(null)
  const recommendedList = ref(null)
  const reviewSet = ref(null)
  const randomReview10 = ref(null)
  const recommendCheck = ref(null)

  
  // 영화 조회+ 페이지 이동
  const goDetail = function(movie_id){
    axios({
      method: 'get',
      url: `${API_URL}/movies/${movie_id}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then (res => {
      movie.value = res.data
      reviewSet.value = res.data.review_set
      router.push({name:'MoviesDetail', params:{movie_id: movie_id}})
    })
    .catch (err=>console.log(err))
  }


  // 영화 조회
  const getMovie = function (movieId) {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${movieId}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {
      movie.value = res.data
      reviewSet.value = res.data.review_set
    })
    .catch(err => console.log(err))
  }


  // 보고싶어요
  const movieWatch = function (movieId) {
    axios({
      method: 'post',
      url: `${API_URL}/movies/${movieId}/watch/`,
      headers: {
        Authorization: `Token ${token}`
      },
    })
    .then(res =>{
      console.log(res.data.movie_watch)
      movie_watch.value = res.data.movie_watch
      getMovie(movieId)
    })
    .catch(err => console.log(err))
  }  

  // 선호 장르 영화 받아오기
  const genreRecommend = function() {
    axios({
      method:'get',
      url: `${API_URL}/movies/recommend/prefer/`,
      headers: {
        Authorization: `Token ${token}`
      },
    })
    .then(res=>{
      console.log(res.data)
      favorite_genres.value = res.data.favorite_genres
      recommendedList.value = res.data.favorite_genres_movie
      recommendCheck.value = 1
    })
    .catch(err=>console.log(err))
  }

    

    // 비선호 장르 영화 받아오기
    const newGenreRecommend = function() {
      axios({
        method:'get',
        url: `${API_URL}/movies/recommend/nprefer/`,
        headers: {
          Authorization: `Token ${token}`
        },
      })
      .then(res=>{
        console.log(res.data)
        challenge_genres.value = res.data.challenge_genres
        recommendedList.value = res.data.challenge_genres_movie
        recommendCheck.value = 2
    })
      .catch(err=>console.log(err))
    }


  // 영화 검색
  const searchMovie = function(searched){
    axios({
      method:'post',
      url:`${API_URL}/movies/search/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data:{
        'searched':searched
      }
    })
    .then(res=>{
      searchedList.value = res.data
    })
    .catch(err=>console.log(err))
  }


  // 리뷰 생성
  const reviewCreate = function(payload) {
    const { content, movieId, rank } = payload
    axios({
      method:'post',
      url: `${API_URL}/movies/${movieId}/reviews/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      },
      data : {
        content,
        rank
      }
    })
    .then(res =>{
      goDetail(movieId)
    })
  }
  // 리뷰 좋아요
  const likeReview = function(payload){
    const {reviewId, movieId} = payload
    axios({
      method: 'post',
      url: `${API_URL}/movies/${movieId}/reviews/${reviewId}/likes/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      },      
    })
    .then (res=>{
      goDetail(movieId)
    })
  }
  // 리뷰 삭제
  const reviewDelete = function(payload) {
    const {reviewId, movieId, content, rank} = payload
    axios({
      method:'delete',
      url: `${API_URL}/movies/${movieId}/reviews/${reviewId}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      },
      data : {
        content,
        rank
      }
    })
    .then(res =>{
      goDetail(movieId)
    })
  }


  // 랜덤 리뷰 조회
  const getReview = function(){
    axios({
      method:'get',
      url:`${API_URL}/movies/reviews/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      },
    })
    .then(res=>{
      randomReview10.value = res.data
    })
  }


  return { API_URL, movie, movie_id, movie_watch, searchedList, 
    reviewSet, randomReview10, recommendedList,
    favorite_genres, challenge_genres,recommendCheck,
    goDetail, getMovie, movieWatch, searchMovie, genreRecommend, newGenreRecommend,
    reviewCreate, getReview, reviewDelete, likeReview,
    }
  })
