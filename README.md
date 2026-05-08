# ML II Capstone – Customer Segmentation with Unsupervised Learning

## Project Description

This project applies unsupervised machine learning techniques to segment retail customers using transaction data from the UCI Online Retail dataset. The workflow includes exploratory data analysis, RFM feature engineering, preprocessing, dimensionality reduction with PCA, and clustering with K-Means, Hierarchical Agglomerative Clustering, and DBSCAN.

The goal is to identify meaningful customer groups such as high-value loyal customers, recent low-to-mid value customers, cooling customers, and inactive or at-risk customers. Because the dataset does not include ground-truth customer segment labels, clustering is used to discover natural behavioral patterns in the data.

## Dataset Source

The dataset used for this project is the UCI Online Retail dataset.

Download URL:

https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx

To download the dataset automatically, run:

```bash
python download_data.py
```

This will save the file to:

```text
data/Online Retail.xlsx
```

Do not commit the downloaded `.xlsx` file to the repository. The dataset is excluded through `.gitignore`.

## Required Libraries

The project uses the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- openpyxl
- jupyter

Install dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository.
2. Install the required libraries.
3. Download the dataset using the provided script.
4. Open the notebook in Jupyter.
5. Run the notebook cells from top to bottom.

Example commands:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
pip install -r requirements.txt
python download_data.py
jupyter notebook
```

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── download_data.py
├── .gitignore
├── data/
│   └── README.md
├── notebooks/
│   └── customer_segmentation.ipynb
├── reports/
│   └── final_report.pdf
└── outputs/
    └── figures/
```

## Main Workflow

The analysis follows this pipeline:

1. Load and inspect the Online Retail dataset.
2. Clean invalid transactions and remove missing customer IDs.
3. Engineer RFM features:
   - Recency
   - Frequency
   - Monetary value
4. Preprocess features using IQR outlier capping, log transformation, and StandardScaler.
5. Apply PCA for two-dimensional visualization.
6. Train and evaluate:
   - K-Means
   - Hierarchical Agglomerative Clustering
   - DBSCAN
7. Compare algorithms using:
   - Silhouette Score
   - Davies-Bouldin Index
   - Calinski-Harabasz Index
8. Recommend the best clustering model for marketing segmentation.

## Final Recommendation

Based on the clustering evaluation, K-Means with four clusters is recommended for marketing segmentation because it produced the strongest internal validation scores and the most interpretable customer segments.
