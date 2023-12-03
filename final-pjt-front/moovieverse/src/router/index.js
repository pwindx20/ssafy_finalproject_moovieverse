import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '../stores/account'

// accounts
import firstMainPage from '@/views/main/firstMainPage.vue'
import secondMainPage from '@/views/main/secondMainPage.vue'
import SignUp from '@/views/accounts/SignUp.vue'
import LogIn from '@/views/accounts/LogIn.vue'
import MyPage from '@/views/accounts/MyPage.vue'

// movies
import RecommendPage from '@/views/movies/RecommendPage.vue'
import MoviesDetail from '@/views/movies/MoviesDetail.vue'

// articles
import ArticleMain from '@/views/articles/ArticleMain.vue'
import ArticleDetail from '@/views/articles/ArticleDetail.vue'
import ArticleCreate from '@/views/articles/ArticleCreate.vue'
import ArticleUpdate from '@/views/articles/ArticleUpdate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'firstMainPage',
      component: firstMainPage
    },
    {
      path: '/home',
      name: 'secondMainPage',
      component: secondMainPage
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/mypage/:username',
      name: 'MyPage',
      component: MyPage
    },
    {
      path: '/recommend',
      name: 'RecommendPage',
      component: RecommendPage
    },
    {
      path: '/movies/:movie_id',
      name: 'MoviesDetail',
      component: MoviesDetail
    },
    {
      path: '/articles',
      name: 'ArticleMain',
      component: ArticleMain
    },
    {
      path: '/articles/:articleId',
      name: 'ArticleDetail',
      component: ArticleDetail
    },
    {
      path: '/articles/create',
      name: 'ArticleCreate',
      component: ArticleCreate
    },
    {
      path: '/articles/:articleId/update',
      name: 'ArticleUpdate',
      component: ArticleUpdate
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useAccountStore()
  if (!store.isLogin) {
    if ((to.name !== 'firstMainPage') && (to.name !== 'SignUp') && (to.name !== 'LogIn') ) {
      window.alert('로그인이 필요합니다.')
      return {name: 'firstMainPage'}  
    }
  }
})

export default router
