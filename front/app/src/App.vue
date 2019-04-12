<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Acribia </span>
        <span class="font-weight-light">TEST ASSIGNMENT</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/DDmitiy/acribia_test.git"
        target="_blank"
      >
        <span class="mr-2">GitHub</span>
        <v-icon>open_in_new</v-icon>
      </v-btn>
    </v-toolbar>

    <v-content>
      <SearchForm/>
    </v-content>
  </v-app>
</template>

<script>
import SearchForm from './components/SearchForm'

export default {
  name: 'App',
  components: {
    SearchForm
  },
  data () {
    return {
      //
    }
  }
}
</script>
