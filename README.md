# 🚀 Blood Donation Platform (Django)

## 📌 Overview

This platform is a vital bridge connecting those in urgent need of blood with compassionate donors. It streamlines the blood donation process, enabling quick and efficient blood requests and donor notifications to save lives.

## ✨ Features

*   **Secure User Authentication:** Seamless signup, login, and logout with a custom user model, ensuring a personalized and secure experience for every user.
*   **Comprehensive Donor Registration:** Empower individuals to volunteer as blood donors by easily providing their blood type, contact details, and location, building a robust network of life-savers.
*   **Effortless Blood Request System:** Users can quickly submit blood requests, specifying the required blood type, location, and hospital, facilitating rapid response in critical situations.
*   **Automated Donor Matching & Notifications:** Intelligent system automatically identifies and notifies matching donors for new blood requests, ensuring timely awareness and action.
*   **Interactive Notification Management:** Donors and requesters can view and update the status of blood requests through a dedicated notification dashboard, providing transparency and control.
*   **Integrated Contact & FAQ:** A user-friendly contact form and a comprehensive FAQ section address common queries, enhancing user support and engagement.

## 🛠️ Tech Stack

*   **Backend:** Python (Django)
*   **Database:** SQLite
*   **Frontend:** HTML, CSS, JavaScript (Django Templates)

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/blood-donation.git
    cd blood-donation
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: A `requirements.txt` file is not currently in the repository. You may need to create one by running `pip freeze > requirements.txt` after installing Django and other necessary packages.* 

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## 📂 Project Structure

```
blood-donation/
├── blood_donation/          # Main Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI config for deployment
├── donation/                # Core application for blood donation features
│   ├── models.py            # Database models (CustomUser, Donor, BloodRequest, Notification, FAQ, ContactMessage)
│   ├── views.py             # Business logic and view functions
│   ├── urls.py              # Application-specific URL routing
│   ├── forms.py             # Django forms for user input
│   └── migrations/          # Database schema changes
├── templates/               # HTML templates for rendering pages
│   └── donation/            # Application-specific templates
├── static/                  # Static files (CSS, JS, images)
├── db.sqlite3               # SQLite database file
└── manage.py                # Django's command-line utility
```

## 📈 Future Improvements

*   **Location-Based Matching:** Implement advanced location services to connect requesters with the nearest available donors, significantly reducing response times.
*   **Donor Availability Scheduling:** Allow donors to set their availability and preferred donation times, optimizing the matching process and reducing coordination overhead.
*   **Real-time Chat/Communication:** Integrate a real-time chat feature between requesters and donors to facilitate direct communication and coordination.

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository, make improvements, and submit pull requests.

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.