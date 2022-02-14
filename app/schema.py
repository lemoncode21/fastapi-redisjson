from redis_om import HashModel
from config import redis_db

class Task(HashModel):
    name: str
    description: str
    
    class Meta: 
        database: redis_db

