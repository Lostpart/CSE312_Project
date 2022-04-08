<template>
  <div>
    <ContactsList></ContactsList>
  </div>
</template>

<script>
// @ is an alias to /src
import ContactsList from '@/components/ContactsList'

export default {
  name: 'MessagesView',
  components: {
    ContactsList
    }
}
</script>
