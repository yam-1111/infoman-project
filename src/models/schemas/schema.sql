-- MySQL / MariaDB syntax

-- handle if table already exists
CREATE TABLE IF NOT EXISTS personal_information (
  -- AUTO_INCREMENT for auto-incrementing integer in MySQL/MariaDB
  CSC_ID_No INT AUTO_INCREMENT PRIMARY KEY, 
  Full_Name VARCHAR(30) NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Place_Of_Birth VARCHAR(20),
  Sex CHAR(1) CHECK (Sex IN ('M', 'F')),
  Civil_Status CHAR(2) CHECK (Civil_Status IN ('S', 'M', 'W', 'Se', 'O')),
  Height_m FLOAT,
  Weight_kg FLOAT,
  Blood_Type CHAR(3) CHECK (Blood_Type IN ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+')),
  GSIS_ID_NO CHAR(20),
  PAGIBIG_ID_NO CHAR(14),
  PHILHEALTH_NO CHAR(15),
  SSS_NO CHAR(12),
  TIN_NO CHAR(15),
  Agency_Employee_NO VARCHAR(9),
  Citizenship CHAR(4) CHECK (Citizenship IN ('Fil', 'DC-B', 'DC-N')),
  Residential_Address VARCHAR(100),
  Permanent_Address VARCHAR(100),
  Telephone_NO VARCHAR(12),
  Mobile_NO VARCHAR(10),
  Email_Address VARCHAR(150) UNIQUE NOT NULL,
  Father_Full_Name VARCHAR(50),
  Mother_Full_Name VARCHAR(50),
  Spouse_Full_Name VARCHAR(50),
  Spouse_Occupation VARCHAR(30),
  Spouse_Business_Address VARCHAR(100),
  Spouse_Telephone_Number CHAR(12),
  -- user password
  password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS education (
  Education_ID INT AUTO_INCREMENT PRIMARY KEY,
  CSC_ID_No INT NOT NULL,
  Education_Level VARCHAR(30) CHECK (Education_Level IN ('Elementary', 'Secondary', 'Vocational', 'College', 'Graduate Studies')),
  School_Name VARCHAR(50),
  Education_Degree VARCHAR(50),
  Education_Start DATE,
  Education_End DATE,
  Highest_Level VARCHAR(150),
  Year_Graduated DATE,
  Scholarship_Acad_Honors VARCHAR(20),
  -- prevent duplicate rows
  UNIQUE KEY unique_cols (Education_Level, School_Name, Education_Degree),
  -- enable deletion on child from parent(personal_information)
  FOREIGN KEY (CSC_ID_No) 
    REFERENCES personal_information(CSC_ID_No) 
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS children (
  Children_ID INT AUTO_INCREMENT PRIMARY KEY,
  CSC_ID_No INT NOT NULL,
  Name_of_Children VARCHAR(30),
  Children_Date_of_Birth DATE,
   -- enable deletion on child from parent(personal_information)
  FOREIGN KEY (CSC_ID_No) 
    REFERENCES personal_information(CSC_ID_No) 
    ON DELETE CASCADE
);
