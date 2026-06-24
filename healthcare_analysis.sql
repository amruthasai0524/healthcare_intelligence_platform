CREATE DATABASE healthcare_db;
USE healthcare_db;
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    sex INT,
    cp INT,
    trestbps INT,
    chol INT,
    fbs INT,
    restecg INT,
    thalach INT,
    exang INT,
    oldpeak FLOAT,
    slope INT,
    ca INT,
    thal INT,
    target INT
);
SHOW TABLES;
DESC patients;
SELECT CURRENT_USER();
CREATE USER 'amrutha'@'localhost'
IDENTIFIED BY 'Amrutha@123';
GRANT ALL PRIVILEGES
ON healthcare_db.*
TO 'amrutha'@'localhost';
FLUSH PRIVILEGES;

SELECT COUNT(*) FROM patients;
SELECT COUNT(*) FROM patients;
##  disease Disrtribution
SELECT
    target,
    COUNT(*) AS patient_count
FROM patients
GROUP BY target;

# Average Age

SELECT
    AVG(age) AS average_age
FROM patients;

# avaerage cholesterol by disesase Status

SELECT
    target,
    AVG(chol) AS avg_cholesterol
FROM patients
GROUP BY target;

# Average Blood Pressure 
SELECT
    target,
    AVG(trestbps) AS avg_bp
FROM patients
GROUP BY target;


# Gender Distrubution 
SELECT
    sex,
    COUNT(*) AS total_patients
FROM patients
GROUP BY sex;

# disease by Gender 
SELECT
    sex,
    target,
    COUNT(*) AS count
FROM patients
GROUP BY sex, target;

# Top 10 Highest Cholesterol Patients
SELECT *
FROM patients
ORDER BY chol DESC
LIMIT 10;

# High Risk Patients
SELECT *
FROM patients
WHERE chol > 250
AND trestbps > 140;


