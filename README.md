This browser extension lets you right-click a link and open it in your default browser.

Why would you want to do this? Because life is difficult? I dunno. For me, Google Inbox is super buggy in Firefox (I can't send mail sometimes) but I want to use Firefox as my default browser. I actually really love Inbox when it works, especially the bundling feature.

I have resorted to running Inbox in Google Chrome but *I want it to open links in Firefox*.

Here's an example for how to install it for Chrome on Mac OS X. You will have to adjust some paths. If you want to install it for Windows, [read this maybe](https://developer.chrome.com/apps/nativeMessaging#examples).

First, clone the source somewhere. Take note of the directory.

```
git clone https://github.com/kumar303/default-opener.git ~/dev/default-opener
```

Install the [native messaging](https://developer.chrome.com/apps/nativeMessaging) host application by linking `default_opener.json` in the source code to your `NativeMessagingHosts` directory.
```
mkdir -p ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts
ln -s ~/dev/default-opener/app/default_opener.json ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/default_opener.json
```

Quit Chrome if it's running. Start it like this:

```
open -a Google\ Chrome --args --enable-logging --v=1
```

Tail the logs:

```
tail -f ~/Library/Application\ Support/Google/Chrome/chrome_debug.log
```

Those steps aren't totally necessary -- it's just in case you need logging.

In `chrome://extensions/`, turn on developer mode, and load the unpacked extension from the `extension` directory. Find the `key` for your extension on the same developer page, underneath your extension name. Open `app/default_opener.json` in an editor and change `allowed_origins` so that it points to this extension key. It will look something like this:

```
chrome-extension://dehppekledagpdijhjbphlnpfednmoce/
```

Reload the extension. Right click a link to see the 'Open link in default browser' menu item.

Beware that the native application part is a **Python 2 script**. You can see it in `app/default_opener.py`.

If you can think of an easier way to do all of this, let me know!
