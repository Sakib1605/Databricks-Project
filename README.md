# Databricks-Project
End-to-End Databricks Engineering: Auto Loader Ingestion → DLT Silver → Dynamic SCD Gold Layer



🚀 I’ve been working on a Databricks project focused on building a reliable and scalable data pipeline—from ingestion to transformation. The main goal is to handle fast-changing, multi-source data and convert it into clean, consistent, continuously updated datasets without manual intervention or pipeline disruptions.

📥 For the ingestion layer, I built a parameterized incremental ingestion framework using Databricks Auto Loader. It automatically detects new files, handles schema drift, ensures idempotent behavior, and prevents duplicates—creating a Bronze layer that is stable, scalable, and low-maintenance.
🔗 Full workflow: https://medium.com/@sakibul1605/how-i-built-a-parameterized-incremental-ingestion-framework-in-databricks-using-auto-loader-b54a62d9e6d0

⚙️ For the transformation layer, I used Delta Live Tables (DLT) to enforce data quality, manage schema consistency, and automatically handle CDC/SCD logic—without writing complex merge statements. This keeps the Silver layer accurate, up-to-date, and analytics-ready with significantly reduced maintenance overhead.
🔗 Silver layer write-up: https://medium.com/@sakibul1605/building-the-silver-layer-with-delta-live-tables-challenges-solutions-step-by-step-fa33b07f750c

🔶 Now, my next step is building a dynamic, fully automated Slowly Changing Dimension (SCD) framework in the Gold layer. The goal is to create a parameter-driven system that updates any dimension table using key & CDC columns—without rewriting pipelines.

📌 I’ll continue sharing updates as I build this out
