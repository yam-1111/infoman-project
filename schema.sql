-- postgres syntax

-- handle if table already exist
CREATE TABLE IF NOT EXISTS personal_information;
CREATE TABLE IF NOT EXISTS children;
CREATE TABLE IF NOT EXISTS education;

-- Create table personal_information
CREATE TABLE personal_information (
  CSC_ID_No SERIAL PRIMARY KEY, -- SERIAL for auto-incrementing integer in PostgreSQL
  Full_Name VARCHAR(30) NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Place_Of_Birth VARCHAR(20) NOT NULL,
  Sex CHAR(1) CHECK (Sex IN ('M', 'F')),
  Civil_Status CHAR(2) CHECK (Civil_Status IN ('S', 'M', 'W', 'Se', 'O')),
  Height_m FLOAT NOT NULL,
  Weight_kg FLOAT NOT NULL,
  Blood_Type CHAR(3) CHECK (Blood_Type IN ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+')),
  GSIS_ID_NO CHAR(20) NOT NULL,
  PAGIBIG_ID_NO CHAR(14) NOT NULL,
  PHILHEALTH_NO CHAR(15) NOT NULL,
  SSS_NO CHAR(12) NOT NULL,
  TIN_NO CHAR(15) NOT NULL,
  Agency_Employee_NO VARCHAR(9) NOT NULL,
  Citizenship CHAR(4) CHECK (Citizenship IN ('Fil', 'DC-B', 'DC-N')),
  Residential_Address VARCHAR(100) NOT NULL,
  Permanent_Address VARCHAR(100) NOT NULL,
  Telephone_NO VARCHAR(12),
  Mobile_NO VARCHAR(10),
  Email_Address VARCHAR(20) NOT NULL,
  Father_Full_Name VARCHAR(50) NOT NULL,
  Mother_Full_Name VARCHAR(50) NOT NULL,
  Spouse_Full_Name VARCHAR(50),
  Spouse_Occupation VARCHAR(30),
  Spouse_Business_Address VARCHAR(100),
  Spouse_Telephone_Number CHAR(12)
);

-- Create table education
CREATE TABLE education (
  Education_ID SERIAL PRIMARY KEY,
  CSC_ID_No INTEGER NOT NULL,
  Education_Level VARCHAR(30) CHECK (Education_Level IN ('Elementary', 'Secondary', 'Vocational', 'College', 'Graduate Studies')),
  School_Name VARCHAR(50) NOT NULL,
  Education_Degree VARCHAR(50) NOT NULL,
  Education_Start DATE NOT NULL,
  Education_End DATE,
  Highest_Level VARCHAR(150) NOT NULL,
  Year_Graduated DATE,
  Scholarship_Acad_Honors VARCHAR(20),
  FOREIGN KEY (CSC_ID_No) REFERENCES personal_information(CSC_ID_No)
);

-- Create table children
CREATE TABLE children (
  Children_ID SERIAL PRIMARY KEY,
  CSC_ID_No INTEGER NOT NULL,
  Name_of_Children VARCHAR(30),
  Children_Date_of_Birth DATE,
  FOREIGN KEY (CSC_ID_No) REFERENCES personal_information(CSC_ID_No)
);
-