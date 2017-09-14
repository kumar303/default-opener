/*
On startup, connect to the "default_opener" app.
*/
var port = chrome.runtime.connectNative("default_opener");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});

/*
On a click on the browser action, send the app a message.
*/
chrome.browserAction.onClicked.addListener(() => {
  const link = 'http://farmdev.com';
  console.log(`Sending: link ${link} `);
  port.postMessage({link: link});
});
