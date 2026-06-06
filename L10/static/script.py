from js import document, Chart 
from pyodide.http import pyfetch
from pyodide.ffi import create_proxy,to_js
import asyncio

#Data
temps = []
labels = []

#Chart 
canvas = document.getElementById("chart")
ctx = canvas.getContext("2d") 
chart_config = {
    "type":"line",
    "data": {
        "labels":labels,
        "datasets":[
            {
                "label":"Temperature",
                "data":temps,
                "borderWidth":2,
                "tension":0.3,
            }
        ]
    },
    "options" : 
    {
        "responsive" : True,
        "animations":
        {
            "y" : 
            {
                "beginAtZero": True
            }
        }
    }
}

chart = Chart.new(ctx, to_js(chart_config))

#Fetch sensor data
async def get_sensor():
    response = await pyfetch("/sensor", method="GET")

    data = await response.json()

    temp = data["temperature"]
    hum  = data["humidity"]

    #Update Text
    document.getElementById("temp").innerText = str(temp) 
    document.getElementById("hum").innerText = str(hum)

    #Update Chart
    temps.append(temp)
    labels.append(str(len(labels)))

    if len(temps) > 20:
        temps.pop(0)
        labels.pop(0)
    chart.update()

#Sensor Loop
async def sensor_loop():
    while True:
        try:
            await get_sensor()
        except Exception as e:
            print(f"Error occurred: {e}")
        await asyncio.sleep(2)

#Start Background Task 
asyncio.ensure_future(sensor_loop())

#Led Control 
#Led ON
async def led_on(event):
    try:
        response = await pyfetch("/led/on",method="GET")
        data = await response.json()
        print(f'LED ON Response: {data}')
    except Exception as e:
        print(f"Error turning LED ON: {e}")

#Led OFF
async def led_off(event):
    try:
        response = await pyfetch("/ledoff",method="GET")
        data = await response.json()
        print(f"LED OFF Response: {data}")
    except Exception as e:
        print(f"Error turning LED OFF: {e}") 

#PROXY 
on_proxy =create_proxy(led_on) 
off_proxy = create_proxy(led_off) 

document.getElementById("onBtn").addEventListener("click", on_proxy)
document.getElementById("offBtn").addEventListener("click", off_proxy)

print("Script loaded")
