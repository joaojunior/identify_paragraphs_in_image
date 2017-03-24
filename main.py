import argparse

import cv2

from images import identify_paragraphs_in_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(dest="file_name_input", metavar="FILE",
                        help="image to read")
    parser.add_argument("--dest", dest="file_name_output",
                        metavar="FILE",
                        help="output image", default='output.png')
    args = parser.parse_args()
    file_name_input = args.file_name_input
    file_name_output = args.file_name_output

    image = cv2.imread(file_name_input, 0)
    number_paragraphs, image = identify_paragraphs_in_image(image)
    cv2.imwrite(file_name_output, image)
    print(number_paragraphs)
