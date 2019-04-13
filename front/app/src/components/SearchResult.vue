<template>
    <v-layout justify-center row wrap>
        <v-flex xs12 pb-3>
            <h2 class="text-xs-center">Results ({{progressPercent}} %)</h2>
        </v-flex>
        <v-data-table
            :items="hosts"
            :headers="[{text: 'Хост', sortable: false}]"
          >
            <template slot="items" slot-scope="props">
                <td><a href="props.item">{{ props.item }}</a></td>
            </template>
            <v-alert slot="no-results" :value="true" color="error" icon="warning">
              Your search for "{{ domain }}" found no results.
            </v-alert>
          </v-data-table>
        <table id="subdoms">

        </table>
    </v-layout>
</template>

<script>
    export default {
        name: 'SearchResult',
        data() {
            return {
                subdomsDiv: {},
                progressPercent: 0,
                hosts: [],
            }
        },
        props: ['actions', 'domain'],
        mounted() {
            this.subdomsDiv = document.getElementById('subdoms')
            this.$socket.onmessage = (data) => {
                this.message_handler(JSON.parse(data.data))
            }
        },
        methods: {
            message_handler(message) {
                if (message.action === this.actions.addHost) {
                    this.addHost(message.domain)
                }
                if (message.action === this.actions.stop) {
                    this.$emit('stopChecking')
                }
                if (message.action === this.actions.updateProgress) {
                    this.progressPercent = message.percent
                }
                if (message.action === this.actions.start) {
                    this.hosts = []
                    this.progressPercent = 0
                }
            },
            addHost(domain) {
                setTimeout(() => {this.hosts.unshift(domain)}, 0)
            }
        }
    }
</script>

<style scoped>

</style>