<template>
    <div class="blog-wrapper">
        <p>blog Index</p>
        <ul v-if="list.length">
            <li v-for="item in list" :key="item.id">
                <p>{{item.body}}</p>
            </li>
        </ul>
        <div v-else>
            <p>暂无文章列表</p>
            <button @click="$router.push('/create')">发表一篇吧</button>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            list: []
        }
    },
    async created() {
        try {
            const rst = await this.$post('/articles')
            this.list = rst.data.list || []
        } catch(err) {

        }
    }
}
</script>