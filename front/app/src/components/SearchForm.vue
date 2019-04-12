<template>
    <v-container>
        <v-layout
                row
                justify-center
        >
            <v-flex xs4>
                <v-text-field
                        :autofocus="true"
                        :clearable="true"
                        placeholder="google.com"
                        v-model.trim="domain"
                >
                    <template v-slot:label>
                        <h2>Domain for search subdomains</h2>
                    </template>
                </v-text-field>
            </v-flex>
            <v-flex xs1 offset-xs1>
                <v-text-field
                        type="number"
                        v-model.number="deep"
                        max="3"
                        min="1"
                ></v-text-field>
            </v-flex>
        </v-layout>
        <v-layout justify-center pb-3>
            <v-btn
                    @click="StartStopSearch"
                    :loading="loading"
            >{{ btnText }}
            </v-btn>
        </v-layout>
        <SearchResult
                :actions="actions"
                @stopChecking="stopChecking"
                :domain="domain"
        ></SearchResult>
    </v-container>
</template>

<script>
    import SearchResult from './SearchResult'

    export default {
        components: {
            SearchResult
        },
        data() {
            return {
                domain: '',
                deep: 1,
                btnTextStart: 'Start checking',
                btnTextStop: 'Stop checking',
                btnText: '',
                actions: {
                    start: 'start',
                    stop: 'stop_checking',
                    addHost: 'add_host',
                    updateProgress: 'update_progress'
                },
                loading: false,
            }
        },
        mounted() {
            this.btnText = this.btnTextStart
        },
        methods: {
            StartStopSearch() {
                this.$socket.sendObj({action: this.actions.start, domain: this.domain, deep: this.deep})
                this.btnText = this.btnTextStop
                this.loading = true
            },
            stopChecking() {
                this.btnText = this.btnTextStart
                this.loading = false
            }
        }
    }
</script>

<style>

</style>
