
from fastapi import FastAPI
from uuid import uuid4
from pydantic import BaseModel,Field,field_validator
from typing import Optional
from datetime import datetime

app=FastAPI()
todo_list=[]
class Todo(BaseModel):
    id:str=Field(default_factory=lambda :str(uuid4()))#自动生成唯一id
    title:str = Field(...,min_length=1)
    content:Optional[str]
    deadline:datetime
    status:Optional[str]='未完成'
    @field_validator('status')
    def validate_status(cls,v):
        if v not in ['已完成','未完成']:
            raise ValueError( '状态必须是已完成和未完成')
        return v
@app.post('/todo/')
async def todo(todo:Todo):
    todo_list.append(todo)
    return todo
@app.get('/todos/')
def get_todos(status:Optional[str]=None,todo_id: Optional[str] = None):
    if todo_id:
        for todo in todo_list:
            if todo.id==todo_id:
                return todo
    if status:
        filtered_todo=[todo for todo in todo_list if todo.status==status]
        return filtered_todo

    return todo_list
@app.patch('/todos/{todo_id}/{status}')
def update_todo(todo_id:str,status:str):
    for todo in todo_list:
        if todo.id==todo_id:
            if status not in ['已完成','未完成']:
                return {'error':'状态必须是已完成或未完成'}
            todo.status=status
            return {'message':'状态更新成功','todo':todo}
    return {'error':'待办事务不存在'}
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id:Optional[str]=None):
    for todo in todo_list:
        if todo.id==todo_id:
            todo_list.remove(todo)
            return {'message':'待办事务删除成功','delete_todo':todo}
    return {'error':'事务不存在'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

