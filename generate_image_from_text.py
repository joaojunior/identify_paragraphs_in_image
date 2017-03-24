import argparse

from images import text_to_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(dest="file_name",
                        help="write image in FILE", metavar="FILE")
    parser.add_argument(dest="text", type=str,
                        help="Text to generate the image")
    args = parser.parse_args()

    text_to_image(text=args.text, file_name=args.file_name)
