# Proyecto Práctico: Evolución de Arquitectura API

Bienvenido al laboratorio práctico del Bootcamp de Git & GitHub. 
Esta carpeta contiene un código que **cambia y evoluciona dependiendo de la rama de Git en la que te encuentres**.

## ¿De qué trata este laboratorio?
Vas a vivir en primera persona cómo un proyecto "espagueti" mal diseñado (Fase 0) evoluciona a un código modular con **FastAPI** (Fase 1) y finalmente a una **Arquitectura Limpia** profesional (Fase 2). En cada fase verás sus problemas, aprenderás a solucionarlos y probarás el código usando los tests.

---

## 🗺️ MAPA DE RAMAS (Cómo navegar el laboratorio)

Para hacer este laboratorio paso a paso, **debes abrir tu terminal en esta carpeta** y usar el comando `git checkout` para "saltar" entre las fases del código.

### 🟡 Fase 0: El Monolito Inicial
Aquí verás todo el código en un solo archivo, con estado global y pruebas frágiles.
👉 **Comando para iniciar:**
```bash
git checkout 0_fase_inicial
```

### 🟠 Fase 1: FastAPI y Modularidad
Aquí introducimos FastAPI y Pydantic para validar datos, pero aún está acoplado a la BD.
👉 **Comando para saltar:**
```bash
git checkout 1_fase_fastapi_modular
```

### 🟢 Fase 2: Arquitectura Limpia (SOLID)
El diseño final y profesional con Inyección de Dependencias, Casos de Uso y Dominios puros.
👉 **Comando para ver la solución final:**
```bash
git checkout 2_fase_arquitectura_avanzada
```

---

## 🛠️ Instrucciones Generales
1. **Entorno**: Asegúrate de tener listo tu entorno Conda. En la Fase 2 tienes un script `setup_conda.sh` si lo necesitas, o puedes crearlo manualmente:
   `conda create -n bootcamp_git python=3.10 -y && conda activate bootcamp_git && pip install fastapi uvicorn httpx pytest pytest-cov`
2. **Lee el README de cada rama**: Una vez hagas `git checkout`, el archivo `README.md` que estás leyendo AHORA MISMO **cambiará automáticamente** para explicarte la fase actual.
3. **No rompas la historia principal**: Al ser un laboratorio de Git, siéntete libre de experimentar, ¡pero ten cuidado de no mezclar ramas si no se te pide!

¡Abre tu terminal, activa el entorno Virtual y ejecuta `git checkout 0_fase_inicial` para comenzar la magia!
