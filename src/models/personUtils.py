from datetime import datetime


def replace_null(value):
    return value if value is not None else ""


def personInformation(status, user):
    return {
        "status": status,
        "formData": {
            "agencyemployee": replace_null(user[14]),  # Agency_Employee_NO
            "bloodType": replace_null(user[7]),  # Blood_Type
            "citizenship": replace_null(user[15]),  # Citizenship
            "dateOfBirth": str(user[2]),  # Date_Of_Birth
            "email_address": replace_null(user[20]),  # Email_Address
            "fatherFullName": replace_null(user[19]),  # Father_Full_Name
            "fullName": replace_null(user[1]),  # Full_Name
            "gsis": replace_null(user[8]),  # GSIS_ID_NO
            "height": replace_null(user[5]),  # Height_m
            "mobile_no": replace_null(user[18]),  # Mobile_NO
            "motherFullName": replace_null(user[21]),  # Mother_Full_Name
            "pagibig": replace_null(user[9]),  # PAGIBIG_ID_NO
            "permanent_address": replace_null(user[17]),  # Permanent_Address
            "philhealth": replace_null(user[10]),  # PHILHEALTH_NO
            "placeOfBirth": replace_null(user[3]),  # Place_Of_Birth
            "residential_address": replace_null(user[16]),  # Residential_Address
            "spouseFullName": replace_null(user[22]),  # Spouse_Full_Name
            "spouseOccupation": replace_null(user[23]),  # Spouse_Occupation
            "sss": replace_null(user[11]),  # SSS_NO
            "telephone_no": replace_null(user[18]),  # Telephone_NO
            "tin": replace_null(user[12]),  # TIN_NO
            "weight": replace_null(user[6]),  # Weight_kg
        },
    }


def person_update(data):
    return (
        replace_null(data.get("fullName")),
        replace_null(data.get("dateOfBirth")),
        replace_null(data.get("placeOfBirth")),
        replace_null(data.get("sex")),
        replace_null(data.get("civilStatus")),
        replace_null(data.get("height")),
        replace_null(data.get("weight")),
        replace_null(data.get("bloodType")),
        replace_null(data.get("gsis")),
        replace_null(data.get("pagibig")),
        replace_null(data.get("philhealth")),
        replace_null(data.get("sss")),
        replace_null(data.get("tin")),
        replace_null(data.get("agencyemployee")),
        replace_null(data.get("citizenship")),
        replace_null(data.get("residential_address")),
        replace_null(data.get("permanent_address")),
        replace_null(data.get("telephone_no")),
        replace_null(data.get("mobile_no")),
        replace_null(data.get("email_address")),
        replace_null(data.get("fatherFullName")),
        replace_null(data.get("motherFullName")),
        replace_null(data.get("spouseFullName")),
        replace_null(data.get("spouseOccupation")),
        replace_null(data.get("spouseBusinessAddress")),
        replace_null(data.get("spouseTelephoneNumber")),
        data.get("email_address"),
    )


def fieldToUpdate(data):
    return {
        "Full_Name": data.get("fullName"),
        "Date_Of_Birth": data.get("dateOfBirth"),
        "Place_Of_Birth": data.get("placeOfBirth"),
        "Sex": data.get("sex"),
        "Civil_Status": data.get("civilStatus"),
        "Height_m": data.get("height"),
        "Weight_kg": data.get("weight"),
        "Blood_Type": data.get("bloodType"),
        "GSIS_ID_NO": data.get("gsis"),
        "PAGIBIG_ID_NO": data.get("pagibig"),
        "PHILHEALTH_NO": data.get("philhealth"),
        "SSS_NO": data.get("sss"),
        "TIN_NO": data.get("tin"),
        "Agency_Employee_NO": data.get("agencyemployee"),
        "Citizenship": data.get("citizenship"),
        "Residential_Address": data.get("residential_address"),
        "Permanent_Address": data.get("permanent_address"),
        "Telephone_NO": data.get("telephone_no"),
        "Mobile_NO": data.get("mobile_no"),
        "Father_Full_Name": data.get("fatherFullName"),
        "Mother_Full_Name": data.get("motherFullName"),
        "Spouse_Full_Name": data.get("spouseFullName"),
        "Spouse_Occupation": data.get("spouseOccupation"),
        "Spouse_Business_Address": data.get("spouseBusinessAddress"),
        "Spouse_Telephone_Number": data.get("spouseTelephoneNumber"),
    }
