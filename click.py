import pyautogui
import time


def click_and_print(x, y):
    """
    Clicks on the specified coordinates and prints the coordinates.
    """
    time.sleep(0.2)
    pyautogui.click(x, y)
    print(f"Clicked at: ({x}, {y})")


def main():
    # Wait and go to the desired window
    print("Wait and go to the desired window")
    time.sleep(3)

    # Click on top left
    print("Click on top left")
    x_min, y_min = pyautogui.position()
    click_and_print(x_min, y_min)

    # Wait for user to click bottom right
    print("Click on bottom right")
    time.sleep(5)
    pyautogui.click()

    # Get coordinates of bottom right
    x_max, y_max = pyautogui.position()
    click_and_print(x_max, y_max)

    # Calculate width and height
    width = x_max - x_min
    height = y_max - y_min

    # Click on every pixel within the rectangle
    for x in range(int(x_min), int(x_min + width), 5):
        for y in range(int(y_min), int(y_min + height), 5):
            click_and_print(x, y)

    # Print message after clicking on all pixels
    print("Clicked on all pixels within the rectangle.")


if __name__ == "__main__":
    main()
