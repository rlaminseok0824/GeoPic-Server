from beanie import Document
        
        
class Articles(Document):
    name: str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Example Name",
            }
        }
