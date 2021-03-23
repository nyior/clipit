chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
  chrome.storage.sync.set({ tabUrl: tabs[0].url })
})
