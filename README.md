# screen-find-click

A minimal screen-automation helper built on [PyAutoGUI](https://pyautogui.readthedocs.io/)
and the `keyboard` library. It watches the screen for a template image, moves the
mouse to it, and clicks — plus a small demo flow that automates a browser search.

## Features

- `find_and_click(image_path, timeout=30)`: polls `pyautogui.locateCenterOnScreen(...,
  confidence=0.8)` until the template appears, eases the cursor over and clicks.
- `automate_browser_task()`: example flow — find a browser icon, open a new tab,
  type a URL, then find a search box and type a query.
- PyAutoGUI failsafe enabled: slam the mouse to the top-left corner to abort.

## Project layout

- `zidonghua.py` — single script.

## Run

```bash
pip install pyautogui keyboard
```

Before running, place your own template images (e.g. `browser_icon.png`,
`search_box.png`) next to the script, then:

```bash
python zidonghua.py
```

## Notes

- Template matching depends on screen resolution and scaling; take the screenshots
  on the same display you run the script on.
- This is a demo skeleton — replace `automate_browser_task()` steps with your own
  target images and actions.