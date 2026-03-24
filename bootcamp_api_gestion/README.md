# Laboratorio FASE 1: FastAPI y Modularidad

> ⚠️ **TIP DE NAVEGACIÓN Git:**
> Estás en la **Fase 1**.
> - Para volver atrás: `git checkout 0_fase_inicial`
> - Para avanzar a la final: `git checkout 2_fase_arquitectura_avanzada`

¡Bienvenidos a la Fase 1! 
En la fase anterior vimos los horrores del código acoplado en un solo fichero `gestion_monolito.py`. Ahora hemos introducido **FastAPI** y **Pydantic**.
Hemos borrado el antiguo código y hemos reorganizado el proyecto en módulos dentro de la carpeta `app/`.

## ¿Qué ha cambiado?
1. **Modelos Pydantic (`schemas.py`)**: Hemos eliminado todos los `if/else` interminables. Pydantic se encarga de que la edad sea `int`, que sea mayor a 18, y que el email sea válido.
2. **Modularidad (`routers/`)**: Hemos separado la lógica en diferentes archivos según el dominio (Clientes, Productos, Ventas).
3. **Manejo de Errores Standard**: En lugar de hacer prints o devolver diccionarios con la clave `"error"`, ahora levantamos `HTTPException`s y retornamos códigos HTTP reales (400, 404, 422).
4. **Tests Claros y Aislados**: Con FastAPI `TestClient` y los **fixtures** de Pytest, limpiamos el estado global antes de cada prueba. El orden de los tests ya no importa y nunca fallarán al azar.

## Instrucciones del Laboratorio

### 1. Preparar el Entorno
Seguimos en el entorno `bootcamp_git`. Hay que instalar las nuevas dependencias:
```bash
pip install -r requirements.txt
```

### 2. Ejecutar las Pruebas
Ahora ejecutar tests es una maravilla y no dependen del orden:
```bash
pytest tests/ -v
```
Pruébalos individualmente y verás que no se rompen. El fixture `run_around_tests` (en `test_api.py`) se encarga de limpiar las listas globales antes y después de cada prueba.

### 3. Cobertura de Código (Coverage)
Corre el siguiente comando:
```bash
pytest --cov=app tests/
```
Veréis que la cobertura ha subido drásticamente comparado con la fase 0. ¿Por qué? ¡Porque la complejidad ciclomática de nuestro código es casi cero! Pydantic hace el levantamiento de excepciones por nosotros, así que nuestras rutas solo tienen la "ruta feliz" y excepciones HTTP claras.

### Limitaciones Actuales (Tu reto analítico)
1. Aún usamos listas en memoria (`database.py`) que actúan como estado global y complican el acceso concurrente real.
2. **Lo peor de todo:** La lógica de negocio está acoplada directamente a FastAPI (en los endpoints / routers). Si quisiéramos usar esta lógica en una tarea en background o desde una consola, tendríamos que reescribirla.

**Para ver la solución profesional a estos problemas (Arquitectura Limpia), cambia a la rama final:**
`git checkout 2_fase_arquitectura_avanzada`
