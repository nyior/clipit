function loadCurrentTabUrl () {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    return tabs[0].url
  })
}

export { loadCurrentTabUrl }
