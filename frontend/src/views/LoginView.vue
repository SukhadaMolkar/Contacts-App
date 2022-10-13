<template>
    <div class="Login">
        <h1>Log In</h1>
        <form v-on:submit.prevent="submitDetails">
            <label>Username</label>
            <input type="text" name="username" v-model="username"> <br><br>
            <label>Password</label>
            <input type="text" name="password" v-model="password"> <br><br>
            <button type="submit">LogIn</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
// import RegisterViewVue from './RegisterView.vue'
    export default{
        name:"LoginView",
        data() {
            return{
                    username:"",
                    password:""
            }
        },
        methods:{
            submitDetails(e) {
                const formData={
                    username:this.username,
                    password:this.password
                }
                console.log(formData)
                axios
                .post("/api/acc/login/",formData,{"headers": { 
                                    "Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
                                }})
                                .then(response => {
                    console.log(response)
                    this.$router.push("/login")
                })
                .catch(error => {console.log(error.response)
                })   
            }
        }
    }
</script>