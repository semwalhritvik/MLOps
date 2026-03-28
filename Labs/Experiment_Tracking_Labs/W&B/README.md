1. Project Overview
This lab demonstrates how to integrate Weights & Biases (W&B) into a standard Scikit-Learn workflow. Using the Wine Recognition dataset and a Random Forest Classifier, I practiced adapting experiment tracking across different machine learning frameworks.

2. Steps Performed
Environment Configuration: 
* Set up a Python virtual environment in VS Code.

Resolved the ServicePollForTokenError by forcing the WANDB_START_METHOD to thread to ensure compatibility with the VS Code Jupyter extension.

Data Preparation: 
* Utilized the sklearn.datasets.load_wine module to fetch a 13-feature multi-class dataset.

Performed a 70/30 train-test split to evaluate model generalization.

Model Implementation: 
* Initialized a RandomForestClassifier with a defined set of hyperparameters (n_estimators, max_depth).

W&B Integration:
Config Logging: Used wandb.config to save model parameters, ensuring every experiment is reproducible.
Performance Metrics: Logged the final Error Rate to the W&B run summary.
Rich Visualizations: Generated an interactive Confusion Matrix using wandb.sklearn.plot_confusion_matrix to identify which wine classes were most frequently confused by the model.

3. Key Learnings
Framework Agnostic Tracking: Learned that W&B’s sklearn integration is highly flexible and can be applied to almost any tabular data problem beyond just Gradient Boosting.

Data Science Workflow: Reinforced the MLOps habit of logging "Metadata first, Metrics second," which is a core skill for my graduate studies at Northeastern.

How to Use This Notebook
Install dependencies: pip install wandb scikit-learn numpy

Authenticate: Ensure you are logged into W&B via wandb.login().

Run: Execute all cells. The link to your interactive dashboard will appear in the output of the wandb.init() cell.