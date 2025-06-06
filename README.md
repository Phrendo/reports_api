# EM Reports API

## Environment Variables
- `DATABASE_URL`: ODBC connection string for SQL Server (e.g., `DRIVER={ODBC Driver 17 for SQL Server};SERVER=...;DATABASE=...;UID=...;PWD=...`)
- `CORS_ORIGINS`: Comma-separated list of allowed CORS origins

## Running Locally
1. Create a `.env` file in the project root with `DATABASE_URL` and `CORS_ORIGINS`.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the API:
   ```
   uvicorn app.main:app --reload
   ```

