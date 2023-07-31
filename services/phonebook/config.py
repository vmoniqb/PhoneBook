import os

# Define contact DB variables
DATABASE_NAME = os.getenv('DATABASE_NAME', 'contacts')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'B1u3par58')

# Define DB URL
DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
