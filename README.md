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

## License & Attribution / 许可与来源

Original project code authored for this repository is released under the MIT License; see [LICENSE](./LICENSE).

When reusing or redistributing a substantial portion, retain the LICENSE and its copyright notice. The copyright notice includes this original source URL: https://github.com/change979666/screen-find-click. Please keep the source link visible in your redistributed source or project documentation.

This license applies only to original material that the repository maintainer has the right to license. Third-party libraries, vendor code, platform SDKs, trademarks, screenshots, icons, fonts, and other external assets remain subject to their respective licenses and terms. Review those terms before reuse.

**Project status:** personal/archived project, shared as-is. Maintenance, compatibility, and production readiness are not guaranteed.
