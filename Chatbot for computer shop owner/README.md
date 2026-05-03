# 👔 Shop Owner Utilities & Data Tools

This directory contains specialized tools and scripts designed for the owner of RK Computers to manage the system's data, perform database maintenance, and analyze business performance.

## 🛠️ Included Tools

### 🗄️ Database Management
- **`newDB.py`**: A comprehensive script for initializing and managing the shop's database. Handles schema creation and initial data seeding.
- **`mergedb.py`**: Utility script for merging or synchronizing data between different database instances.
- **`sammydb.py`**: Supplementary database interface script.

### 📊 Data Analysis
- **`newloader.ipynb`**: A Jupyter Notebook used for processing raw data, loading it into the database, and performing exploratory data analysis (EDA).
- **`production/`**: Contains files or assets ready for deployment or generated reports.

## 🚀 Usage

### Running Python Scripts
Ensure you have the necessary dependencies installed (e.g., `sqlite3`, `pandas`, `mysql-connector-python` if applicable):
```bash
python newDB.py
```

### Using the Jupyter Notebook
1. Install Jupyter: `pip install jupyter`
2. Launch the notebook server: `jupyter notebook`
3. Open `newloader.ipynb` to view and run the data processing pipeline.

## ⚠️ Important Note
These tools are intended for administrative use. Ensure proper backups are made before running scripts that modify the production database.
