import httpx
from fastapi import FastAPI, Request

TOKEN = "7099779832:AAEUyjQElb6J2ocRtXsTJi68dbHPbiEv0pE"
CHAT_ID = "748689055"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
client = httpx.AsyncClient()

app = FastAPI()


@app.post("/post_phone")
async def webhook(req: Request):
    data = await req.json()
    print(data)
    text = data['name']
    text += " - "
    text += data['phone']
    await client.post(f"{BASE_URL}/sendMessage?chat_id={CHAT_ID}&text={text}",
                      headers={'Content-Type': 'application/json'})
    return data
