from app.db.database import engine

if __name__ == "__main__":
    with engine.connect() as conn:
        print("Database connected successfully!")