<template>
  <div>
    <v-row justify="space-around" style="padding: 0px; margin: 0px">
      <v-card width="600">
        <v-img
          height="180px"
          src="https://wallpaperaccess.com/full/3896911.jpg"
        >
          <v-flex class="text-xs-right">
            <v-btn fab small style="float: right; margin: 20px">
              <v-icon> mdi-plus </v-icon>
            </v-btn>
          </v-flex>

          <v-card-title class="white--text mt-8">
            <v-avatar color="blue" size="110">
              <span class="white--text text-h5">YW</span>
            </v-avatar>
          </v-card-title>
        </v-img>

        <!-- <v-card-text>
        <div class="font-weight-bold ml-8 mb-2">Today</div>

        <v-timeline align-top dense>
          <v-timeline-item
            v-for="message in messages"
            :key="message.time"
            :color="message.color"
            small
          >
            <div>
              <div class="font-weight-normal">
                <strong>{{ message.from }}</strong> @{{ message.time }}
              </div>
              <div>{{ message.message }}</div>
            </div>
          </v-timeline-item>
        </v-timeline>
      </v-card-text> -->
        <div style="height: 500px" class="overflow-y-auto overflow-x-hidden">
          <v-row>
            <v-col v-for="(item, i) in items" :key="i" cols="12">
              <v-card>
                <div class="">
                  <div>
                    <v-row>
                      <v-col cols="2">
                        <v-img
                          :alt="`${item.title} avatar`"
                          :src="item.avatar"
                          :max-width="30"
                          style="margin: 20px"
                        ></v-img>
                      </v-col>
                      <v-col style="float: left" cols="auto">
                        <div
                          style="
                            text-align: left;
                            color: #3d97f5;
                            padding-top: 15px;
                          "
                        >
                          {{ item.title }}
                        </div>
                        <div style="text-align: left">{{ item.artist }}</div>
                        <v-avatar
                          size="150"
                          tile
                          style="padding-top: 20px; padding-bottom: 20px"
                        >
                          <v-img :src="item.src"></v-img>
                        </v-avatar>
                        <v-row style="padding-top: 15px; padding-left: 5px">
                          <v-btn icon color="pink">
                            <v-icon>mdi-heart</v-icon>
                          </v-btn>
                          <v-btn icon color="green">
                            <v-icon>mdi-comment-outline</v-icon>
                          </v-btn>
                        </v-row>
                      </v-col>
                    </v-row>
                    <!-- <v-card-actions>
                  <v-btn
                    v-if="item.artist === 'Ellie Goulding'"
                    class="ml-2 mt-3"
                    fab
                    icon
                    height="40px"
                    right
                    width="40px"
                  >
                    <v-icon>mdi-play</v-icon>
                  </v-btn>

                  <v-btn v-else class="ml-2 mt-5" outlined rounded small>
                    START RADIO
                  </v-btn>
                </v-card-actions> -->
                  </div>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-card>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    messages: [
      {
        from: "You",
        message: `Sure, I'll see you later.`,
        time: "10:42am",
        color: "deep-purple lighten-1",
      },
      {
        from: "John Doe",
        message: "Yeah, sure. Does 1:00pm work?",
        time: "10:37am",
        color: "green",
      },
      {
        from: "You",
        message: "Did you still want to grab lunch today?",
        time: "9:47am",
        color: "deep-purple lighten-1",
      },
    ],
    items: [
      {
        src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        title: "Plankton",
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png",
        artist: "Foster the People",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
        title: "SpongeBob",
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png",
        artist: "Ellie Goulding",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        title: "Plankton",
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png",
        artist: "Foster the People",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
        title: "SpongeBob",
        avatar:
          "https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png",
        artist: "Ellie Goulding",
      },
    ],
  }),
};
</script>
