# Customer Segmentation for Online Retail Using RFM Analysis and Clustering

## Project Overview

This project performs an end-to-end customer segmentation analysis on an online retail dataset using **RFM (Recency, Frequency, Monetary)** metrics and multiple clustering algorithms. The goal is to identify actionable customer segments to drive targeted marketing strategies and improve business decision-making.

The analysis compares three clustering methods:
- **K-Means**
- **DBSCAN**
- **Hierarchical Clustering**

and evaluates their performance using internal validation metrics and business interpretability.

---

## Repository Structure

```
├── .gitignore                                          # Git ignore file
├── LICENSE                                             # MIT License
├── README.md                                           # Project documentation
├── requirements.txt                                    # Python dependencies
├── final_copy_of_Machine_Learning_2_project.ipynb     # Jupyter Notebook (full analysis)
└── final_copy_of_Machine_Learning_2_project.py        # Python script version
```

---

## Dataset

**Source:** [Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) (UCI Machine Learning Repository)

- Two sheets: Year 2009–2010 and Year 2010–2011
- Contains transactional data from a UK-based online retailer
- Key fields: Invoice number, Stock code, Description, Quantity, Invoice date, Unit price, Customer ID, Country

---

## Team Roles & Responsibilities

| Role | Name | Responsibility |
|------|------|------------|----------------|
| **Project Manager & Lead Writer** | Esther Wanjiru | Project coordination, documentation, final report |
| **Data Cleaning Specialist** | Brandon Kungu  | Data preprocessing, outlier handling, missing value treatment |
| **EDA Analyst** | Otieno Evance | Exploratory data analysis, visualization, country sales analysis |
| **Feature Engineer** | Peter James Onyango  | RFM construction, log transformation, scaling |
| **GitHub Coordinator / Ops Engineer** | Jeff Omondi  | Repository management, environment setup, script automation |
| **K-Means Modeller & Evaluator** | Martin Waithanji | K-Means clustering, elbow method, silhouette scoring |
| **Hierarchical Clustering Specialist** | Kelvin Kipkoech | Hierarchical clustering, dendrogram interpretation |
| **PCA & Visualization Lead** | Allan Gift  | PCA dimensionality reduction, 2D/3D visualizations |

---

## Key Steps in the Analysis

### 1. Data Cleaning & Preprocessing
- Standardized column names
- Converted data types
- Filtered out negative quantities and prices
- Flagged cancelled transactions
- Removed exact duplicate rows

### 2. Exploratory Data Analysis (EDA)
- Distribution of quantity, unit price, and revenue
- Outlier detection via box plots and log scaling
- Sales by country
- Missing value analysis (especially customer ID)

### 3. RFM Feature Engineering
- **Recency:** Days since last purchase
- **Frequency:** Number of unique invoices
- **Monetary:** Total revenue per customer
- Log transformation + StandardScaler applied

### 4. Clustering Algorithms
- **K-Means:** Elbow method + silhouette score to select k=3
- **DBSCAN:** K-distance graph to tune epsilon, min_samples
- **Hierarchical Clustering:** Dendrogram + Ward linkage

### 5. Cluster Evaluation
- Silhouette Score
- Davies–Bouldin Index
- Calinski–Harabasz Index

### 6. Visualization
- 3D scatter plots (Plotly)
- 2D PCA projections
- Feature loading heatmaps
- Radar-style bar charts of scaled RFM means

---

## Results Summary

### Internal Metrics Comparison

| Algorithm               | k (clusters) | Silhouette | Davies–Bouldin | Calinski–Harabasz |
|------------------------|--------------|------------|----------------|-------------------|
| K-Means                | 3            | 0.347      | 1.037          | 5215.59           |
| Hierarchical           | 3            | 0.323      | 1.069          | 3970.60           |
| DBSCAN (refined)       | 2 ( + noise )| 0.279      | 1.010          | 2898.70           |

### K-Means Segments (Recommended)

| Cluster | Segment                        | Recency (days) | Frequency | Monetary ($) | Size |
|---------|--------------------------------|----------------|-----------|--------------|------|
| 1       | Best Customers                 | 32.9           | 19.1      | 10,789.63    | 1228 |
| 0       | Regular Customers              | 109.9          | 4.3       | 1,538.82     | 2267 |
| 2       | Lapsed / Low-Value Customers   | 375.1          | 1.5       | 397.52       | 2383 |

### DBSCAN Unique Insight
- **Noise cluster (72 customers):** Extremely high-value outliers  
  - Frequency: ~62 orders  
  - Monetary: ~$71,675  
  - *Recommendation:* Dedicated account management

---

## Business Recommendations

| Segment                          | Strategy |
|----------------------------------|----------|
| Best Customers (K-Means Cluster 1) | VIP programs, loyalty rewards, early access, personalized outreach |
| Regular Customers (K-Means Cluster 0) | Cross-selling, upselling, retention campaigns |
| Lapsed Customers (K-Means Cluster 2) | Win-back offers or deprioritization based on ROI |
| DBSCAN Outliers (Noise)           | White-glove service, individual account management |

---

## How to Run the Code

### Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Execution

#### Option 1: Run the Python script

```bash
python final_copy_of_Machine_Learning_2_project.py
```

#### Option 2: Run the Jupyter Notebook

Open `final_copy_of_Machine_Learning_2_project.ipynb` in Jupyter Lab or Google Colab.

> **Note:** The script includes Google Drive mounting for Colab. If running locally, remove or comment out the `drive.mount` and zip extraction cells.

---

## Visual Highlights

- 3D interactive cluster plots (Plotly)
- 2D PCA projections showing cluster separation
- Dendrogram for hierarchical clustering
- K-distance graph for DBSCAN tuning
- Correlation heatmaps and feature loadings

---

## Conclusion

**K-Means clustering is recommended** for this business problem due to:
- Highest internal validation scores
- Most interpretable and actionable segments
- Simplicity and scalability

DBSCAN provides complementary value by identifying extreme outliers, while hierarchical clustering serves as a robust alternative.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Authors

**Team Members – Machine Learning 2 Project**

- Esther Wanjiru  – Project Manager & Lead Writer
- Brandon Kungu  – Data Cleaning Specialist
- Otieno Evance  – EDA Analyst
- Peter James Onyango  – Feature Engineer
- Jeff Omondi  – GitHub Coordinator / Ops Engineer
- Martin Waithanji  – K-Means Modeller & Evaluator
- Kelvin Kipkoech  – Hierarchical Clustering Specialist
- Allan Gift  – PCA & Visualization Lead
- Moris Gachanja-DBScan Analyst
  
---

## Acknowledgments

- UCI Machine Learning Repository for the Online Retail II dataset
- scikit-learn, pandas, seaborn, matplotlib, and plotly communities
```
