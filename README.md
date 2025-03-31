# 🚀 Volentify
![Volentify](https://github.com/user-attachments/assets/52696936-2fdf-4d0f-9f4b-16f73f3db03c)


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
### 🚫 **Deployment Status**
Currently, the project is not deployed due to the following reasons:
- 🛠️ **Ongoing Development:** The platform is still under active development, with new features and optimizations being added.
- ⚙️ **Infrastructure Setup:** The required cloud infrastructure (such as MongoDB Atlas, AWS, or Heroku) is yet to be configured for production deployment.
- 🔒 **Security and Testing:** Additional security measures and testing are needed before the platform goes live.
- 💰 **Resource Constraints:** Lack of sufficient server resources and funding for stable deployment.

✅ Future plans include deploying the platform on a cloud service for public access.

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
SENDER_EMAIL=<Your Sender Email ID>
SENDER_EMAIL_PASSWORD=<Your Sender Email Password>
OPENCAGE_API=<Your OpenCage API Key>
```
✅ Make sure to add your actual credentials before running the project.

---

### 📷 **Working Prototype**
Here are some images and videos showcasing the working prototype:

#### 🖥️ **Streamlit Dashboard**

*Displays real-time disaster information in an interactive format.*

![volent1](https://github.com/user-attachments/assets/80f06f1d-0d53-4252-8c3b-baaa2ae8cc7f)
![volent2](https://github.com/user-attachments/assets/06d7bf3c-5295-44ab-bd10-0e46991bc773)
![volent3](https://github.com/user-attachments/assets/fff8dec7-da61-4e51-9f35-a439da28ce24)
![volent4](https://github.com/user-attachments/assets/cd027886-4635-4a8d-abcf-f8c12c6c1399)
![volent5](https://github.com/user-attachments/assets/69f40341-7796-46de-a3ce-587d8e42efe4)

---

#### 🎥 **Demo Video**

[▶️ Watch the Platform in Action](https://youtu.be/Jgyuki1mTn4)
- Click the link to see the system in operation.
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


