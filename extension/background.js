var port = chrome.runtime.connectNative("default_opener");

/**
 * Call the native appliction with this url to open it with the default browser
 */
function callUrl(url) {
    console.log(`Sending: link ${url}`);
    port.postMessage({link: url});
}

port.onMessage.addListener((response) => {
    console.log("Received: " + response);
});

port.onDisconnect.addListener(() => {
    console.log("Port was disconnected. Error:", chrome.runtime.lastError);
});

/** Create a new context menu to open links with an external browser */
chrome.contextMenus.create({
  title: 'Open in default browser',
  contexts: ['link'],
  onclick: (info) => {
      callUrl(info.linkUrl);
  }
});

/** Open the current tab in the default browser if the extension button in the toolbar is pressed */
chrome.browserAction.onClicked.addListener(function(tab) {
    callUrl(tab.url);
})

/** 
 * This is going to be called by listen.js if a new tab is opened.
 * Its URL will be opened in an external browser and the tab will be closed.
 */
chrome.runtime.onMessage.addListener(
 function(request, sender, sendResponse) {
    console.log(JSON.stringify(request));
    if (request.hasOwnProperty("request")) {
        //if (request["request"] == "LAUNCH" && isWhitelisted(sender.tab.url)) {
        if (request["request"] == "LAUNCH" && !sender.tab.pinned) {
            callUrl(sender.tab.url);
            chrome.tabs.remove(sender.tab.id);
        }
    } else {
        sendResponse({response: "nothing"});
    }

});
