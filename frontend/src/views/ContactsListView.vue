<template>
    <div class="contactsList">
      <h1>Contact List of User</h1>
      <table class="table" border="1">
        <thead>
            <!-- <th>Owner</th> | -->
            <th>First Name</th>  
            <th>Last Name</th>   
            <th>Country Code</th>  
            <th>Phone Number</th> 
        </thead>

        <tbody>
          <tr v-for="contact in listOfContacts">
            <!-- <td>{{contact.owner}}</td> -->
            <td>{{contact.first_name}}</td>
            <td>{{contact.last_name}}</td>
            <td>{{contact.country_code}}</td>
            <td>{{contact.phone_number}}</td>
          </tr>
        </tbody>
      </table>

      <form v-on:submit.prevent="getContactsofOwner">
            <button type="submit">Get Contact</button>
      </form>
      <router-link :to="{ path: '/contactsListDetails' }"><button>Add Contact</button></router-link> <br><br>
      <form v-on:submit.prevent="logOut">
            <button type="submit">Log Out</button>
      </form>
    </div>
</template>

<script>
import axios from 'axios'
export default{
  name:"ContactsListView",
  data() {
    return {
      listOfContacts:[]
    }
  },

  methods:  {
    
    setDetailedContacts(contacts) {
      // include all data from the contact list response
    
      for (let contact in contacts) {
        this.listOfContacts.push({...contacts[contact]})
        // console.log(JSON.parse(JSON.stringify(this.listOfContacts)))
        
      }
    },

    getContactsofOwner() {
      let that = this;
      axios
        .get('http://localhost:8000/api/contacts/contact/',  
        {headers:{Accept: "application/json", "Content-Type": "application/json;charset=UTF-8", Authorization: "Bearer " + localStorage.getItem("token")}},
        {responseType:"json"})

        .then(function (response) {
          if (response.status == 200) {
            that.setDetailedContacts(response.data)
          }
        })
        .catch(error => {console.log(error.response)})
    },

    logOut(e) {
      localStorage.removeItem("token")
      localStorage.removeItem("user")
      alert("logging out")
      this.$router.push("/login")
      
  },

  mounted() {
    this.getContactsofOwner()
      }
  }
}

  
  

</script>
  
