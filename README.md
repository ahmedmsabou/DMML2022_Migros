# Migros - Ahmed and Joris

# Presentation:
https://youtu.be/re6JNey5R4I
The link to our presentation for the project.

# Organization:

There are 3 folders. 
The 'Data' folder contains the data that was given in the project.
The 'Code' folder contains 2 files consisting of the code of our project. One file has the 4 required algorithms, while the other has our implementation of the camemBERT model.
The 'Presentation' folder contains the presentation used during the video.
 
# Summary of Project

The goal of this project is to correctly classify the difficulty level of French sentences. For this purpose, we first wanted to know what the baseline performance is. This will help to compare our results and check if a model is working properly.

We found that the most common class among 6 classes has 813 out of 4800 observations, meaning that we have a basline of 0.169375!

Thereafter, we used 4 models to classify the difficulty of French sentences. After performing hyper-parameter tuning, and using 20% of the data as validation, we obtain results for the KNN, random forest, logistic regression, and decision tree models. Moreover, we have used the camamBERT model, which is pre-trained on French sentences. Below, the results are showcased.

![image](https://user-images.githubusercontent.com/114418721/209132572-09dacff0-5413-444d-8cb1-7e61d2715bfa.png)

Focusing mainly on the accuracy, one can see that the decision tree had the wost performance on this data set. As expected, the random forest outperformed the decision tree, while the kNN model was unable to beat the random forest. Out of the 4 base models, the logistic regression performed best, with a 46% accuracy on the validation set.

The best model however, is the camamBERT model, with 57,4% accuracy on the validation set. One may use a confusion matrix to discover how the BERT model tends to predict the difficulty of a sentence incorrectly. Clearly, one sees that most incorrect predictions are right next to the diagonal of the matrix, implying that it is usually only 1 diffuclty level of the true value.

![image](https://user-images.githubusercontent.com/114418721/209134335-4bb43e2e-249a-4704-ae77-260067abe6e4.png)
