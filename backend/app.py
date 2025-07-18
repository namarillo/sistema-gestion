from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "¡Sistema de gestión activo!"}

@app.get("/equipo/{hostname}")
def get_equipo(hostname: str):
    return {
        "hostname": hostname,
        "status": "activo",
        "zabbix": "Datos simulados de Zabbix",
        "wazuh": "Datos simulados de Wazuh"
    }