var port = chrome.runtime.connectNative("default_opener");

port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});

chrome.contextMenus.create({
  title: 'Open in default browser',
  contexts: ['link'],
  onclick: (info) => {
    console.log(`Sending: link ${info.linkUrl} `);
    port.postMessage({link: info.linkUrl});
  }
});
