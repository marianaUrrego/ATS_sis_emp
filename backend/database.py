from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# para instalar sqlalchemy :          pip install sqlalchemy
# o si de esta manera no funciona: python -m pip install sqlalchemy

#esquema core
metadata = MetaData(schema='core')

# Crear el engine
engine = create_engine(DATABASE_URL)

# Crear el SessionLocal para usarlo en los repositorios y servicios
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base(metadata=metadata)
