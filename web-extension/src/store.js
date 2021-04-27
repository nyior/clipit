import { reactive } from 'vue'

export const store = {
  state: reactive({
    tabUrl: null
  }),

  updateTabUrl (newUrl) {
    this.state.tabUrl = newUrl
  }
}
