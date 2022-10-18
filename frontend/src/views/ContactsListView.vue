<template>
    <div class="contactsList">
      <h1>Contact List of User</h1>
      <!-- <p id="username "></p> -->
      
      <!-- <button type="button" onclick= "location.href=">Add COntact</button>
      <a :href="'/job/' + r.id"></a> -->
      <table class="table">
        <thead>
          <tr>
            <!-- <th>Contact Person</th>  |   -->
            <th>First Name</th>  |  
            <th>Last Name</th>  |  
            <th>Country Code</th>  |  
            <th>Phone Number</th>  |  
          </tr>
        </thead>

        <tbody>
          <!-- {% for contact in mem %} -->
          <tr v-for="contact in ContactDetails" :key="contact.id">
            <!-- <tr> -->
            <!-- <td>{{contact.owner}}</td> -->
            <td>{{contact.first_name}}</td>
            <td>{{contact.last_name}}</td>
            <td>{{contact.country_code}}</td>
            <td>{{contact.phone_number}}</td>
          </tr>
        </tbody>
      </table>
      <router-link :to="{ path: '/contactsListDetails' }"><button>Add Contact</button></router-link> <br><br>
      <form v-on:submit.prevent="logOut">
            <button type="submit">Log Out</button>
      </form>
          <!-- {% endfor %} -->
    </div>
</template>

<script>
import axios from 'axios'
// console.log("storage",localStorage.getItem("user"))
// document.getElementById("username").innerHTML=localStorage.getItem("user")
export default{
  name:"ContactsListView",
  data() {
    return {
      ContactDetails:[]
    }
  },
  // mounted() {
  //   axios
  //   .get('http://localhost:8000/admin/contacts/contact/', {responseType:"json"})
  //   .then((response) => {
  //     formatContacts(response.data)
  //   })

  // },
  methods: {
    formatContacts(contactData) {
      for (let key in contactData) {
        this.ContactDetails.push({...contactData[key],owner:key})
      }
    },
    logOut(e) {
      // axios
      // .then(localStorage.removeItem("token") )
      localStorage.removeItem("token")
      this.$router.push("/login")
      }
  },
}
</script>
  
