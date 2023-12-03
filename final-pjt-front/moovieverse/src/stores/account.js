import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const username_onlogin = ref(null)
  const profile = ref(null)
  const myProfile = ref(null)
  const isFollowed = ref(null)
  const everything = ref(null)

  // 로그인 유무 확인
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 내 프로필 가져오기
  const getMyProfile = function(){
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${username_onlogin.value}/profile/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
    .then(res => {
      myProfile.value = res.data
     
    })
    .catch(err => console.log(err))
  }
  
  // 내 프로필 가져오기
  const goMyProfile = function(){
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${username_onlogin.value}/profile/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
    .then(res => {
      myProfile.value = res.data
     
    })
    .then(res=>{
      router.push({name:'MyPage', params:{username:username_onlogin.value}})
    })
    .catch(err => console.log(err))
  }


  // 프로필 가져오기
  const getProfile = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${username}/profile/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
    .then(res => {
      profile.value = res.data.userSerializer
      everything.value = res.data
      console.log(everything.value)
    })
    .catch(err => console.log(err))
  }

  // 프로필로 가기
  const goProfile = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${username}/profile/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
    .then(res => {
      profile.value = res.data.userSerializer
      everything.value = res.data
    })
    .then(res=>{
      router.push({name:'MyPage', params:{username:username}})
    })
    .catch(err => console.log(err))
  }

  
  // 팔로우
  const follow = function (userId, username) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/${userId}/follow/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
    .then(res =>{
      isFollowed.value = res.data.isFollowed
      getProfile(username)
      // console.log(res.data.isFollowed)
    })
    .catch(err => console.log(err))
  }


  // 회원가입
  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    // const email = 
    const email = payload.email
    const nickname = payload.nickname

    console.log(payload)
    axios({
      method: 'post',
      url: `${API_URL}/accounts/registration/`,
      data: {
        username, password1, password2, email, nickname
      }
    })
    .then(res => {
      console.log('회원가입완료')
    })
    .catch(err => console.log(err))
  }


  // 로그인
  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      token.value = res.data.key
      username_onlogin.value = username
      console.log(username_onlogin.value)
      router.push({name: 'secondMainPage'})
    })
    .catch(err => console.log(err))
    
  }


  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(res => {
        token.value = null; 
        username_onlogin.value = null
        // localStorage.removeItem('account')
        // location.reload()
      })
      .catch(err => console.log(err));
  };
  
  
  return { token, username_onlogin, profile, myProfile, isFollowed, isLogin, everything,
    goMyProfile, getMyProfile,goProfile, getProfile, follow,
    signUp, logIn, logOut
 }
}, {persist: true} )