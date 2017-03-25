import os
from random import randint
from textwrap import wrap

import cv2
from loremipsum import get_paragraphs
from numpy import average
from scipy.stats.mstats import gmean

from images import identify_paragraphs_in_image, text_to_image

folder_output = 'result'
os.makedirs(folder_output, exist_ok=True)
MAX_IMAGE_BY_PARAGRAPH = 100
MAX_PARAGRAPHS = 4
MAX_NUMBER_EXPERIMENTS = 10
quantity_tests = 0
correct_answers = {}
wrong_answers = []
functions = [average, gmean]

for experiment in range(1, MAX_NUMBER_EXPERIMENTS+1):
    for function in functions:
        name = function.__name__
        correct_answers[function.__name__] = correct_answers.get(name, 0)
        for number_paragraphs in range(2, MAX_PARAGRAPHS+1):
            correct = 0
            for i in range(MAX_IMAGE_BY_PARAGRAPH):
                quantity_tests += 1
                file_name_input = '{}_{}_{}_{}.png'.format(function.__name__,
                                                           number_paragraphs,
                                                           experiment,
                                                           i)
                file_name_input = os.path.join(folder_output, file_name_input)
                paragraphs = get_paragraphs(number_paragraphs)
                text = ''
                for paragraph in paragraphs:
                    paragraph = wrap(paragraph, 80)
                    max_lines = randint(1, min(4, len(paragraph)))
                    text += '\n'.join(paragraph[0:max_lines])
                    text += '\n\n'

                text_to_image(text=text, file_name=file_name_input)
                image = cv2.imread(file_name_input, 0)
                result = identify_paragraphs_in_image(image, function)
                cv2.imwrite(file_name_input, result[1])
                if number_paragraphs == result[0]:
                    correct += 1
                else:
                    wrong_answers.append(file_name_input)
            correct_answers[function.__name__] += correct
print('Quantity Tests:', quantity_tests / len(functions))
print('#Correct answers by method:', correct_answers)
print('Name file incorrect answers:', wrong_answers)
