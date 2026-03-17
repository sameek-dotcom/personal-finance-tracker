# 💰 Personal Finance Tracker

A full-stack **Personal Finance Tracker** web application that helps users track expenses, analyze spending habits, and manage their finances efficiently.

---

## 🚀 Features

### 🔐 Authentication

* User Signup & Login (with validation)
* Local storage-based authentication (frontend)
* Flow:
  `Signup → Login → Dashboard`

---

### 📊 Dashboard

* Total expense summary
* Smart insights:

  * 📌 Highest spending category
  * 📌 % spending analysis
  * 📌 Highest spending day
* Charts:

  * Pie Chart (category distribution)
  * Bar Chart (category comparison)
  * Line Chart (trend)

---

### 💸 Expense Management

* Add expenses (amount, category, description, date)
* View all transactions in table format

---

### 📄 Reports

* Generate **professional PDF reports**
* Includes:

  * Structured table
  * Total expense
  * Smart insight

---

### 🎨 UI Features

* Sidebar navigation
* Navbar with dark mode 🌙
* Gradient homepage
* Clean dashboard UI

---

## 🛠️ Tech Stack

### Frontend

* React.js
* React Router
* Axios
* Chart.js
* jsPDF

### Backend

* FastAPI (Python)
* PostgreSQL

---

# ⚙️ HOW TO RUN THIS PROJECT (STEP-BY-STEP)

---

## 🔹 1. Clone Repository

```bash
git clone https://github.com/sameek-dotcom/finance-tracker.git
cd finance-tracker
```

---

## 🔹 2. Setup Backend (FastAPI)

### Step 1: Go to backend folder

```bash
cd backend
```

### Step 2: Create virtual environment

```bash
python -m venv venv
```

### Step 3: Activate environment

👉 Windows:

```bash
venv\Scripts\activate
```
### Step 4: Install dependencies

```bash
pip install fastapi uvicorn psycopg2
```

### Step 5: Run backend server

```bash
uvicorn main:app --reload
```

👉 Backend runs on:

```
http://127.0.0.1:8000
```

---

## 🔹 3. Setup PostgreSQL Database

### Step 1: Open pgAdmin / psql

### Step 2: Create database

```sql
CREATE DATABASE finance_db;
```

### Step 3: Connect to database

```sql
\c finance_db;
```

### Step 4: Create table

```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    category TEXT,
    description TEXT,
    transaction_date DATE
);
```

---

## 🔹 4. Setup Frontend (React)

### Step 1: Go to frontend folder

```bash
cd ../frontend
```

### Step 2: Install dependencies

```bash
npm install
```

### Step 3: Install required libraries

```bash
npm install axios react-router-dom chart.js react-chartjs-2 jspdf jspdf-autotable react-icons
```

### Step 4: Run React app

```bash
npm start
```

👉 Frontend runs on:

```
http://localhost:3000
```

---

# 🔄 HOW TO USE

1. Open browser → `http://localhost:3000`
2. Go to **Signup page**
3. Create account
4. Login using same credentials
5. Access dashboard
6. Add expenses
7. View charts & insights
8. Generate PDF report

---



# 📁 Project Structure

```
finance-tracker/
│
├── frontend/
├── backend/
├── README.md
```

# 💰 Personal Finance Tracker

A full-stack **Personal Finance Tracker** web application that helps users track expenses, analyze spending habits, and manage their finances efficiently.

---

## 🚀 Features

### 🔐 Authentication

* User Signup & Login (with validation)
* Local storage-based authentication (frontend)
* Flow:
  `Signup → Login → Dashboard`

---

### 📊 Dashboard

* Total expense summary
* Smart insights:

  * 📌 Highest spending category
  * 📌 % spending analysis
  * 📌 Highest spending day
* Charts:

  * Pie Chart (category distribution)
  * Bar Chart (category comparison)
  * Line Chart (trend)

---

### 💸 Expense Management

* Add expenses (amount, category, description, date)
* View all transactions in table format

---

### 📄 Reports

* Generate **professional PDF reports**
* Includes:

  * Structured table
  * Total expense
  * Smart insight

---

### 🎨 UI Features

* Sidebar navigation
* Navbar with dark mode 🌙
* Gradient homepage
* Clean dashboard UI

---

## 🛠️ Tech Stack

### Frontend

* React.js
* React Router
* Axios
* Chart.js
* jsPDF

### Backend

* FastAPI (Python)
* PostgreSQL

---

# ⚙️ HOW TO RUN THIS PROJECT (STEP-BY-STEP)

---

## 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/finance-tracker.git
cd finance-tracker
```

---

## 🔹 2. Setup Backend (FastAPI)

### Step 1: Go to backend folder

```bash
cd backend
```

### Step 2: Create virtual environment

```bash
python -m venv venv
```

### Step 3: Activate environment

👉 Windows:

```bash
venv\Scripts\activate
```

👉 Mac/Linux:

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install fastapi uvicorn psycopg2
```

### Step 5: Run backend server

```bash
uvicorn main:app --reload
```

👉 Backend runs on:

```
http://127.0.0.1:8000
```

---

## 🔹 3. Setup PostgreSQL Database

### Step 1: Open pgAdmin / psql

### Step 2: Create database

```sql
CREATE DATABASE finance_db;
```

### Step 3: Connect to database

```sql
\c finance_db;
```

### Step 4: Create table

```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    category TEXT,
    description TEXT,
    transaction_date DATE
);
```

---

## 🔹 4. Setup Frontend (React)

### Step 1: Go to frontend folder

```bash
cd ../frontend
```

### Step 2: Install dependencies

```bash
npm install
```

### Step 3: Install required libraries

```bash
npm install axios react-router-dom chart.js react-chartjs-2 jspdf jspdf-autotable react-icons
```

### Step 4: Run React app

```bash
npm start
```

👉 Frontend runs on:

```
http://localhost:3000
```

---

# 🔄 HOW TO USE

1. Open browser → `http://localhost:3000`
2. Go to **Signup page**
3. Create account
4. Login using same credentials
5. Access dashboard
6. Add expenses
7. View charts & insights
8. Generate PDF report

---

# ⚠️ COMMON ERRORS & FIXES

### ❌ "react-scripts not found"

```bash
npm install
```

---

### ❌ Backend not connecting

* Check FastAPI is running
* Check URL: `http://127.0.0.1:8000`

---

### ❌ "relation transactions does not exist"

* Run SQL table creation query again

---

### ❌ CORS error

Add in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

# 📁 Project Structure

```
finance-tracker/
│
├── frontend/
├── backend/
├── README.md
```

---

# 🎯 Future Improvements

* 🔐 JWT authentication
* 👤 Multi-user support
* 📱 Mobile responsive UI
* 📊 Advanced analytics

---

# 👨‍💻 Author

**Sameeksha Kotian**

---

⭐ If you like this project, give it a star!

