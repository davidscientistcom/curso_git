# Laboratorio FASE 0: El Monolito Espagueti

¡Bienvenidos a la Fase 0 del sistema de gestión!
Este código representa lo que **NO debemos hacer** a la hora de diseñar software.
Es un ejemplo perfecto de código "legado" mal estructurado, sin arquitectura y con testing frágil.

## Escenario Actual
Tienes una aplicación que gestiona Clientes, Productos y Ventas. Todo el código está amontonado en un solo fichero: `gestion_monolito.py`.

## Problemas de este código:
1. **Estado Global**: Se usan variables globales (`clientes_db`, etc.) compartidas que provocan efectos secundarios inesperados entre ejecuciones y tests.
2. **Complejidad Ciclomática**: Las funciones como `crear_cliente` tienen un anidamiento profundo de estructuras `if/else`, dificultando la lectura y las pruebas.
3. **Alto Acoplamiento**: La lógica de validación de datos está directamente acoplada con la lógica de negocio y de "almacenamiento".
4. **Tests Frágiles**: Los tests dependen del orden de ejecución. Si ejecutas un solo test aisladamente, fallará porque asume un estado creado por tests anteriores.

## Instrucciones del Laboratorio

### 1. Preparar el Entorno (Conda)
Asegúrate de estar usando el entorno:
```bash
conda activate bootcamp_git
```
*(Si no lo tienes, créalo con `conda create -n bootcamp_git python=3.10 -y` y luego instala las dependencias).*

```bash
pip install -r requirements.txt
```

### 2. Rompe los tests a propósito
Ejecuta las pruebas de forma secuencial:
```bash
pytest -v
```
¡Todo verde! Pero ahora intenta ejecutar **solo un test específico**:
```bash
pytest test_gestion.py::test_realizar_venta_vip_exito -v
```
¿Qué pasa? **¡Falla estrepitosamente!** Falla porque dependía de que los tests anteriores rellenaran las listas globales. Esto en la vida real es un desastre que te hará perder días de trabajo.

### 3. Medición de Cobertura Basura
Ejecuta este comando para ver qué porcentaje del código prueban realmente nuestros tests:
```bash
pytest --cov=gestion_monolito
```
Observarás que hay partes considerables del código (rutas de error, comprobaciones de tipos) que jamás se llegaron a testear.

### Tu Objetivo Analítico
Abre `gestion_monolito.py`. Fíjate en el bloque `if/else` de la función de ventas. Piensa: ¿Qué pasaría si te piden añadir un descuento especial si el cliente cumple los años hoy? ¿Dónde lo pondrías? ¿Cuántos tests se romperían?

**Para ver la solución profesional a esto, cambia a la siguiente rama:**
`git checkout 1_fase_fastapi_modular`
