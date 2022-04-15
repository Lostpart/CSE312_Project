<template>
<div>

</div>

</template>

<script>
  export default {
    data: () => ({ 
        drawer: null,
        links: [
            ['mdi-message-text', 'Messages', '/messages'],
            ['mdi-account-multiple', 'Square', '/about'],
        ]
    }),
    methods:{
        abcde(arg){
            alert(arg)
        }
    }
  }
</script>