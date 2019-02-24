---
interact_link: content/interests.ipynb
kernel_name: python3
title: 'Interests'
prev_page:
  url: /education
  title: 'Education'
next_page:
  url: /cocurriculars
  title: 'Co-Curriculars'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Interests

## Coding
Languages: Python, HTML, CSS, SQLite, UNIX Command Line, Git | Currently Learning: Java, R, Ruby


While watching the Data 8 lectures as a part of my position at ETS, I became intrigued by the prospect of data science; I thought that it was amazing how powerful computations could be processed in seconds and how the analysis of large data sets could be performed so quickly. It was in watching these lectures and doing some experiments with the `datascience` library in my free time that I became enamoured with the prospect of learning coding beyond the data-specific aspects of Python libraries. I decided to enroll in Data 8 for Summer 2018 so that I could get credit for the practice I put in while watching the lectures, and then I moved to CS 88.


In my own free time, I used what I learned between sitting in on Data 8 lectures and some work I did in CS 88 to write a Sudoku object that can open a file with a sudoku puzzle, read it, and determine if it is a valid solution, among other things. The full .py file can be found [on GitHub](https://github.com/chrispyles/python-projects/blob/master/sudoku/sudoku.py), but I have included the function that checks the validity of the solved puzzle below.

```python
def check_puzzle(self):
    """
    >>> s = Sudoku('filled_puzzle_1.txt')
    >>> s.check_puzzle()
    Congratulations! Your answers check out!
    """
    collection = []
    for i in range(1, 10):
        for j in range(9):
            num_occurances = sum([i == k[j] for k in self.rows])
                if num_occurances == 1:
                    collection += [1]
                else:
                    print('Sorry, but your answers do not work.')
    for i in range(1, 10):
        for j in self.rows:
            num_occurances = sum([i == j[k] for k in range(9)])
                if num_occurances == 1:
                    collection += [1]
                else:
                    print('Sorry, but your answers do not work.')
    if sum(collection) == 162:
        print('Congratulations! Your answers check out')
        self.completed = True
    else:
        print('Sorry, but your answers do not work.')
```

The function prints a line that tells you whether or not your table is a solution by going through each row and column and verifying that each digit in `range(1, 10)` appears only once (note that the `range` function is inclusive on the first parameter but not on the second).

Over the summer that I took Data 8, I worked on practice problems from past iterations of the CS 61A course (a course at UC Berkeley equivalent to Data 8 and CS 88), and I was introduced to GitHub and its webhosting platform, which inspired me to take up learning HTML and CSS on Codecademy. In a day, I had learned the basics of both languages and had this website up and running. Coding, although a relatively new interest of mine, is something that I want to learn as much as possible about, and which I intend to pursue throughout my life.

## Finance and the Economy
This interest began when I took AP Macroeconomics in high school, and it has grown since. I was fascinated by how different sectors of the economy were so interconnected with each other, and how a small cause somewhere inevitably led to a large effect in a completely different place. Since AP Macro, my interest has grown more specifically into finance; this semester, I am taking Engineering 120, a class on economics and finance, and I hope to get more involved in UC Berkeley's finance community.

## Data Science
At the end of Data 8, I found myself interested in learning more about data science. I decided to learn R, a data-oriented programming language, since it is used in most data science applications, and I also took the knowledge from Data 8 to begin working on other data sets that I could find online. As an example, for [this data set](https://www.kaggle.com/neuromusic/avocado-prices) from Kaggle which has information about avocado prices, I built a k-nearest neighbors classifier to classify avocados as either `'conventional'` or `'organic'`. [This .py file](files/avocado_classifier.py) contains the code for the classifier; it classifies a set of avocados based on the average price, total volume, and total number of bags for that set. The `test_accuracy` function defined in the file showed that the 7-nearest neighbors classifier was 94.8% accurate. You can also find the Jupyter Notebook (in HTML format) that I used while building the classifier and optimizing $k$ in the [Jupyter](https://jupyter.cpyles.com) section of this website.

Another recent project of mine has been based on [an insurance data set](https://www.kaggle.com/mirichoi0218/insurance) I found on Kaggle. It contains some information about different insurance customers, including age, sex, BMI, number of children, region, charges, and whether or not the person was a smoker. In [this Jupyter Notebook](https://nbviewer.jupyter.org/github/chrispyles/jupyter/blob/master/notebooks/insurance/insurance.ipynb), I first tried to see if there was a correlation between BMI and insurance charges; the value of $r$ that I computed was low enough that there might have been a slight correlation, but there certainly wasn't a prevalent one. Next, I decided to test whether or not being a smoker affected what you were charged by insurance companies; to do this, I did an A/B test to see whether or not the distributions of charges for smokers and non-smokers came from the same underlying distribution. I got a p-value of 0 (meaning that the observed value was more extreme that any of the simulated values under the assumption of the null hypothesis), and concluded that being a smoker does affect your insurance charges.
