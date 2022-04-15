<template>
  <v-app>
    <!-- <v-navigation-drawer app width="400"> -->
    <v-navigation-drawer
      width="220"
      v-model="drawer"
      class="pa-0"
      app
    >
      <v-sheet
        color="blue lighten-4"
        class="pa-0"
      >
        <v-list>
            <v-list-item>
                <v-list-item-avatar color="blue" size="60">
                    <span class="white--text text-h5">YW</span>
                </v-list-item-avatar>
            </v-list-item>
            <v-list-item link>
                <v-list-item-content>
                    <v-list-item-title class="text-h6" >
                        Yanchao Wang
                    </v-list-item-title>
                </v-list-item-content>

                <v-list-item-action>
                    <v-icon>mdi-menu-down</v-icon>
                </v-list-item-action>
            </v-list-item>
        </v-list>
      </v-sheet>

      <v-divider></v-divider>

      
      <v-list>
        <v-list-item
          v-for="[icon, text, route] in links"
          :key="icon"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content @click="$router.replace(route).catch(err=>{})">
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!-- </v-navigation-drawer> -->

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer
      app
      color="transparent"
      height="72"
      inset
    >
    </v-footer>
  </v-app>
</template>

<script>
  // import DashBoard from './pages/DashBoard'
import { io } from "socket.io-client";

export default {
    name: 'App',
    components: {
    // HelloWorld,
    // CardsStack,
    // DashBoard
    },
    data: () => ({ 
      drawer: null,
      links: [
            ['mdi-message-text', 'Messages', '/messages'],
            ['mdi-account-multiple', 'Square', '/about'],
      ]}),
    methods: {
      reserve () {
        this.loading = true
        setTimeout(() => (this.loading = false), 2000)
      },
    },
    mounted(){
      const socket = io('http://localhost:8080',{
        transports: ['websocket','polling'],
        // transports: ["polling"],
        upgrade: true,
        rejectUnauthorized: false
      })
      socket.on("connect_error", (err) => {
        console.log(err);
      });
      socket.on("connect", (resp) => {
        console.log(socket.id);
        console.log(resp); 
      });
      console.log(io)
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
