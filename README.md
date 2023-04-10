# Firebase reCAPTCHA intent handler/parser

REQUIREMENTS: pyclip and Tkinter

### Manual usage

Run `main.py '<intent:// url>'` and copy the parsed recaptchaToken.

### Linux setup

Run `sudo make install` or `PREFIX=~/.local make install` if .local/bin is in global $PATH

And `xdg-mime default Intent.desktop x-scheme-handler/intent`

### Windows setup (UNTESTED, I'd advise you to add the URI handler directly)

Change the python interpreter path and the python file path before applying the registry file
