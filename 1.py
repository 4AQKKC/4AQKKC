import cv2
import pytesseract
import pyautogui
import time
import numpy as np
from PIL import ImageGrab
from openai import OpenAI

# --- CONFIG ---
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if different
BLUESTACKS_WINDOW_NAME = 'BlueStacks'
TILE_SIZE = 40  # approx. pixel size of a tile block
COLOR_THRESHOLDS = {
    'red': ([0, 0, 100], [80, 80, 255]),
    'blue': ([100, 0, 0], [255, 80, 80]),
    'yellow': ([0, 100, 100], [80, 255, 255]),
    'purple': ([100, 0, 100], [255, 80, 255])
}

# --- SETUP ---
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
openai = OpenAI(api_key='your-api-key-here')


def get_bluestacks_window():
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    return screen_np


def crop_game_area(img):
    # You should manually adjust this crop area based on your BlueStacks layout
    height, width, _ = img.shape
    return img[100:700, 100:500]  # Example values, crop the game grid area


def detect_tile_color(tile_img):
    avg_color = tile_img.mean(axis=(0, 1))
    for color_name, (lower, upper) in COLOR_THRESHOLDS.items():
        if all(lower[i] <= avg_color[i] <= upper[i] for i in range(3)):
            return 1  # occupied
    return 0  # empty


def recognize_blocks(image):
    board = []
    for y in range(10):
        row = []
        for x in range(10):
            tile = image[y * TILE_SIZE:(y + 1) * TILE_SIZE, x * TILE_SIZE:(x + 1) * TILE_SIZE]
            val = detect_tile_color(tile)
            row.append(val)
        board.append(row)
    return board


def get_next_blocks(image):
    # This is a placeholder
    return ['red_t', 'blue_l', 'yellow_square']


def query_chatgpt_for_best_move(board, next_blocks):
    prompt = f"""
You are an AI playing a block puzzle game. 
The board is a 10x10 grid (0 = empty, 1 = occupied). 
Here is the current board:
{board}

The next available blocks are:
{next_blocks}

Return the best move as a Python dictionary like this:
{{"block": "red_t", "position": [4, 5]}}
"""
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(response.choices[0].message.content)


def draw_overlay(position, block_type):
    x, y = position
    px, py = 100 + x * TILE_SIZE, 100 + y * TILE_SIZE  # Adjust based on actual coordinates
    pyautogui.moveTo(px, py)
    pyautogui.click()  # simulate click for visualization, or draw rectangle if using overlay lib


def main_loop():
    while True:
        screen = get_bluestacks_window()
        game_area = crop_game_area(screen)
        board = recognize_blocks(game_area)
        next_blocks = get_next_blocks(game_area)

        best_move = query_chatgpt_for_best_move(board, next_blocks)
        draw_overlay(best_move['position'], best_move['block'])

        time.sleep(5)  # Update every 5 seconds


if __name__ == '__main__':
    main_loop()
