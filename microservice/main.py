from fastapi import FastAPI
from clickhouse_driver import Client
from fastapi.responses import JSONResponse
import clickhouse_connect


app = FastAPI()

# Conectar a ClickHouse
clickhouse_client = clickhouse_connect.get_client(host='localhost', username='default', password='password')


# Ruta para consultar datos de una tabla específica
@app.get("/consultar/{table_name}/")
async def consultar_tabla(table_name: str):
    # query = "SHOW TABLES"
    # # tables = clickhouse_client.execute(query)
    # tables = clickhouse_client.command(query)

    # if tables:
    #    query2 = f"SELECT * FROM {table_name} LIMIT 10" 
    #    result2 = clickhouse_client.command(query2)
    #    rows = [dict(row) for row in result2]
    #    return JSONResponse(content=rows)
    # else:
    #     return JSONResponse(content={"message":"Table not found"}, status_code=404)
    return 0