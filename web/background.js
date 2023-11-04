chrome.tabs.onActiveChanged.addListener(function(tab) {
    // Assuming by 'value' you mean the URL of the tab
    // The URL might not be available immediately if the tab is not yet fully loaded
    console.log(`New tab created with ID: ${tab.id}`);
    const d = new Date();
    let time = d.getTime();
    console.log("The tab was created at time: " + time);
    // You can also use chrome.tabs.get to ensure that the tab's properties are updated
    chrome.tabs.get(tab.id, function(newTab) {
      console.log(`New tab URL: ${newTab.url}`);
    });
  });