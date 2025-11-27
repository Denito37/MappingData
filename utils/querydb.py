from etl.load.load import engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import text

Session = sessionmaker(bind=engine)
session = Session()


def query_db_all(table_model):
    """Query all records from a table.
    
    Args:
        table_model: SQLAlchemy model class for the table
        
    Returns:
        List of all records from the table
    """
    data = session.query(table_model).all()  # Fixed: added parentheses
    return data


def query_db_filtered(table_model, column_name, filter_value):
    """Query records from a table filtered by a column value.
    
    Args:
        table_model: SQLAlchemy model class for the table
        column_name: String name of the column to filter on
        filter_value: Value to filter by
        
    Returns:
        List of filtered records
    """
    # Fixed: Use getattr to dynamically access the column
    column = getattr(table_model, column_name)
    data = session.query(table_model).filter(column == filter_value).all()
    return data


def query_db_by_borough(table_model, borough):
    """Convenience function to filter by borough.
    
    Args:
        table_model: SQLAlchemy model class (Fountains or Trees)
        borough: Borough name to filter by
        
    Returns:
        List of records in the specified borough
    """
    return query_db_filtered(table_model, 'borough', borough)


def query_db_by_status(table_model, status):
    """Convenience function to filter by status.
    
    Args:
        table_model: SQLAlchemy model class (Fountains or Trees)
        status: Status value to filter by
        
    Returns:
        List of records with the specified status
    """
    return query_db_filtered(table_model, 'status', status)


def close_session():
    """Close the database session."""
    session.close()