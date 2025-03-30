# 🚀 Volentify

**Volentify** is a real-time disaster information aggregation platform that collects, categorizes, and displays disaster-related data from verified news portal. It offers a user-friendly dashboard to help disaster response agencies, and it's registered users make informed decisions quickly.

---

## 📌 **Features**
- 🌐 **Real-time Data Collection:** Aggregates disaster-related information from verified News Resource(Google News).
- 🔍 **Intelligent Categorization:** Uses NLP models to filter and classify disaster types.
- 📊 **Interactive Dashboard:** Displays the data on a visually appealing Streamlit dashboard.
- ⚙️ **FastAPI Backend:** Manages data processing and user authentication.
- 💡 **User Notifications:** Email alerts for disasters in your proximity.

---

## ⚙️ **Tech Stack**
- **Backend:** FastAPI, Python
- **Frontend:** Streamlit
- **Database:** MongoDB
- **APIs:** Google News API

---

## 🚀 **Getting Started**

### ✅ **Prerequisites**
Make sure you have the following installed:
- Python 3.9+
- MongoDB (running locally or a remote instance)
- Pip for Python package management

---

### 🔧 **Installation**
1. **Clone the repository**
```bash
git clone https://github.com/thehimanshubansal/Volentify.git
cd Volentify
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate        # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

### 🚦 **Running the Application**

#### 1️⃣ **Start the FastAPI Backend**
Open a terminal and run the FastAPI server:
```bash
uvicorn app:app --reload
```
- The backend will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

#### 2️⃣ **Run the Streamlit Dashboard**
In a separate terminal, start the Streamlit frontend:
```bash
streamlit run main.py
```
- The dashboard will be available at: [http://localhost:8501](http://localhost:8501)

---

### 🔥 **Environment Variables**
Create a `.env` file in the root directory with the following variables:
```plaintext
MONGO_URI=<Your MongoDB Connection String>
```
**📷 Working Prototype**
Here are some images and videos showcasing the working prototype:

Streamlit dashboard displaying real-time disaster information.
---

▶️ Demo Video
Watch the platform in action.
---

### ⚒️ **Folder Structure**
```
/Volentify
 ├── .env                  # Environment variables
 ├── about.py              # About page logic
 ├── alert.py              # Alert management
 ├── app.py                # FastAPI backend
 ├── db.py                 # MongoDB connection logic
 ├── ggnews_dms4.py        # News aggregation script
 ├── login.py              # User login logic
 ├── main.py               # Streamlit frontend
 ├── models.py             # Data models and schemas
 ├── precaution.py         # Precautionary measures logic
 ├── requirements.txt      # Python dependencies
 ├── send_emails.py        # Email notification logic
 ├── signup.py             # User signup logic
 ├── README.md             # Documentation
 ├── /images               # Screenshots and prototype images
 └── /videos               # Demo videos
```

---

### 🛠️ **Contributing**
Contributions are welcome! If you'd like to improve the project:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

### 📄 **License**
This project is licensed under the [MIT License](LICENSE).

---

### 🛡️ **Authors**

- **Gyanvir Singh** - [GitHub](https://github.com/Gyanvir)
- **Himanshu Bansal** - [GitHub](https://github.com/thehimanshubansal)
- **Rajveer Rangile** - [GitHub](https://github.com/therareonegit)

- **Contributors Welcome!**


