<template>
    <div class="center-content">
        <form action="/auth/register" method="POST">
            <input type="text" placeholder="用户名" name="user_nm">
            <input type="password" placeholder="密码" name="user_pwd">
            <button>提交</button>
        </form>
    </div>
</template>