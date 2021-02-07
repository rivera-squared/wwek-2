#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy as sp


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# In[3]:


get_ipython().run_cell_magic('file', 'hw_data.csv', 'id,sex,weight,height\n1,M,190,77\n2,F,120,70\n3,F,110,68\n4,M,150,72\n5,O,120,66\n6,M,120,60\n7,F,140,70')


# # Python

# ## 1. Finish creating the following function that takes a list and returns the average value.

# In[4]:


def average(my_list):
    total = 0
    for item in my_list:
        total = item + total
    
    return total/len(my_list)

average([1,2,1,4,3,2,5,9])


# ## 2. Using a Dictionary keep track of the count of numbers (or items) from a list

# In[6]:


def counts(my_list):
    counts = dict()
    for item in my_list:
        item
    
    return len(my_list)

counts([1,2,1,4,3,2,5,9])    


# ## 3.  Using the `counts()` function and the `.split()` function, return a dictionary of most occuring words from the following paragraph. Bonus, remove punctuation from words.

# In[7]:


paragraph_text = '''
For a minute or two she stood looking at the house, and wondering what to do next, when suddenly a footman in livery came running out of the wood—(she considered him to be a footman because he was in livery: otherwise, judging by his face only, she would have called him a fish)—and rapped loudly at the door with his knuckles. It was opened by another footman in livery, with a round face, and large eyes like a frog; and both footmen, Alice noticed, had powdered hair that curled all over their heads. She felt very curious to know what it was all about, and crept a little way out of the wood to listen.
The Fish-Footman began by producing from under his arm a great letter, nearly as large as himself, and this he handed over to the other, saying, in a solemn tone, ‘For the Duchess. An invitation from the Queen to play croquet.’ The Frog-Footman repeated, in the same solemn tone, only changing the order of the words a little, ‘From the Queen. An invitation for the Duchess to play croquet.’
Then they both bowed low, and their curls got entangled together.
Alice laughed so much at this, that she had to run back into the wood for fear of their hearing her; and when she next peeped out the Fish-Footman was gone, and the other was sitting on the ground near the door, staring stupidly up into the sky.
Alice went timidly up to the door, and knocked.
‘There’s no sort of use in knocking,’ said the Footman, ‘and that for two reasons. First, because I’m on the same side of the door as you are; secondly, because they’re making such a noise inside, no one could possibly hear you.’ And certainly there was a most extraordinary noise going on within—a constant howling and sneezing, and every now and then a great crash, as if a dish or kettle had been broken to pieces.
‘Please, then,’ said Alice, ‘how am I to get in?’
‘There might be some sense in your knocking,’ the Footman went on without attending to her, ‘if we had the door between us. For instance, if you were inside, you might knock, and I could let you out, you know.’ He was looking up into the sky all the time he was speaking, and this Alice thought decidedly uncivil. ‘But perhaps he can’t help it,’ she said to herself; ‘his eyes are so very nearly at the top of his head. But at any rate he might answer questions.—How am I to get in?’ she repeated, aloud.
‘I shall sit here,’ the Footman remarked, ‘till tomorrow—’
At this moment the door of the house opened, and a large plate came skimming out, straight at the Footman’s head: it just grazed his nose, and broke to pieces against one of the trees behind him.'''

from collections import Counter

paragraph_text = paragraph_text.split(" ")
count = Counter(paragraph_text)
count.most_common()


# ## 4. Read in a file and write each line from the file to a new file Title-ized
# 
# `This is the first line` ->  `This Is The First Line`
# 
# Hint: There's a function to do this

# In[1]:


file = open("file_1.txt", "w")
file.write("This Is The First Line")
file.close()

file = open("file_1.txt", "r")
str1 = file.readline()
print(str1)
file.close()


# # Numpy

# ## 1. Given a list, find the average using a numpy function. 

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import traceback
import matplotlib.pyplot as plt

import numpy as np


# In[4]:


simple_list = [1,2,1,4,3,2,5,9]
average = np.average(simple_list)
average


# ## 2. Given two lists of Heights and Weights of individual, calculate the BMI of those individuals, without writing a `for-loop`

# In[7]:


heights = [174, 173, 173, 175, 171]
weights = [88, 83, 92, 74, 77]

ht = np.array(heights)
wt = np.array(weights)

z = (wt) / ((ht/100)**2)
z


# ## 3. Create an array of length 20 filled with random values (between 0 to 1) 

# In[8]:


np.random.rand(20)


# ## Bonus. 1. Create an array with a large (>1000) length filled with random numbers from different distributions (normal, uniform, etc.). 2. Then, plot a histogram of these values. 

# In[12]:


normal = np.random.normal(0,1,1200)

len(normal)


# In[11]:


import matplotlib.pyplot as plt

plt.hist(normal)


# # Pandas

# ## 1. Read in a CSV () and display all the columns and their respective data types 

# In[13]:


import pandas as pd
ab = pd.read_csv('/Users/edwardriverarivera/Desktop/mlnn/2/hw_data.csv')

ab


# ## 2. Find the average weight 

# In[14]:


wt_1 = ab.iloc[:,2]
np.average(wt_1)


# ## 3. Find the Value Counts on column `sex` 

# In[15]:


sex = ab.iloc[:,1]
sex.value_counts()


# ## 4. Plot Height vs. Weight 

# In[16]:


ht_1 = ab.iloc[:,3]
plt.scatter(ht_1, wt_1)
plt.title("Height vs. Weight Plot")


# ## 5. Calculate BMI and save as a new column

# In[17]:


bmi = wt_1 / (ht_1**2) * 703 # Unlike previous BMI formula, I had to re-do the formula to implement the 'English' system
bmi_1 = list(bmi)
ab.loc[:, 'bmi'] = bmi_1
ab


# ## 6. Save sheet as a new CSV file `hw_dataB.csv`

# In[18]:


ab.to_csv('hw_dataB.csv')


# ## Run the following

# In[19]:


get_ipython().system('cat hw_dataB.csv')

