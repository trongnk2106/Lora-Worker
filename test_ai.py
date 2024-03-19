from app.src.v1.gemma_trainer.gemma_trainer import gemma_traner
from app.src.v1.schemas.base import GemmaTrainerRequest

if __name__=="__main__": 
    request_data = {
    "task_id": "123",
    "data": ["data1", "data2", "data3", "data4", "data5"],
    "num_train_epochs": 1
    }
    print("training")
    result = gemma_traner(
        celery_task_id="123",
        request_data=GemmaTrainerRequest(**request_data)
    )



