function loadCurrentTabUrl () {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    return encodeURI(tabs[0].url)
  })
}

export { loadCurrentTabUrl }
