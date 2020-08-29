<template>
<div class="main-nav">
    <nav>
        <branding></branding>
        <search></search>
    </nav>
</div>
</template>

<script>
import search from '../1-molecule/search.vue'
import branding from '../1-molecule/branding.vue'

export default {
  name: 'Nav Bar',
  components: {
    search,
    branding
  }
};
</script>

<style scoped>
h1 {
    margin: 0;
    padding: 10px;
}

.main-nav {
    width: 100%;
    background: black;
    color: white;
}

nav {
    width: 80%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>