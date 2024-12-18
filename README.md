<!-- @format -->

# [Iris- A small classic dataset from Fisher, 1936.](https://archive.ics.uci.edu/dataset/53/iris)

=========================

### Classification problem

---

Out of three classes two are linearly separable and one is separable non linearly.

### Dataset Information

##### Each instance is a plant

#### Additional information

This is one of the earliest datasets used in the literature on classification methods and widely used in statistics and machine learning. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are not linearly separable from each other.

#### Evaluation score :

Seems Overfitting , need to check what else can improve model accuracy score.

##### Test :---- When deleted features based on correlation heat map of independent feature.

recall_score: 71%

f1_score: 69%

precision: 71%

##### Test ----included all independent features.

recall_score: 89%

f1_score: 90%

precision: 90%

<hr/>

![alt model test result](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/Test_result.PNG)

<hr/>

##### Train ----When deleted features based on correlation heat map of independent feature.

recall_score: 95%

f1_score: 95%

precision: 96%

<hr/>

##### Train ----included all independent features.

recall_score: 100%

f1_score: 100%

precision: 100%

<hr/>

![alt model train result](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/Train_result.PNG)

<hr/>

### Exploratory Data Analysis

#### Check Data Imbalance

![alt dataset imbalane check](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/class_count_check_data_imbalance.png)

#### Features histogram plot

![alt attributes histogram](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/attribute_histogram_plots.png)

#### Correlation checks

![alt data correlation](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/features_correlation.png)

#### Check for Outliers

![alt outliers](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/check_for_outliers.png)

#### Pairplot to find independent features relation with each other

![alt pairplot](https://github.com/brajeshkumar1989/IrisDataPrediction/blob/main/images/compare_features.png)

#### Overall status of the project: in progress

## completed:

1. Data ingestion
2. Data validation
3. Data Transformation
4. Model training
   a. compare different model
   b. find best parameters and model
5. Model Evaluation

## InProgress:

1. deployment and uiux

##### author:

#### Brajesh kumar
