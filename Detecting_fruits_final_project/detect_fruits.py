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
    resize_jpg = cv2.resize(jpg, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    jpg = cv2.GaussianBlur(resize_jpg, (19, 19), 0)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)

    # Banana
    lower_banana = np.array([20, 100, 160])
    upper_banana = np.array([30, 255, 255])
    mask_banana = cv2.inRange(hsv_jpg, lower_banana, upper_banana)
    banana_contours = cv2.findContours(mask_banana, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contours = banana_contours[0]
    for c in banana_contours:
        contour = cv2.contourArea(c)
        if contour > 2500:
            banana += 1

    # Orange
    lower_orange = np.array([0, 217, 0])  # 10 200 200
    upper_orange = np.array([19, 255, 255])  # 25 255 255
    mask_orange = cv2.inRange(hsv_jpg, lower_orange, upper_orange)
    orange_contours = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contours = orange_contours[0]
    for o in orange_contours:
        contour = cv2.contourArea(o)
        if contour > 2000:
            orange += 1

    lower2 = np.array([0, 36, 0])  # 0 128 24    0 125 0
    upper2 = np.array([13, 220, 255])  # 10 255 255 31 255 148

    upper_mask = cv2.inRange(hsv_jpg, lower2, upper2)

    apple_mask = upper_mask
    apple_contours = cv2.findContours(apple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    for a in apple_contours:
        contour = cv2.contourArea(a)
        if contour > 2000:  # contours area function need to check
            apple += 1
    return {'apple': apple, 'banana': banana, 'orange': orange}

@click.command()
@click.option('-p', '--data_path', help='Path to data directory', type=click.Path(exists=True, file_okay=False,
                                                                                  path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path),
              required=True)
def main(data_path: Path, output_file_path: Path):
    img_list = data_path.glob('*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        fruits = detect_fruits(str(img_path))
        results[img_path.name] = fruits

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)



if __name__ == '__main__':
    main()