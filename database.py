from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL (relative path)
SQLALCHEMY_DATABASE_URL: str = "sqlite:///./clinic.db"

# Create the SQLAlchemy engine with SQLite-specific connection args
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed only for SQLite
)

# Create a session factory for database interactions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Base class for ORM models
Base = declarative_base()
