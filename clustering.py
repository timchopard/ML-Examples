import numpy as np                      # Mathematics etc.
import pandas as pd                     # Dataframes

from sklearn.datasets import load_iris  # Downloads a dataset
from sklearn.cluster import KMeans      # The clustering model
from sklearn.metrics import f1_score    # Evaluation metric

raw_data = load_iris()                  # Load data
df = pd.DataFrame(data=raw_data.data, columns=raw_data.feature_names)
df['Y'] = raw_data.target               # Set labels

print(df.head(3))                       # Show first 3 rows

clusters = 3                            # Define the number of clusters
seed = 31                               # Set a seed for reproducability
iterations = 250                        # Set the maximum iterations
model = KMeans(n_clusters=clusters, max_iter=iterations, random_state=seed)

model.fit(df.drop(columns=["Y"]))       # Fit the model to the data
df["Y_hat"] = model.labels_             # Add the predicted values to the DF

evaluation = f1_score(                  # Evaluate the results
    df["Y"],
    df["Y_hat"],
    average="micro"
)

print(f"F1 = {evaluation:.3f}")         # Show the evaluation
