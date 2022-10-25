<template>
    <div class="ContactsListDetail">
        <h1>Contact Details</h1>
        <form v-on:submit.prevent='submitDetails'>
            <label>Country Code   </label>
            <input type="text" name="country_code" v-model="country_code"> <br><br>

            <label>First Name </label>
            <input type="text" name="firstname" v-model="first_name"> <br><br>

            <label>Last Name  </label>
            <input type="text" name="lastname" v-model="last_name"> <br><br>

            <label>Phone Number      </label>
            <input type="text" name="phone_number" v-model="phone_number"><br><br>

            <label>Contact Picture   </label>
            <input type="string" name="contact_picture" ><br><br>

            <label>Is Favorite   </label>
            <input type="checkbox" name="is_favorite" ><br><br>
            <button type="submit">Add Details</button><br><br>
        </form>
        <form v-on:submit.prevent="logOut">
            <button type="submit">Log Out</button>
        </form>
        <form v-on:submit.prevent="getContact">
            <button type="submit">Get Contact</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios'

export default{
        name:"ContactsListDetailView",
        data() {
            return {
                // owner_name:localStorage.getItem("user"),
                country_code:"",
                first_name:"",
                last_name:"",
                phone_number:"",
                contact_picture:null,
                is_favorite:false
            }
        },
        methods: {
            submitDetails(e) {
                const contactFormData={
                // owner_name:localStorage.getItem("user"),
                country_code:this.country_code,
                first_name:this.first_name,
                last_name:this.last_name,
                phone_number:this.phone_number,
                contact_picture:this.contact_picture,
                is_favorite:this.is_favorite
                }
                const headers = {"Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                                    "Authorization": "Bearer "+localStorage.getItem("token")}
                console.log(contactFormData)
                axios
                .post("/api/contacts/contact/", contactFormData, {headers: headers})
                .then(response => {
                    console.log(response.data)
                    localStorage.setItem("contact",JSON.stringify(response.data))
                    this.$router.push("/contactsListDetails")
                })
                .catch(error => {console.log(error.response)
                })   
                
            },
            logOut(e) {
                // axios
                // .then(localStorage.removeItem("token") )
                localStorage.removeItem("token")
                localStorage.removeItem("user")
                alert("logging out")
                this.$router.push("/login")
            },
            getContact(e) {
                const headers = {"Access-Control-Allow-Origin": "*",
                                    "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                                    "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token",
                                    "Authorization": "Bearer "+localStorage.getItem("token")}
                const formData={
                    id:this.id
                }
                axios
                .post("/api/contacts/contact/", formData, {headers: headers})
                .then(response => {
                    console.log(response)
                    this.$router.push("/contactsListDetails")
                })
            }
            }
        }
    
    



</script>