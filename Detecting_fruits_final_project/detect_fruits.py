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
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # TODO: Implement detection method.
    boundaries_orange = [
        [[0, 0, 0], [80, 165, 255]],
    ]
    boundaries_apple = [
        [[31, 91, 82], [74, 255, 210]],
    ]
    fruits=dict()
    print(boundaries_orange[0][0])
    lower_orange = np.array(boundaries_orange[0][0], np.uint8)
    upper_orange = np.array(boundaries_orange[0][1], np.uint8)
    lower_apple = np.array(boundaries_apple[0][0], np.uint8)
    upper_apple = np.array(boundaries_apple[0][1], np.uint8)
    print(len(lower_orange.shape))
    mask = cv2.inRange(img, lower_orange, upper_orange)
    output_orange = cv2.bitwise_and(img, img, mask=mask)
    output_orange = cv2.cvtColor(output_orange, cv2.COLOR_BGR2GRAY)
    circles_orange = cv2.HoughCircles(output_orange, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=10, param2=40,
                                      minRadius=110, maxRadius=140)

    circles = np.uint16(np.around(circles_orange))
    fruits['o'] = circles

    mask_apple = cv2.inRange(img, lower_apple, upper_apple)
    output_apple = cv2.bitwise_and(img, img, mask=mask_apple)
    output_apple = cv2.cvtColor(output_apple, cv2.COLOR_BGR2GRAY)
    circles_apple = cv2.HoughCircles(output_apple, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=10, param2=30,
                                     minRadius=110, maxRadius=135)
    circles = np.uint16(np.around(circles_apple))
    fruits['g'] = circles

    for color, circle in fruits.items():
        if color == 'o':
            for circl in circle[0, :]:
                if circl[2] >= 110:
                    cv2.circle(img, (circl[0], circl[1]), circl[2], (0, 0, 255), 2)

        else:
            for circl in circle[0, :]:
                if circl[2] >= 110:
                    cv2.circle(img, (circl[0], circl[1]), circl[2], (0, 255, 0), 2)
    apple = 0
    banana = 0
    orange = 0

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