#!/usr/bin/env python
# coding: utf-8

# ## Introduction to MACHINE LEARNING

# In[ ]:


Machine learning (ML) is a branch of artificial intelligence (AI) that enables computers to “self-learn” from training data
and improve over time, without being explicitly programmed. Machine learning algorithms are able to detect patterns in data
and learn from them, in order to make their own predictions.


# ## AI vs ML vs DL vs Data Science - The difference between them

# In[ ]:


## AI
🔹Artificial Intelligence (AI) enables machines to think by understanding, learning from the data, and taking decisions
based on patterns hidden in the data or make inferences that would otherwise be very difficult for humans to make manually.
The end goal of using ML or DL is to create an AI application or machine as smart as humans.


# In[ ]:


## ML
🔹Machine Learning (ML) is a subset of AI; it provides us statistical tools/techniques like Supervised, Unsupervised, and 
Reinforcement learning to explore and analyze the data.


# In[ ]:


## DL
🔹Deep Learning (DL) is further a subset of ML, and the main idea behind it is to make machines learn by mimicking the 
human brain. Here, we create a multi neural network architecture with the help of different techniques like ANN, CNN, and
RNN.


# In[ ]:


## DS
🔹Data Science (DS) is basically drawing insights from structured and unstructured data either by using ML or DL or without
these techniques. We can even use different visualization tools, statistics, and probability to gain these insights.


# ## Types of ML

# In[ ]:


=> Supervised Machine Learning
=> Unsupervised Machine Learning
=> Semi-Supervised Machine Learning
=> Reinforcement Learning


# ### Supervised ML

# In[ ]:


The main goal of the supervised learning technique is to map the input variable(x) with the output variable(y). 
Some real-world applications of supervised learning are Risk Assessment, Fraud Detection, Spam filtering, etc.


# In[ ]:


# Categories of Supervised Machine Learning
Classification
Regression


# In[ ]:


# Advantages:
=> Since supervised learning work with the labelled dataset so we can have an exact idea about the classes of objects.
=> These algorithms are helpful in predicting the output on the basis of prior experience.

# Disadvantages:
=> These algorithms are not able to solve complex tasks.
=> It may predict the wrong output if the test data is different from the training data.
=> It requires lots of computational time to train the algorithm.

# Applications of Supervised Learning
=> Image Segmentation: Supervised Learning algorithms are used in image segmentation. In this process, image classification
    is performed on different image data with pre-defined labels.
=> Medical Diagnosis: Supervised algorithms are also used in the medical field for diagnosis purposes. It is done by using 
    medical images and past labelled data with labels for disease conditions. With such a process, the machine can identify
    a disease for the new patients.
=> Fraud Detection - Supervised Learning classification algorithms are used for identifying fraud transactions, fraud 
customers, etc. It is done by using historic data to identify the patterns that can lead to possible fraud.
=> Spam detection - In spam detection & filtering, classification algorithms are used. These algorithms classify an email as
spam or not spam. The spam emails are sent to the spam folder.
=> Speech Recognition - Supervised learning algorithms are also used in speech recognition. The algorithm is trained with 
voice data, and various identifications can be done using the same, such as voice-activated passwords, voice commands, etc.


# ## Unsupervised ML

# In[ ]:


The main aim of the unsupervised learning algorithm is to group or categories the unsorted dataset according to the 
similarities, patterns, and differences. Machines are instructed to find the hidden patterns from the input dataset.


# In[ ]:


Categories of Unsupervised Machine Learning:-
    => Clustering
    => Association


# In[ ]:


# Advantages:
=> These algorithms can be used for complicated tasks compared to the supervised ones because these algorithms work on the 
unlabeled dataset.
=> Unsupervised algorithms are preferable for various tasks as getting the unlabeled dataset is easier as compared to the 
labelled dataset.

# Disadvantages:
=> The output of an unsupervised algorithm can be less accurate as the dataset is not labelled, and algorithms are not
trained with the exact output in prior.
=> Working with Unsupervised learning is more difficult as it works with the unlabelled dataset that does not map with the 
output.

# Applications of Unsupervised Learning
=> Network Analysis: Unsupervised learning is used for identifying plagiarism and copyright in document network analysis of
    text data for scholarly articles.
=> Recommendation Systems: Recommendation systems widely use unsupervised learning techniques for building recommendation 
    applications for different web applications and e-commerce websites.
=> Anomaly Detection: Anomaly detection is a popular application of unsupervised learning, which can identify unusual data 
    points within the dataset. It is used to discover fraudulent transactions.
=> Singular Value Decomposition: Singular Value Decomposition or SVD is used to extract particular information from the 
    database. For example, extracting information of each user located at a particular location.


# ## Semi-Supervised Learning

# In[ ]:


Semi-Supervised learning is a type of Machine Learning algorithm that lies between Supervised and Unsupervised machine 
learning. It represents the intermediate ground between Supervised (With Labelled training data) and Unsupervised learning
(with no labelled training data) algorithms and uses the combination of labelled and unlabeled datasets during the training 
period.
To overcome the drawbacks of supervised learning and unsupervised learning algorithms, the concept of Semi-supervised 
learning is introduced. The main aim of semi-supervised learning is to effectively use all the available data, rather than
only labelled data like in supervised learning. Initially, similar data is clustered along with an unsupervised learning
algorithm, and further, it helps to label the unlabeled data into labelled data. It is because labelled data is a 
comparatively more expensive acquisition than unlabeled data.


# In[ ]:


# Advantages:
=> It is simple and easy to understand the algorithm.
=> It is highly efficient.
=> It is used to solve drawbacks of Supervised and Unsupervised Learning algorithms.

# Disadvantages:
=> Iterations results may not be stable.
=> We cannot apply these algorithms to network-level data.
=> Accuracy is low.


# ##  Reinforcement Learning

# In[ ]:


Reinforcement learning works on a feedback-based process, in which an AI agent (A software component) automatically explore 
its surrounding by hitting & trail, taking action, learning from experiences, and improving its performance. Agent gets 
rewarded for each good action and get punished for each bad action; hence the goal of reinforcement learning agent is to 
maximize the rewards.
Due to its way of working, reinforcement learning is employed in different fields such as Game theory, Operation Research,
Information theory, multi-agent systems.

A reinforcement learning problem can be formalized using Markov Decision Process(MDP). In MDP, the agent constantly 
interacts with the environment and performs actions; at each action, the environment responds and generates a new state.


# In[ ]:


# Categories of Reinforcement Learning
=> Positive Reinforcement Learning
=> Negative Reinforcement Learning

# Real-world Use cases of Reinforcement Learning
=> Video Games:
RL algorithms are much popular in gaming applications. It is used to gain super-human performance. Some popular games that
use RL algorithms are AlphaGO and AlphaGO Zero.

=> Resource Management:
The "Resource Management with Deep Reinforcement Learning" paper showed that how to use RL in computer to automatically 
learn and schedule resources to wait for different jobs in order to minimize average job slowdown.

=> Robotics:
RL is widely being used in Robotics applications. Robots are used in the industrial and manufacturing area, and these robots
are made more powerful with reinforcement learning. There are different industries that have their vision of building 
intelligent robots using AI and Machine learning technology.

=> Text Mining
Text-mining, one of the great applications of NLP, is now being implemented with the help of Reinforcement Learning by 
Salesforce company.


# In[ ]:


# Advantages:
=> It helps in solving complex real-world problems which are difficult to be solved by general techniques.
=> The learning model of RL is similar to the learning of human beings; hence most accurate results can be found.
=> Helps in achieving long term results.

# Disadvantages:
=> RL algorithms are not preferred for simple problems.
=> RL algorithms require huge data and computations.
=> Too much reinforcement learning can lead to an overload of states which can weaken the results.


# ## How do you validate a dataset in machine learning?

# In[ ]:


# Cross-Validation in Machine Learning
=> Reserve a subset of the dataset as a validation set.
=> Provide the training to the model using the training dataset.
=> Now, evaluate model performance using the validation set. If the model performs well with the validation set, perform 
the further step, else check for the issues


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




