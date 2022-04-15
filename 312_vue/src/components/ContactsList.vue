<template>
  <div>
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
      <v-col v-show="isClicked">
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
          min-height="300"
          width="100%"
        >
          <div v-for="chat in currentHistory"
              :key="chat.chatID">
            <v-row>
              <v-col>
                <v-card
                  disabled
                  elevation="4"
                  link
                  min-width="50px"
                  class="pa-2 ma-4"
                  style="display: inline-block"
                  :class="{ 'light-blue': !chat.flag, 'white--text': !chat.flag}"
                  :style="{ float: chat.flag ? 'left' : 'right'}"
                >
                  {{chat.msg}}
                </v-card>
              </v-col>
            </v-row>
          </div>
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
            v-model="currentSentence"
          >
          </v-textarea>
          <v-btn
            style="float:right"
            @click="sendMsg"
          >
            SEND
          <v-icon right>
              mdi-send
            </v-icon> 
          </v-btn>
        </v-sheet>
      </v-col>  
    </v-row>
  </div>
</template>

<script> 
  export default {
      components:{
      },
      data: () => ({
        currentFriend:'',
        currentAvatarSrc:'',
        currentHistory:[],
        currentSentence:'',
        isClicked:false,
        recent: [
          {
            active: true,
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png',
            title: 'Plankton',
            history:[
              {
                chatID: 1,
                flag:true,
                timestamp: '2022-04-15 01:44:36',
                msg:'test'
              },
              {
                chatID: 2,
                flag:false,
                timestamp: '2022-04-15 01:44:36',
                msg:'test'
              }
            ]
          },
          {
            active: true,
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/0/05/Squidward_stock_art.png',
            title: 'Squidward',
            history:[
              {
                chatID: 3,
                timestamp: '2022-04-15 03:44:36',
                msg:'test2'              
              },
              {
                chatID: 4,
                timestamp: '2022-04-15 03:44:36',
                msg:'test2'              
              }
            ]
          },
          {
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png',
            title: 'SpongeBob',
            history:[
              {
                chatID: 5,
                msg:'test3'
              }
            ]
          },
          {
            avatar: 'https://static.wikia.nocookie.net/spongebob/images/5/5d/Patrick_stock_art.png',
            title: 'Patrick',
            history:[
              {
                msg:'test4'
              }
            ]
          },
        ],
      }),
      methods:{
        changeCurrentFriend(chat){
          this.currentFriend = chat.title
          this.currentAvatarSrc = chat.avatar
          this.currentHistory = chat.history
          this.isClicked = true
          this.currentSentence = ''
        },
        findFriendIdx(name){
          const len = this.recent.length
          for(let i = 0; i < len; i++){
            if(this.recent[i]['title'] === name){
              return i
            }
          }
          return -1
        },
        sendMsg(){
          const friend_idx = this.findFriendIdx(this.currentFriend)
          this.recent[friend_idx]['history'].push({
            chatID: Math.random() * 10000,
            timestamp: '2022-04-15 03:44:36',
            msg:this.currentSentence
          })
          this.recent[friend_idx]['history'].push({
            flag: true,
            chatID: Math.random() * 10000,
            timestamp: '2022-04-15 03:44:36',
            msg:this.currentSentence
          })
          this.currentSentence = ''
        }
      },
      computed:{
      }
  }
</script>