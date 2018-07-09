# bee-focused

## Description

## Requirements

- Python 3 (On a Mac? `homebrew install python`)
- [Beeminder](https://www.beeminder.com/home)
- [Focus](https://heyfocus.com/)
- [Focus browser extension](https://heyfocus.com/docs/help/browser-extensions/)
  if you're using a browser other than Safari, Chrome, or Vivaldi

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

- Find the path to your local copy of Python 3: `which python3`
- Open Crontab: `export VISUAL=nano; crontab -e`
- Add this line: `*/5 * * * *  /path/to/python3 /path/to/bee-focused/bee-focused.py >>/path/to/bee-focused/cron.log 2>&1`
- Save and exit

In order to allow you to enable Focus separately from this script, bee-focused
never explicitly unfocuses. Instead, it starts 7-minute focus sessions and then
lets the last one expire when you're caught up on your goals. For that reason,
it's important that the script runs at least every seven minutes (I suggest
every five) in order to insure that there isn't time between when one focus
session expires and the next is initiated.

## Information

- [Beeminder API docs](http://api.beeminder.com)
- "`lane` (number): Where you are with respect to the yellow brick road (2 or more = above the road, 1 = top lane, -1 = bottom lane, -2 or less = below the road)."
- [Focus scripting docs](https://heyfocus.com/docs/features/scripting/)
