<template>
  <div class="box box-background">
    <CommentListItem 
      v-for="comment in articleStore.commentSet"
      :key="comment.id"
      :comment="comment"
      :nickname="nickname"    
    />
  </div>
</template>

<script setup>
import CommentListItem from '@/components/articles/CommentListItem.vue'
import { useArticleStore } from '../../stores/article';

const articleStore = useArticleStore()

const data = defineProps({
  nickname:String
})

</script>

<style scoped>
.box-background{
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.2);
  width: 100%;
  padding: 2%;
}
</style>