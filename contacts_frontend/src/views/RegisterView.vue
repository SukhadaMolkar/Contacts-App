<template>
    <div class="Register">
        <h1>Register Yourself</h1>
        <form v-on:submit.prevent='submitDetails'>
            <label>Username   </label>
            <input type="text" name="username" v-model="username"> <br><br>
            <label>First Name </label>
            <input type="text" name="firstname" v-model="firstname"> <br><br>
            <label>Last Name  </label>
            <input type="text" name="lastname" v-model="lastname"> <br><br>
            <label>  Email      </label>
            <input type="email" name="email" v-model="email"><br><br>
            <label>Password   </label>
            <input type="password" name="password" v-model="password"><br><br>
            <button type="submit">Register</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
// import { response } from 'express'

    export default{
        name:"RegisterView",
        data() {
            return {
                username:'',
                firstname:'',
                lastname:'',
                email:'',
            }
        },
        methods: {
            submitDetails(e) {
                const formData={
                    username:this.username,
                    firstname:this.firstname,
                    lastname:this.lastname,
                    email:this.email,
                    password:this.password
                }
                axios
                .post("/api/acc/register/",FormData, {"headers": { 
                                    "Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
                                }})
                .then(response => {
                    console.log(response)
                    this.$router.push("/register")
                })
                .catch(error => {console.log(error.response)
                })   
            }
            
        }   

    }
</script>