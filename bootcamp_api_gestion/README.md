# Laboratorio FASE 2: Arquitectura Limpia (Clean Architecture) y SOLID

¡Bienvenidos a la Fase Final!
Hemos transformado nuestro código de un monolito acoplado a una estructura profesional altamente escalable.

## ¿Qué hemos logrado?
1. **Separación de Responsabilidades (SRP)**:
   - `src/domain`: Contiene las reglas más puras (Entidades e Interfaces). No sabe NADA de FastAPI ni de bases de datos.
   - `src/use_cases`: Orquesta la lógica de negocio (por ejemplo, cómo se realiza una venta). Tampoco sabe de HTTP.
   - `src/infrastructure`: Contiene todo el detalle externo (FastAPI "routers" y las bases de datos en memoria).

2. **Inversión de Dependencias (DIP)**:
   - Los Casos de Uso dependen de `Interfaces` (`ClienteRepository`), no de implementaciones concretas.
   - FastAPI inyecta la implementación real (`InMemoryClienteRepository`) a través de dependencias (`Depends`).

3. **Facilidad Asombrosa de Testing**:
   - Revisa `tests/test_api.py`. Gracias a FastAPI `dependency_overrides`, podemos cambiar la base de datos real por una de prueba en 1 sola línea, sin tocar el código de negocio.
   - Los tests son completamente predecibles.

## Ejercicio Práctico
Avanza y verifica que la configuración del entorno sigue activa:
```bash
conda activate bootcamp_git
```

1. **Ejecuta los tests**:
   ```bash
   pytest tests/ -v
   ```
2. **Mira la Cobertura Definitiva**:
   ```bash
   pytest --cov=src --cov=app tests/
   ```
   La cobertura es excelente y el código es resistente al cambio. Si mañana queremos cambiar la base de datos en memoria por **PostgreSQL**, ¡sólo tenemos que crear un `PostgresClienteRepository` que cumpla la interfaz, y cambiar 1 línea en `dependencies.py`!

**Conclusión del Bootcamp**:
Habéis visto cómo un diseño estructurado reduce la "Deuda Técnica", hace que las pruebas sean triviales y permite que la aplicación crezca sin romperse.
