# bee-focused

## Description

## Requirements

- Python 3 (On a Mac? `homebrew install python`)
- [Beeminder](https://www.beeminder.com/home)
- [Focus](https://heyfocus.com/)

## Setup

Log into Beeminder, and then download auth_token.json at this url and place it
in the `bee-focused` root folder:

[https://www.beeminder.com/api/v1/auth_token.json](https://www.beeminder.com/api/v1/auth_token.json)

Copy `goals_example.json` to `goals.json` and edit to reflect which of your
Beeminder goals you want to use to trigger focus time.

```bash
chmod +x bee-focused.py
./bee-focused.py
```

Add an entry to your crontab to run the script every few minutes.

- Open Crontab: `export VISUAL=nano; crontab -e`
- Add this line: `*/5 * * * * /path/to/bee-focused.py`
- Save and exit

If you're using a browser other than Safari, Chrome, and Vivaldi, you'll also
need to install the Focus extension. [Here's their documentation on how to do
that.](https://heyfocus.com/docs/help/browser-extensions/)

## Information

- [Beeminder API docs](http://api.beeminder.com)
- "`lane` (number): Where you are with respect to the yellow brick road (2 or more = above the road, 1 = top lane, -1 = bottom lane, -2 or less = below the road)."
- [Focus scripting docs](https://heyfocus.com/docs/features/scripting/)
