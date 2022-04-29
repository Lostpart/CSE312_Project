<template>
  <div>
    <v-row justify="space-around" style="padding: 0px; margin: 0px">
      <v-card width="600">
        <v-img height="180px" src="https://wallpaperaccess.com/full/3896911.jpg">
          <v-flex class="text-xs-right">
            <v-col cols="auto">
              <v-dialog transition="dialog-top-transition" max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    fab
                    small
                    style="float: right; margin: 20px"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon> mdi-plus </v-icon>
                  </v-btn>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-toolbar color="primary" dark>Share a new moment</v-toolbar>
                    <v-file-input
                      style="margin-left: 10px"
                      accept="image/*"
                      label="Picture"
                      v-model="newMomentImg"
                      filled
                      prepend-icon="mdi-camera"
                    ></v-file-input>
                    <v-textarea
                      style="margin-left: 10px"
                      prepend-icon="mdi-comment"
                      name="input-7-1"
                      label="Comment"
                      v-model="newMomentComment"
                    ></v-textarea>
                    <v-card-actions class="justify-end">
                      <v-btn color="blue" rounded dark text @click="handleSubmit"
                        >Submit</v-btn
                      >
                    </v-card-actions>
                    <v-card-actions class="justify-end">
                      <v-btn text rounded @click="dialog.value = false">Close</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-col>
          </v-flex>

          <v-card-title class="white--text mt-8">
            <v-avatar color="blue" size="80">
              <span class="white--text text-h5">{{ avatarName }}</span>
            </v-avatar>
          </v-card-title>
        </v-img>
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
                        <div style="text-align: left; color: #3d97f5; padding-top: 15px">
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
                        </v-row>
                      </v-col>
                    </v-row>
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
  methods: {
    handleSubmit() {},
  },
  computed: {
    avatarName() {
      const displayName = this.$store.state.user.displayName
      if (displayName) return displayName.substring(0, 1).toUpperCase()
      return ''
    },
  },
  data: () => ({
    newMomentImg: null,
    newMomentComment: '',
    messages: [
      {
        from: 'You',
        message: `Sure, I'll see you later.`,
        time: '10:42am',
        color: 'deep-purple lighten-1',
      },
      {
        from: 'John Doe',
        message: 'Yeah, sure. Does 1:00pm work?',
        time: '10:37am',
        color: 'green',
      },
      {
        from: 'You',
        message: 'Did you still want to grab lunch today?',
        time: '9:47am',
        color: 'deep-purple lighten-1',
      },
    ],
    items: [
      {
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        title: 'Plankton',
        avatar:
          'https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png',
        artist: 'Foster the People',
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        title: 'SpongeBob',
        avatar:
          'https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png',
        artist: 'Ellie Goulding',
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        title: 'Plankton',
        avatar:
          'https://static.wikia.nocookie.net/spongebob/images/7/77/Plankton_stock_art.png',
        artist: 'Foster the People',
      },
      {
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        title: 'SpongeBob',
        avatar:
          'https://static.wikia.nocookie.net/spongebob/images/d/d7/SpongeBob_stock_art.png',
        artist: 'Ellie Goulding',
      },
    ],
  }),
}
</script>
