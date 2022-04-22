<template>
  <div class="Square">
    <v-row justify="space-around" style="padding: 0px; margin: 0px">
      <v-col>
        <v-card width="40%">
          <v-list>
            <v-list-item
              v-show="chat.active"
              v-for="chat in recent"
              :key="chat.title"
              link
            >
              <v-list-item-avatar>
                <v-img :alt="`${chat.title} avatar`" :src="chat.avatar"></v-img>
              </v-list-item-avatar>

              <v-list-item-content @click="changeCurrentFriend(chat)">
                <v-list-item-title v-text="chat.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  components: {},
  data: () => ({
    currentFriend: "",
    currentAvatarSrc: "",
    currentHistory: [],
    currentSentence: "",
    isClicked: false,
    recent: [
      {
        active: true,
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png",
        title: "Plankton",
        history: [
          {
            chatID: 1,
            flag: true,
            timestamp: "2022-04-15 01:44:36",
            msg: "test",
          },
          {
            chatID: 2,
            flag: false,
            timestamp: "2022-04-15 01:44:36",
            msg: "test",
          },
        ],
      },
      {
        active: true,
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/0/05/Squidward_stock_art.png",
        title: "Squidward",
        history: [
          {
            chatID: 3,
            timestamp: "2022-04-15 03:44:36",
            msg: "test2",
          },
          {
            chatID: 4,
            timestamp: "2022-04-15 03:44:36",
            msg: "test2",
          },
        ],
      },
      {
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png",
        title: "SpongeBob",
        history: [
          {
            chatID: 5,
            msg: "test3",
          },
        ],
      },
      {
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/5/5d/Patrick_stock_art.png",
        title: "Patrick",
        history: [
          {
            msg: "test4",
          },
        ],
      },
    ],
  }),
};
</script>
