<template>
  <div>
    <v-row justify="space-around" style="padding: 0px; margin: 0px">
      <v-card width="600">
        <v-img height="180px" src="https://wallpaperaccess.com/full/3896911.jpg">
          <v-flex class="text-xs-right">
            <v-col cols="auto">
              <v-dialog transition="dialog-top-transition" max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn fab small style="float: right; margin: 20px" v-bind="attrs" v-on="on">
                    <v-icon> mdi-plus </v-icon>
                  </v-btn>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-toolbar color="primary" dark>Share a new moment</v-toolbar>
                    <v-file-input
                      style="margin-left: 10px"
                      accept="image/png, image/jpeg"
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
                      <v-btn color="blue" rounded dark text @click="handleSubmit">Submit</v-btn>
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
            <v-col v-for="(item, i) in momentsList" :key="i" cols="12">
              <v-card>
                <div class="">
                  <div>
                    <v-row>
                      <v-col cols="2">
                        <v-avatar color="blue" size="60" style="margin-top: 10px; margin-left: 10px">
                          <span class="white--text text-h5">{{ getAvatarNameById(item.title) }}</span>
                        </v-avatar>
                      </v-col>
                      <v-col style="float: left" cols="auto">
                        <div style="text-align: left; color: #3d97f5; padding-top: 15px">
                          {{ getUsernameById(item.title) }}
                        </div>
                        <div style="text-align: left">{{ item.content }}</div>
                        <v-avatar size="150" tile style="padding-top: 20px; padding-bottom: 20px">
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
  import axios from 'axios'

  export default {
    methods: {
      getUsernameById(userID) {
        const usersList = this.$store.state.user.usersList
        for (let i = 0; i < usersList.length; i++) {
          if (usersList[i]['user_id'] === userID) return usersList[i]['displayName']
        }
        return ''
      },
      getAvatarNameById(userID) {
        return this.getUsernameById(userID).substring(0, 1).toUpperCase()
      },
      handleSubmit() {
        if (!this.newMomentImg) {
          alert('An image is required')
          return
        }
        if (this.newMomentComment.length === 0) {
          alert('A comment is required')
          return
        }
        this.fileToBase64(this.newMomentImg).then((fileInBase64WithPrefix) => {
          const imgFileName = this.newMomentImg.name
          const base64PrefixIdx = fileInBase64WithPrefix.search('base64,')
          const fileInBase64 = fileInBase64WithPrefix.substring(base64PrefixIdx + 'base64,'.length)
          const newMomentJson = {
            user_id: this.$store.state.user.userID,
            image: [{ filename: imgFileName, file: fileInBase64 }],
            content: this.newMomentComment,
          }
          const _this = this
          axios
            .post('http://127.0.0.1:8080/moment/create', newMomentJson)
            .then((response) => {
              const responseObj = response.data
              if (responseObj.status === 'error') {
                alert(responseObj.message)
                return
              }
              _this.newMomentImg = null
              _this.newMomentComment = ''
              axios
                .post('http://127.0.0.1:8080/moment/getRecentMoments', { limit: 100 })
                .then(function (response) {
                  _this.$store.commit('setMomentsList', response.data)
                })
                .catch(function (error) {
                  console.log(error)
                })
            })
            .catch((error) => alert(error))
        })
      },
      fileToBase64(file) {
        return new Promise((resolve) => {
          const reader = new FileReader()
          reader.onload = function (e) {
            resolve(e.target.result)
          }
          reader.readAsDataURL(file)
        })
      },
    },
    computed: {
      avatarName() {
        const displayName = this.$store.state.user.displayName
        if (displayName) return displayName.substring(0, 1).toUpperCase()
        return ''
      },
      momentsList() {
        const orginalMomentsList = this.$store.state.user.momentsList
        const res = []
        for (let i = 0; i < orginalMomentsList.length; i++) {
          const originalMoment = orginalMomentsList[i]
          const newMoment = {}
          newMoment['src'] =
            originalMoment['image'].length === 0
              ? ''
              : 'http://localhost:8080/upload-image/' + originalMoment['image'][0]
          newMoment['title'] = originalMoment['from']
          newMoment['content'] = originalMoment['content']
          res.push(newMoment)
        }
        return res
      },
    },
    data: () => ({
      newMomentImg: null,
      newMomentComment: '',
    }),
  }
</script>
