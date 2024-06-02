DROP TABLE IF EXISTS 'personal_information';
DROP TABLE IF EXISTS 'children';
DROP TABLE IF EXISTS 'education';

CREATE TABLE personal_information (
  CSC_ID_No INTEGER PRIMARY KEY AUTOINCREMENT,
  Full_Name VARCHAR(30) NOT NULL, -- Full name of the person
  Date_Of_Birth DATE NOT NULL, -- Person's date of birth
  Place_Of_Birth VARCHAR(20) NOT NULL, -- Place where the person was born
  Sex CHAR(1) CHECK (Sex IN ('M', 'F')), -- Gender (M or F)
  Civil_Status CHAR(2) CHECK (Civil_Status IN ('S', 'M', 'W', 'Se', 'O')), -- Marital Status (Single, Married, Widowed, Separated, Others)
  Height_m FLOAT NOT NULL, -- Height in meters with two decimal places
  Weight_kg FLOAT NOT NULL, -- Weight in kilograms with two decimal places
  Blood_Type CHAR(3) CHECK (Blood_Type IN ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+')), -- Blood type
  GSIS_ID_NO CHAR(20) NOT NULL, -- GSIS ID Number
  PAGIBIG_ID_NO CHAR(14) NOT NULL, -- Pag-IBIG ID Number
  PHILHEALTH_NO CHAR(15) NOT NULL, -- PhilHealth ID Number
  SSS_NO CHAR(12) NOT NULL, -- SSS ID Number
  TIN_NO CHAR(15) NOT NULL, -- Tax Identification Number
  Agency_Employee_NO VARCHAR(9) NOT NULL, -- Employee Number within the Agency
  Citizenship CHAR(4) CHECK (Citizenship IN ('Fil', 'DC-B', 'DC-N')), -- Citizenship (Filipino, Dual Citizen by Birth, Dual Citizen by Naturalization)
  Residential_Address VARCHAR(100) NOT NULL, -- Address of residence
  Permanent_Address VARCHAR(100) NOT NULL, -- Permanent address
  Telephone_NO VARCHAR(12), -- Telephone Number (Optional)
  Mobile_NO VARCHAR(10), -- Mobile Number (Optional)
  Email_Address VARCHAR(20) NOT NULL, -- Email address
  Father_Full_Name VARCHAR(50) NOT NULL, -- Father's full name
  Mother_Full_Name VARCHAR(50) NOT NULL, -- Mother's full name
  Spouse_Full_Name VARCHAR(50), -- Spouse's full name (Optional)
  Spouse_Occupation VARCHAR(30), -- Spouse's occupation (Optional)
  Spouse_Business_Address VARCHAR(100), -- Spouse's business address (Optional)
  Spouse_Telephone_Number CHAR(12) -- Spouse's telephone number (Optional)
);


CREATE TABLE education (
  Education_ID INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for education record (auto-increments) 
  CSC_ID_No INTEGER NOT NULL, -- Foreign Key referencing CS_ID_No in personal_information table
  Education_Level CHAR(30) CHECK (Education_Level IN ('Elementary', 'Secondary', 'Vocational', 'College', 'Graduate Studies')), -- Level of education
  School_Name VARCHAR(50) NOT NULL, -- Name of the school
  Education_Degree VARCHAR(50) NOT NULL, -- Degree or program obtained (if applicable)
  Education_Start DATE NOT NULL, -- Start date of the education program
  Education_End DATE, -- End date of the education program (may be null)
  Highest_Level VARCHAR(150) NOT NULL, -- Highest educational level attained so far
  Year_Graduated DATE, -- Year of graduation (may be null)
  Scholarship_Acad_Honors VARCHAR(20), -- Scholarships or academic honors received (Optional)
   FOREIGN KEY (CSC_ID_No) REFERENCES personal_information(CS_ID_No) -- Enforces relationship with personal_information
);

CREATE TABLE children (
  Children_ID INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for child record (auto-increments)
  CSC_ID_No INTEGER NOT NULL, -- Foreign Key referencing CS_ID_No in personal_information table
  Name_of_Children VARCHAR(30), -- Child's name (Optional)
  Children_Date_of_Birth DATE, -- Child's date of birth (Optional)
    FOREIGN KEY (CSC_ID_No) REFERENCES personal_information(CS_ID_No) -- Enforces relationship with personal_information
);


