<template>
    <div class="Login">
        <h1>Log In</h1>
        <form v-on:submit.prevent="submitDetails">
            <label>Username</label>
            <input type="text" name="username" v-model="username"> <br><br>
            <label>Password</label>
            <input type="password" name="password" v-model="password"> <br><br>
            <button type="submit">LogIn</button>
            <!-- <router-link :to="{ path: '/contactsList' }"><button type="submit">LogIn</button></router-link> -->
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
                    password:"",
                    token: ""
                }
        },
        methods:{
            submitDetails(e) {
                const formData={
                    username:this.username,
                    password:this.password
                }
                console.log(formData)
                const headers={ 
                                    "Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
                                }
                axios
                .post("/api/acc/login/",formData,{"headers": headers})
                .then(response => {
                    localStorage.setItem("user",this.username)
                    localStorage.setItem("token",response.data.token)
                    alert("you are logged in")
                    
                    this.$router.push("/login")
                    this.$router.push("/contactsList")
                })
                .catch(error => {console.log(error.response)
                    // alert(console.log(error.response.data.detail))
                    console.log(this.username)
                    if (this.username=="") {
                        alert("Username is Undefined")
                    } else if (this.password=="") {
                        alert("Password is missing")
                    } else {
                        alert("Invalid Credentials. You must register first")
                        this.$router.push("/register")
                    }
                })   
            }
        }
    }
</script>