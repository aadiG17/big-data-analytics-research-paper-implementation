# 💡 Integrated Framework for Spark-Based Big Data Analytics in Sports Health Monitoring

This project implements the research paper:
**"Integrated Framework for Spark-Based Big Data Analytics in Sports Health Monitoring"**

📚 **Research Paper**: [Springer Link](https://link.springer.com/article/10.1007/s00500-023-09450-9)  
📦 **Dataset**: [Chronic Kidney Disease (CKD)](https://www.kaggle.com/datasets/mansoordaku/ckdisease)

---

## ⚙️ Tech Stack

- 🔥 Apache Spark (Standalone Cluster on Docker)
- 🐍 PySpark (Data Processing + MLlib)
- 🤖 Machine Learning: XGBoost, Random Forest, Decision Tree, SVM, Logistic Regression, KNN
- 📓 Jupyter Notebook (inside Spark master container)
- 📈 Streamlit Web App for Predictions
- 🗃 Hadoop HDFS (optional for distributed storage)

---

## 🛠 Setup Instructions

### 1. Install Docker & Docker Compose
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
```

### 2. Clone and Setup Project
```bash
git clone <your-repo-url>
cd SparkScript
sudo docker-compose build
```

### 3. Start Spark Cluster
```bash
sudo docker-compose up -d
```

### 4. Access Services
- 🔗 Spark Master UI: [http://localhost:9090](http://localhost:9090)
- 🔗 Jupyter Notebook: [http://localhost:8888](http://localhost:8888)
- 🔗 Spark History Server: [http://localhost:18080](http://localhost:18080)

> ✅ Jupyter will print a token in the console — use it to access initially.

---

## 🔬 Machine Learning Implementation

- Dataset loaded into PySpark, cleaned, and transformed
- Models trained and evaluated using accuracy, F1-score, and classification report
- Models saved as `.pkl` and integrated into Streamlit app

### ✅ ML Models Used:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- **XGBoost** *(default in Streamlit UI)*

---

## 🖥 Streamlit Prediction Dashboard

### ⚙️ Run Locally (outside Docker)
```bash
streamlit run app.py
```

- Choose ML model (via dropdown)
- Enter medical attributes manually
- Click "Predict" to get result

---

## 📁 Hadoop Integration *(Optional)*

You can extend this to a Hadoop-based architecture:
- Setup 1 master + multiple slaves (including across LAN)
- Upload data to HDFS:
```bash
hdfs dfs -put ckd_data.csv /
```
- Load into Spark:
```python
spark.read.csv("hdfs://master:9000/ckd_data.csv", header=True, inferSchema=True)
```

---

## 📸 Screenshots to Include

- ✅ Spark Master Dashboard showing active workers
- ✅ Worker Node UI
- ✅ Jupyter Notebook (running training)
- ✅ Streamlit app with prediction results

(🖼 Add these in your GitHub repo’s README.md with `![img](path)` syntax)

---

## 📚 Reference

- Spark on Docker: [Medium Article](https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b)

---

## 👨‍💻 Author

**Aaditya** — Final Year B.Tech | Big Data • AI • Cloud

> 💬 _This project brings a real-world research paper into practical implementation using Apache Spark, Docker, ML, and Hadoop._

---

## 🔁 Useful Commands

```bash
# Stop the Spark cluster
sudo docker-compose down

# Restart Spark cluster
sudo docker-compose up -d

# Check logs for container
sudo docker logs <container_name>
```

---

