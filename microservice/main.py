from fastapi import FastAPI, HTTPException
from clickhouse_driver import Client
from fastapi.responses import JSONResponse
from typing import List


app = FastAPI()

# Conectar a ClickHouse
clickhouse_client = Client(host='localhost', port=9000)

# Ruta para consultar datos de una tabla específica
@app.get("/consultar/{table_name}/")
async def consultar_tabla(table_name: str):
    query = "SHOW TABLES"
    tables = clickhouse_client.execute(query)

    if tables:
       query2 = f"SELECT * FROM {table_name} LIMIT 10" 
       result2 = clickhouse_client.execute(query2)
       rows = [dict(row) for row in result2]
       return JSONResponse(content=rows)
    else:
        return JSONResponse(content={"message":"Table not found"}, status_code=404)
    
@app.get("/carreras-realizadas/", response_model=List[dict])
def obtener_carreras() -> List[dict]:
    try:
        query = "SELECT * FROM trips ORDER BY pickup_datetime LIMIT 10"
        result = clickhouse_client.execute(query)
        carreras = [dict(row) for row in result]
        return carreras
    except Exception as e:
        raise e
    
@app.get("/recogidas-por-barrio/", response_model=List[dict])
def recogidas_diarias_por_barrio() -> List[dict]:
    try:
        query = """
            SELECT
                pickup_date,
                pickup_ntaname,
                COUNT(*) AS number_of_trips
            FROM trips
            GROUP BY pickup_date, pickup_ntaname
            ORDER BY pickup_date
        """
        result = clickhouse_client.execute(query)
        recogidas_por_barrio = [dict(row) for row in result]
        
        return recogidas_por_barrio
    except Exception as e:
        raise e