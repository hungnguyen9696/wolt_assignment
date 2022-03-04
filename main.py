from fastapi import FastAPI
from pydantic import BaseModel
from Calculating import calculating

#subclass define the schema or data shape server want to receive
class Fee(BaseModel):
   cart_value: int
   delivery_distance: int
   number_of_items: int
   time: str

app = FastAPI()

@app.get("/")
async def home():
   return {"WoltApp assignment"}

@app.post("/fee")
async def calculate_delivery_fee(fee: Fee):
   try:
      print(fee)
      delivery_fee = calculating(fee)
   except:
      print("something is wrong")
   else:
      return {"delivery_fee": delivery_fee}
