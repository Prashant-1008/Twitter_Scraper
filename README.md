
# Twitter Trends Scraper

A Python-based web application to scrape and display trending Twitter topics using Selenium, Flask, and MongoDB.
(ProxyMesh's Free version is creating errors. So it is excluded)

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [MongoDB Integration](#mongodb-integration)
- [Frontend Overview](#frontend-overview)
- [Credits](#credits)

---
## Demo 

- Initial Phase : 

![Twitter-Trends-Scraper-12-27-2024_07_08_PM](https://github.com/user-attachments/assets/3aa7553c-c053-4cd2-aac4-204750ac405a)

---

https://github.com/user-attachments/assets/558b4dfd-9168-4bbb-a763-3e30df483939

---

- Current Version :

![Twitter-Trends-Scraper-12-28-2024_03_15_PM](https://github.com/user-attachments/assets/b581cc81-9ca4-43f5-91be-1ee6f22512c3)

---

https://github.com/user-attachments/assets/6fe199f7-dccf-488c-8a54-f23b2dc6e1b7

---

## Features

- Automates login to Twitter and scrapes the top trending topics.
- Supports user authentication, including handling verification codes.
- Saves trends data in MongoDB.
- Displays scraped data dynamically in a user-friendly frontend.
- Retrieves client IP information during each scrape request.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: MongoDB
- **Automation**: Selenium with ChromeDriver

---

## Folder Structure

```plaintext
SCRAPER-MAIN/
├── scraper/
│   ├── templates/
│   │   └── index.html      # Frontend template
│   ├── venv/               # Virtual environment
│   ├── scraper.py          # Scraping logic
│   ├── app.py              # Flask application
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── test.py                 # Test script
```

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prashant-1008/Twitter_Scraper.git
   cd Twitter_Scraper
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install ChromeDriver:
   - Ensure the ChromeDriver version matches your installed Chrome browser version.
   - Add ChromeDriver to your system PATH.

5. Set up MongoDB:
   - Start your MongoDB server.
   - Replace the `MONGODB_URI` in `Config` with your MongoDB connection string.

---

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open the browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Click the **"Run Script"** button to scrape the latest Twitter trends.

4. View trends and MongoDB records dynamically.

---

## Configuration

The project uses a `Config` class for sensitive credentials and configurations:

- `TWITTER_USERNAME`: Your Twitter username or email.
- `TWITTER_PASSWORD`: Your Twitter password.
- `MONGODB_URI`: MongoDB connection string.

Make sure to securely store credentials in the `Config` class.

---

## MongoDB Integration

The project saves scraped trends to a MongoDB collection:

- **Database**: `twitter_trends`
- **Collection**: `trends`

Each record includes:
- A unique `_id`.
- Timestamp of the scrape.
- Trends data (rank, name, posts count).

---

## Frontend Overview

The `index.html` file displays trends with a clean UI:

- Click the **Run Script** button to fetch trends.
- See the most recent trends, timestamp, and MongoDB record.
- Responsive design for desktop and mobile.

---

## Credits

Developed by **Prashant-1008** as a project to explore automation and web scraping techniques.
```

Feel free to customize the README further to suit your project’s style or structure!
