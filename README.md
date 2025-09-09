# GAP: Goal Accountibility Partner

Agentic application that helps with all stages of goal creation and completion.

# General Design

This project is a simple web application that combines a React frontend with a FastAPI backend. There is a PostGreSQL database linked to the backend.

## Project Structure

```
gap_web_client
├── backend
│   ├── app
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   └── __init__.py      # Marks the directory as a Python package
│   ├── requirements.txt      # Lists dependencies for the FastAPI backend
│   └── README.md             # Documentation for the backend
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the React application
│   ├── src
│   │   ├── App.js            # Main React component
│   │   └── index.js          # Entry point for the React application
│   ├── package.json          # Configuration file for npm
│   └── README.md             # Documentation for the frontend
└── README.md                 # Overview of the entire project
```

## Getting Started

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the React application in your web browser at `http://localhost:3000`. The FastAPI backend will be available at `http://localhost:8000`.
