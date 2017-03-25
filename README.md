# Introduction
Here have an algorithm to identify paragraphs in an image with text. It have the modules `images.py`, `generate_image_from_text.py`, `identify_paragraph_in_image.py`, `experiment.py` and `tests.py`.
The module `images.py` is the main module to identify paragraphs in an image file. The module `generate_image_from_text.py`
generate an image file from a string. The module `identify_paragraph_in_image.py` receive a image with text and identify paragraphs in this image. The module `expriments.py` run an experiment that generate a lot of images file with text and run the algorithm to identify the paragraphs. After run a experiment is print the statistics about the correct answers. The module `tests.py` have unit tests to algorithms.

# Constraints
The algorithm to identify paragraphs in a text consider the background of the image is white and the color of the text is black.
To run this solution is necessary have the Python3.

# Experiment
To verify the accuracy of the algorithm, the module `experiment.py` run a experiment and verify the answers. You can specific the number max of experiments. Each experiment is composed by 300 images files with text, generated randomly. These 300 images is divide by in three groups: 1) have 100 images with 2 paragraphs each, 2) have 100 images with 3 paragraphs each and 3) have 100 images with 4 paragraphs each.

The algorithm to identify paragraphs use a function as parameter to calculate the average of blank lines between the text and identify paragraphs. In the experiment we use the Arithmetic mean and Geometric mean.
The images generate have the mask name `{a}_{b}_{c}_{s}.png`, where `a` is the name function of calculate the average, `b` is the number of paragraphs in the image, `c` is o number of experiment and `d` is the number of the image in the experiment.

After run an experiment is print the statistics about the tests. The output of a experiment have the number of tests, number of correct answers by each method and the name image files with wrong answers. Below is an example of the output of an experiment:
```
Quantity Tests: 300.0
#Correct answers by method: {'average': 300, 'gmean': 299}
Name file incorrect answers: ['result/gmean_4_1_92.png']
```

# Identify paragraph in a image file with text
You can run the command
```
python identify_paragraph_in_image.py image --dest name_file_output
```
where `image` is the input name image file with a text to identify paragraphs. The parameter `name_file_output` is optional and is where the image output is generated. The image output is the image input with the black lines to divide paragraphs identified.

After run, the algorithm also print the number of paragraphs identified.
