<template>
<div>
  <navbar></navbar>
  <subnav></subnav>
  <homeList></homeList>
</div>
</template>

<script>
import navbar from '../2-components/navbar.vue'
import subnav from '../2-components/subnav.vue'
import homeList from './homeList.vue'

export default {
  name: 'HomePage',
  components: {
    navbar,
    subnav,
    homeList
  }
}
</script>

<style>

</style>
