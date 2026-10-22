cat > akwa_cloud.py << 'PY'
import asyncio, json, websockets
TOKEN="pat_687fc6b463411f55d804b5f61ae6046956dabdde85792b07cf3472ece9775832"
async def main():
    async with websockets.connect("wss://ws.derivws.com/websockets/v3?app_id=1089", additional_headers={"Origin":"https://app.deriv.com"}) as ws:
        await ws.send(json.dumps({"authorize": TOKEN}))
        print(await ws.recv())
        await ws.send(json.dumps({"balance":1}))
        print(await ws.recv())
        await ws.send(json.dumps({"ticks":"R_75","subscribe":1}))
        print("AKWA LIVE CLOUD - Demo $1 TP 10 SL 5")
        for i in range(5):
            d=json.loads(await ws.recv())
            if "tick" in d:
                print(f"V75: {d['tick']['quote']}")
asyncio.run(main())
PY
