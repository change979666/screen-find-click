import pyautogui
import time
import keyboard

def find_and_click(image_path, timeout=30):
    """在屏幕上查找图片并点击"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location is not None:
            pyautogui.moveTo(location.x, location.y, duration=0.5)
            pyautogui.click()
            return True
        time.sleep(1)
    print(f"未找到目标图片 {image_path}")
    return False

def automate_browser_task():
    """示例任务：自动化浏览器搜索"""
    # 打开浏览器（假设浏览器图标在桌面左上角）
    if not find_and_click("browser_icon.png"):
        return

    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')  # 新建标签页
    time.sleep(1)

    # 输入网址
    pyautogui.write("https://www.example.com", interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)

    # 查找搜索框并输入内容
    if find_and_click("search_box.png"):
        pyautogui.write("自动化测试", interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)

def main():
    print("开始自动化任务（按Esc键取消）")
    pyautogui.FAILSAFE = True  # 移动到屏幕左上角可终止程序

    try:
        automate_browser_task()
    except KeyboardInterrupt:
        print("\n任务被用户取消")
    finally:
        print("任务结束")

if __name__ == "__main__":
    # 请先准备好目标图片（如browser_icon.png、search_box.png）
    # 使用命令安装依赖：pip install pyautogui keyboard opencv-python
    main()
