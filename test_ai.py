# from app.src.v1.lora_trainer_v1.lora_trainer import lora_trainer
from app.src.v1.llm.text_completion import gemma_finetuning
from app.src.v1.schemas.base import GemmaFinetuningRequest


if __name__=="__main__": 
    request_data = {
    "task_id": "123",
    "data_path": "/workspace/parrot-host/train.jsonl",
    "num_train_epochs": 1
    }
    print("training")
    result = gemma_finetuning(
        celery_task_id="123",
        request_data=GemmaFinetuningRequest(**request_data)
    )



