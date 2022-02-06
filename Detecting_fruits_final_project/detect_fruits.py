import cv2
import json
import click
import numpy as np
from tqdm import tqdm
from pathlib import Path

from typing import Dict


def detect_fruits(img_path: str) -> Dict[str, int]:
    """Fruit detection function, to implement.
    Parameters
    ----------
    img_path : str
        Path to processed image.
    Returns
    -------
    Dict[str, int]
        Dictionary with quantity of each fruit.
    """
    jpg = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # TODO: Implement detection method.
    orange = 0
    apple = 0
    banana = 0
    resize_jpg = cv2.resize(jpg, dsize=None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    jpg = cv2.GaussianBlur(resize_jpg, (19, 19), 0)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)
    kernel = np.ones((7, 7), np.uint8)

    # Banana
    lower_banana = np.array([20, 100, 160])
    upper_banana = np.array([30, 255, 255])
    mask_banana = cv2.inRange(hsv_jpg, lower_banana, upper_banana)
    lower_banana1 = np.array([19, 78, 87])
    upper_banana1 = np.array([45, 255, 255])
    mask_banana1 = cv2.inRange(hsv_jpg, lower_banana1, upper_banana1)
    mask_banana_full = mask_banana + mask_banana1
    closing_banana = cv2.morphologyEx(mask_banana_full, cv2.MORPH_CLOSE, kernel)
    banana_contours = cv2.findContours(closing_banana, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contours = banana_contours[0]
    for c in banana_contours:
        x, y, w, h = cv2.boundingRect(c)
        contour = cv2.contourArea(c)
        if contour > 10000:
            cv2.rectangle(resize_jpg, (x, y), (x + w, y + h), (0, 0, 255), 2)  ##BGR
            banana += 1

    # Orange
    lower_orange = np.array([0, 206, 0])  # 10 200 200
    upper_orange = np.array([19, 255, 255])  # 25 255 255
    lower_orange1 = np.array([9, 102, 227])  # 10 200 200
    upper_orange1 = np.array([52, 252, 255])  # 25 255 255
    mask_orange = cv2.inRange(hsv_jpg, lower_orange, upper_orange)
    mask_orange1 = cv2.inRange(hsv_jpg, lower_orange1, upper_orange1)
    mask_orange_full = mask_orange + mask_orange1
    closing_orange = cv2.morphologyEx(mask_orange_full, cv2.MORPH_CLOSE, kernel)

    orange_contours = cv2.findContours(closing_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours = orange_contours[0]
    for o in orange_contours:
        x, y, w, h = cv2.boundingRect(o)
        contour = cv2.contourArea(o)
        if contour > 10000:
            cv2.rectangle(resize_jpg, (x, y), (x + w, y + h), (255, 0, 0), 2)  ##BGR
            orange += 1

    lower2 = np.array([0, 36, 0])  # 0 128 24    0 125 0
    upper2 = np.array([14, 220, 255])  # 10 255 255 31 255 148
    apple_mask1 = cv2.inRange(hsv_jpg, lower2, upper2)

    lower1 = np.array([52, 45, 0])  # 0 128 24    0 125 0
    upper1 = np.array([189, 255, 255])  # 10 255 255 31 255 148
    apple_mask2 = cv2.inRange(hsv_jpg, lower1, upper1)

    apple_mask_full = apple_mask1+apple_mask2

    closing_apple = cv2.morphologyEx(apple_mask_full, cv2.MORPH_CLOSE, kernel)
    apple_contours = cv2.findContours(closing_apple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    for a in apple_contours:
        x, y, w, h = cv2.boundingRect(a)
        contour = cv2.contourArea(a)
        if contour > 10000:  # contours area function need to check
            cv2.rectangle(resize_jpg, (x, y), (x + w, y + h), (0, 255, 0), 2)  ##BGR
            apple += 1

    return {'apple': apple, 'banana': banana, 'orange': orange}

@click.command()
@click.option('-p', '--data_path', help='Path to data directory', type=click.Path(exists=True, file_okay=False,
                                                                                  path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path),
              required=True)
def main(data_path: Path, output_file_path: Path):
    print(data_path)
    img_list = data_path.glob('*.jpg')
    results = {}

    for img_path in tqdm(sorted(img_list)):
        fruits = detect_fruits(str(img_path))
        results[img_path.name] = fruits

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)

if __name__ == '__main__':
    main()