# Databricks-Project
End-to-End Databricks Engineering: Auto Loader Ingestion → DLT CDC Processing (Silver) → Metadata-Driven SCD Framework (Gold) → Automated Fact Table Generation → dbt Semantic Models → Power BI Reporting



🚀 I’ve developed an end-to-end Databricks Lakehouse that automates ingestion, processing, dimension and fact data modeling, and analytics reporting.

I set up the foundation using Databricks Auto Loader to incrementally ingest new data and Delta Live Tables (DLT) to clean, standardize, and produce CDC-aware Silver layer datasets. This created a reliable pipeline capable of handling fast-changing data with minimal manual effort. I expanded the architecture by automating how the Gold layer is created and maintained. I implemented automated dimension processing, a dynamic fact table framework, and a DBT transformation layer to ensure the entire analytics flow remains consistent, scalable, and low-maintenance.

The goal is to manage fast-changing, multi-source data and transform it into clean, consistent, continuously updated Silver-layer datasets without manual effort or pipeline disruptions, while evolving the Gold layer into a fully metadata-driven architecture where dimension and fact tables can be generated or updated simply by adjusting parameters—without writing new SQL or creating new pipelines.

📥 **For the ingestion layer,**  I built a parameterized incremental ingestion framework using Databricks Auto Loader. It automatically detects new files, handles schema drift, ensures idempotent behavior, and prevents duplicates—creating a Bronze layer that is stable, scalable, and low-maintenance.

🔗 Full workflow: https://medium.com/@sakibul1605/how-i-built-a-parameterized-incremental-ingestion-framework-in-databricks-using-auto-loader-b54a62d9e6d0

⚙️ **For the transformation layer** , I used Delta Live Tables (DLT) to enforce data quality, manage schema consistency, and automatically handle CDC/SCD logic—without writing complex merge statements. This keeps the Silver layer accurate, up-to-date, and analytics-ready with significantly reduced maintenance overhead.

🔗 Silver layer write-up: https://medium.com/@sakibul1605/building-the-silver-layer-with-delta-live-tables-challenges-solutions-step-by-step-fa33b07f750c

⚙️ **Dynamic Framework for Dimension Tables (Gold Layer):**  Since manually updating each dimension table with separate SCD logic was repetitive and difficult to maintain, I built a metadata-driven framework that manages all dimension updates through a single process. It automatically detects changes using CDC fields, assigns surrogate keys, and applies reliable Delta MERGE updates, making the dimension layer more consistent, automated, and scalable.

Detailed workflow: https://medium.com/@sakibul1605/building-a-dynamic-scd-framework-in-databricks-a-parameter-driven-approach-for-scalable-a947b8ffcdfd

⚙️ **Automated Fact Table Framework :**  I implemented a fully parameter-driven fact framework that removes the need to manually write complex SQL for each new table. It generates the required dimension joins, performs surrogate key lookups, and applies incremental CDC logic to load only new or updated data.

Detailed workflow: https://medium.com/@sakibul1605/building-an-automated-fact-table-framework-in-databricks-95068e1ce489

⚙️ **DBT Transformation Layer:**  I added a dedicated analytics layer using dbt, transforming the refined Gold tables into reliable business models for trend analysis, operational insights, and growth reporting. These dbt models are stored in the Databricks SQL Warehouse and connected directly to Power BI for interactive, consistent dashboards.

Detailed workflow: https://medium.com/@sakibul1605/how-i-used-dbt-data-build-tool-to-build-a-business-friendly-analytics-layer-on-top-of-databricks-e3348cf8295f


**🖥️ Architecture Summary Diagram**

            ┌────────────────────────┐
            │   External Sources      │
            │  (API, CSV, Parquet)    │
            └──────────┬─────────────┘
                       │
           1. Auto Loader (Bronze)
                       │
            ┌──────────▼─────────────┐
            │      Bronze Layer       │
            └──────────┬─────────────┘
                       │
           2. CDC + Standardization
                       │
            ┌──────────▼─────────────┐
            │       Silver Layer      │
            └──────────┬─────────────┘
                       │
              3. SCD Automation
                       │
            ┌──────────▼─────────────┐
            │    Gold Dimensions      │
            └──────────┬─────────────┘
                       │
              4. Fact Modeling
                       │
            ┌──────────▼─────────────┐
            │      Gold Facts         │
            └──────────┬─────────────┘
                       │
                 5. dbt Layer
                       │
            ┌──────────▼─────────────┐
            │ Business KPI Models     │
            └──────────┬─────────────┘
                       │
                 6. Power BI
                       │
            ┌──────────▼─────────────┐
            │ Executive Dashboards    │
            └────────────────────────┘


**Final Outcome :**  A fully automated architecture where Auto Loader ingests raw data, DLT standardizes it in Silver, metadata-driven frameworks generate Gold dimensions and facts, and dbt delivers analytics-ready models for BI. The entire flow is now consistent, low-maintenance, and scalable for future data growth.
