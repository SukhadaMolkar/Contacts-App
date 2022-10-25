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
            <!-- <th>Owner</th> | -->
            <th>First Name</th>  |  
            <th>Last Name</th>  |  
            <th>Country Code</th>  |  
            <th>Phone Number</th>  |  
          </tr>
        </thead>

        <!-- <tbody> -->
          <!-- {% for contact in mem %} -->
          <tr v-for="contact in listOfContacts" :key="contact">
          <!-- <tr v-for="(contact, index) in listOfContacts" :key="index"> -->
            <!-- <tr> -->
            <!-- <td>{{contact.owner}}</td> -->
            <!-- <td>{{contact.owner}}</td> -->
            <td>{{contact.first_name}}</td>
            <td>{{contact.last_name}}</td>
            <td>{{contact.country_code}}</td>
            <td>{{contact.phone_number}}</td>
          </tr>
        <!-- </tbo+dy> -->
      </table>
      <form v-on:submit.prevent="getContactsofOwner">
            <button type="submit">Get Contact</button>
      </form>
      <router-link :to="{ path: '/contactsListDetails' }"><button>Add Contact</button></router-link> <br><br>
      <form v-on:submit.prevent="logOut">
            <button type="submit">Log Out</button>
      </form>
          <!-- {% endfor %} -->
    </div>
</template>

<script>
// import { apiHost} from '../config'
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
      console.log(contacts,"inside set")
    
      for (let contact in contacts) {
        // let listOfDetails=[]
        console.log(contact,"key")
        let listOfDetails=Object.values(contacts[contact])

        console.log(listOfDetails,"final list")
        // this.listOfContacts.push(listOfDetails)

        this.listOfContacts.push({...listOfDetails})
      }
      console.log(this.listOfContacts, "list of contacts values only")
    },

    getContactsofOwner() {
      let that = this;
      axios
        .get('http://localhost:8000/api/contacts/contact/',  
        {headers:{Accept: "application/json", "Content-Type": "application/json;charset=UTF-8", Authorization: "Bearer " + localStorage.getItem("token")}},
        {responseType:"json"})

        .then(function (response) {
          if (response.status == 200) {
            console.log("response 200",response.data)
            // this.setDetailedContact(response.data);
            that.setDetailedContacts(response.data)
          }
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

  created() {
    console.log("entered in mounted")
    console.log("this",this)
    // this.getContactsofOwners();
    this.getContactsofOwner()
    
        // this.ContactDetails.push({...contactData[key],owner:key})
      }
  }
}

  
  

</script>
  
