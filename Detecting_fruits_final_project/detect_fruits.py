import cv2
import json
import click
import numpy as np
from glob import glob
from tqdm import tqdm

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
    banana = 0
    orange = 0
    apple = 0
    jpg = cv2.resize(jpg, dsize=(1000, 800), interpolation=cv2.INTER_AREA)
    hsv_jpg = cv2.cvtColor(jpg, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 160])
    upper_yellow = np.array([30, 255, 255])
    mask_yellow = cv2.inRange(hsv_jpg, lower_yellow, upper_yellow)
    result_yellow = cv2.bitwise_and(jpg, jpg, mask=mask_yellow)

    # finding contours

    banana_contouries = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    banana_contouries = banana_contouries[0]
    for c in banana_contouries:
        x, y, w, h = cv2.boundingRect(c)
        print('banana width', w)
        if w > 119:
            cv2.rectangle(jpg, (x, y), (x + w, y + h), (0, 0, 255), 2)
            banana += 1

    lower_orange = np.array([10, 200, 200])
    upper_orange = np.array([25, 255, 255])
    mask_orange = cv2.inRange(hsv_jpg, lower_orange, upper_orange)
    result_orange = cv2.bitwise_and(jpg, jpg, mask=mask_orange)
    orange_contouries = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    orange_contouries = orange_contouries[0]
    for o in orange_contouries:
        x, y, w, h = cv2.boundingRect(o)
        print('orange width', w)
        if w > 64:
            cv2.rectangle(jpg, (x, y), (x + w, y + h), (255, 0, 0), 2)
            orange += 1

    # lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([8, 255, 255])

    # upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160, 100, 20])
    upper2 = np.array([179, 255, 255])

    lower_mask = cv2.inRange(hsv_jpg, lower1, upper1)
    upper_mask = cv2.inRange(hsv_jpg, lower2, upper2)

    apple_mask = lower_mask + upper_mask
    result_apple = cv2.bitwise_and(jpg, jpg, mask=apple_mask)
    apple_contours = cv2.findContours(apple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    apple_contours = apple_contours[0]
    for o in apple_contours:
        x, y, w, h = cv2.boundingRect(o)
        print('Apple widht: ', w)
        if w > 100:
            cv2.rectangle(jpg, (x, y), (x + w, y + h), (0, 255, 0), 2)
            apple += 1

    return {'apple': apple, 'banana': banana, 'orange': orange}


@click.command()
@click.option('-p', '--data_path', help='Path to data directory')
@click.option('-o', '--output_file_path', help='Path to output file')
def main(data_path, output_file_path):
    img_list = glob(f'{data_path}/*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        fruits = detect_fruits(img_path)

        filename = img_path.split('/')[-1]

        results[filename] = fruits

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)


if __name__ == '__main__':
    main()