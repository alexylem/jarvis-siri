## Description
Control Jarvis using Siri on iOS devices:
* iPhone
* iPad
* Apple Watch
* Mac

**Principle**
Ask Siri to add a Note (synced to your gmail account) containing an order.
This plugins monitors these Notes and make Jarvis execute the order.

## Prerequisites

**Gmail account setup**
1. Have a Gmail account
2. IMAP enabled (Gmail > Settings > Transfert IMAP > Activate IMAP)

**iOS device setup**
1. Go to Settings > Notes > Accounts and add Gmail
2. Make sure sync of Notes is enabled for this Account
3. Select Gmail as default Account for new Notes in Settings > Notes > Default Account
4. Reboot your iOS device to take into account new default Notes account

## Usage
1. Make sure Jarvis is running
2. Invoke Siri (long press home button or "Hey Siri")
3. Say "Note" and your order, ex: "Note allume le bar"
```yml
Jarvis: J'allume le bar
```

## Author
[Alex](https://github.com/alexylem)
