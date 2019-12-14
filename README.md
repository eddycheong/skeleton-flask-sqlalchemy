# skeleton-flask-sqlalchemy

## Creating Migrations Files
1. Add the new model under models
2. Update the __init__.py under models to include your new model
3. Run the following command: `alembic revision -m "Create table x" --autogenerate`
4. Cleanup the migration file

## Running Migrations
`alembic upgrade head`

## Running Seed Files
Although alembic is great for handling migrations of DDL, it unfortunately does not have an convenient way seeding initial files. This is my initial work around of seeding files.
  
`python seeder.py`

## Running API Service
`python server.py`
