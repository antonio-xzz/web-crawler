# Web Crawler Project

## Overview

This project is a **web crawler** built using **FastAPI** for the backend and **React** (TypeScript) for the frontend. The crawler performs web scraping to extract data from target websites, processes it in the backend, and presents the information in a user-friendly interface on the frontend.

## Project Structure

- **Backend**: Python with FastAPI, responsible for handling web scraping requests and processing the scraped data.
- **Frontend**: TypeScript with React, provides the user interface to input URLs, control the crawling process, and view the results.

## Features

- **Web Scraping**: Scrape content from target websites.
- **Data Processing**: Extract and clean specific data like text, images, or links.
- **User Interface**: Simple and responsive UI for controlling the crawler and displaying results.
- **API Integration**: Seamless communication between the frontend and backend via API endpoints.

## Technologies Used

### Backend
- **Python 3.12**
- **FastAPI**: For building the backend API.
- **Uvicorn**: For serving the FastAPI app.
- **Poetry**: For dependency management and environment setup.
- **BeautifulSoup & Requests**: For web scraping (or alternative scraping libraries).
- **Pyenv**: To manage Python versions.

### Frontend
- **React** (with TypeScript): For building the user interface.
- **SCSS**: For styling.
- **Axios**: For making HTTP requests to the backend API.

## Installation and Setup

### Prerequisites

- **Python 3.12** (Managed via `pyenv`)
- **Node.js** (Ensure the latest stable version is installed)
- **Poetry** (For Python dependency management)
- **FastAPI**, **Uvicorn**, **BeautifulSoup**, **Requests** (Handled by Poetry)
- **React** (TypeScript)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/antonio-xzz/web-crawler.git
   cd web-crawler
   ```

2. Install Python and backend dependencies:
   ```bash
   make install-pyenv-zsh  # or use make install-pyenv-bash if using bash shell
   make install-requirements
   ```

3. Run the FastAPI server:
  ```bash
   make run
   ```

### Frontend set up

1. Navigate to the frontend folder
  ```bash
   cd frontend 
  ```

2. Install dependencies:
  ```bash
    cd frontend 
  ```

3. Start the React development server:
```bash
    npm start
  ```

# Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── main.py       # FastAPI entry point
│   │   ├── routers/      # API routes
│   │   ├── services/     # Web scraping logic
│   │   └── tests/        # Unit tests

├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   └── App.tsx       # Main React entry point
│   └── package.json      # Frontend dependencies
└── README.md             # Project readme
```

## Get .env
cp .env-example .env
