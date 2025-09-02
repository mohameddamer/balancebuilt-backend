from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers import master, transactions, finance, upload
app = FastAPI(title='BalanceBuilt API')
@app.on_event('startup')
def startup():
    init_db()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
@app.get('/')
def root(): return {'status':'ok'}
app.include_router(master.router, prefix='/master', tags=['master'])
app.include_router(transactions.router, prefix='/transactions', tags=['transactions'])
app.include_router(finance.router, prefix='/finance', tags=['finance'])
app.include_router(upload.router, prefix='/upload', tags=['upload'])
