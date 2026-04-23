
**Project Overview**

The pipeline performs the following steps:

- Connects to a MySQL server

- Extracts data from Rfam tables (family, full_region)

- Transforms data into a csv file 

- Loads data into Domo using PyDomo

- Supports dataset creation and updates

Note: During dataset updates, the existing data is fully replaced by default.

**Setup Instructions**

1. Clone the Repository

   `git clone https://github.com/s-hreyah/domo-etl`

    `cd domo_etl`
    
2. Install Dependencies

    Make sure you have Python installed, then run:

   `pip install -r requirements.txt` 

3. Configure Environment Variables
   
  - You will find a file named env.example.py
  
  - Create a new file named env.py
  
  - Copy the contents of env.example.py into env.py
  
  - Add your credentials (MySQL and Domo API details)

**How It Works**
1. Data Extraction
   
     a. Connects to MySQL database
   
     b. Fetches data from:

    -family
   
    -full_region
2. Data Loading (Domo)
   
    Uses PyDomo to: Create datasets and Upload data
   
3. Dataset Behavior
   
    Initial Creation:
   
    - Data is uploaded to Domo when the dataset is first created
   
    - Update Operation (Default)
   
    - Existing dataset data is fully replaced

4. Public Test Database

This project uses a public MySQL database for testing purposes.

Documentation Link:  [https://docs.rfam.org/en/latest/database.html]


   
**Incremental Updates (Optional)**

- By default, updates overwrite the dataset.If you want to switch to incremental loading:

- Modify the update function: Change the method from Replace to Append

- This will allow new data to be added instead of replacing the entire dataset.


