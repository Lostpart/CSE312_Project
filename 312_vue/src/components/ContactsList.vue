<template>
<vmain>
      <!-- <v-list
        class="pl-14"
        shaped
        width="30%"
      >
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-content>
            <v-list-item-title>Item {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list> -->


      <v-spacer></v-spacer>

    <v-row>
      <v-col cols = 4>
          <v-list subheader max-height="10">
          <v-list-item
            v-for="chat in recent"
            :key="chat.title"
            link
          >
            <v-list-item-avatar>
              <v-img
                :alt="`${chat.title} avatar`"
                :src="chat.avatar"
              ></v-img>
            </v-list-item-avatar>

            <v-list-item-content @click="changeCurrentFriend(chat)">
              <v-list-item-title v-text="chat.title"></v-list-item-title>
            </v-list-item-content>

            <v-list-item-icon>
              <v-icon :color="chat.active ? 'deep-purple accent-4' : 'grey'">
                mdi-message-outline
              </v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list>
      </v-col>      
      <v-col>
      <v-toolbar
        color="blue"
        dark
      >
        <v-avatar>
          <v-img
            :src="currentAvatarSrc"
          ></v-img>
        </v-avatar>
        <v-toolbar-title>{{currentFriend}}</v-toolbar-title>

        <v-divider
          class="mx-4"
          vertical
        ></v-divider>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </v-toolbar>

        <v-sheet
          color="white"
          elevation="1"
          min-height="335"
          width="100%"
        >
        </v-sheet>
        <v-sheet
          color="white"
          width="100%"
        >
          <v-textarea
            name="input-7-1"
            filled
            label="Message"
            placeholder="Enter message here"
          >
          </v-textarea>

            <v-btn
              tile
              style="float:right"
            >
              SEND
            <v-icon right>
                mdi-send
              </v-icon>
            </v-btn>
        </v-sheet>
      <!-- <UiSessionPanel></UiSessionPanel> -->
      </v-col>  
    </v-row>

</vmain>

</template>

<script> 
  export default {
      components:{
      },
      data: () => ({
        currentFriend:'',
        currentAvatarSrc:'',
        recent: [
          {
            active: true,
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png',
            title: 'Plankton',
          },
          {
            active: true,
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/0/05/Squidward_stock_art.png',
            title: 'Squidward',
          },
          {
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png',
            title: 'SpongeBob',
          },
          {
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/5/5d/Patrick_stock_art.png',
            title: 'Patrick',
          },
        ],
      }),
      methods:{
        changeCurrentFriend(chat){
          this.currentFriend = chat.title
          this.currentAvatarSrc = chat.avatar
        }
      }
  }
</script>