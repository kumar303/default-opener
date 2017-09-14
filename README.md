This extension lets you right-click and open a link in your default browser.

Installation:

```
mkdir -p ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts
ln -s ~/dev/default-opener/app/default_opener.json ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/default_opener.json
```

Start Chrome:

```
open -a Google\ Chrome --args --enable-logging --v=1
```

Tail the logs:

```
tail -f ~/Library/Application\ Support/Google/Chrome/chrome_debug.log
```

In Chrome, load the unpacked extension from the `extension` directory. Find the `key` for your extension on the same developer page. Open `app/default_opener.json` in an editor and change `allowed_origins` so that it points to this extension key. It will look something like this:

```
chrome-extension://dehppekledagpdijhjbphlnpfednmoce/
```

Reload the extension.
