<template>
    <div class="center-content">
        <p v-if="error">{{error}}</p>
        <form action="/auth/login" method="POST">
        <input type="text" placeholder="用户名" name="user_nm" v-model="user_nm"/>
        <input type="password" placeholder="密码" name="user_pwd" v-model="user_pwd"/>
        <button :disabled="disabled" @click="evtSubmit">提交</button>
        </form>
    </div>
</template>
<script>
export default {
  data() {
    return {
        disabled: false,
        user_nm: "",
        user_pwd: "",
        error: ""
    };
  },
  methods: {
    async evtSubmit(ev) {
        ev.preventDefault();
        this.disabled = true;
        try {
            const rst = await this.$post("/auth/login", {
                user_nm: this.user_nm,
                user_pwd: this.user_pwd
            });
            if (rst.data.error) {
                this.error = rst.data.error
            } else {
                // this.$router.push('/')
                window.location.href = '/'
            }
        } catch (err) {
            console.log(err);
        }
        this.disabled = false;
    }
  }
};
</script>