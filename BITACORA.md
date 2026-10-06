# Bitacora

## 2026-10-06 - Permisos al guardar archivos desde VS Code

### Problema

VS Code no permitia guardar archivos dentro de `src/django`, por ejemplo `src/django/app/urls.py`, y mostraba un error de permisos insuficientes.

### Diagnostico

Se revisaron los permisos con:

```bash
id
ls -ld . src src/django src/django/app src/django/app/urls.py
```

El usuario local era `guillenec`, pero `src/` y los archivos del proyecto Django pertenecian a `root:root`:

```text
drwxr-xr-x root root src
drwxr-xr-x root root src/django
-rw-r--r-- root root src/django/app/urls.py
```

Por eso VS Code, ejecutado como usuario normal, no podia modificar esos archivos.

### Causa probable

El servicio Docker estaba ejecutandose como `root` dentro del contenedor. Como `./src/django` esta montado como volumen en `/usr/src/app`, los archivos creados desde el contenedor tambien quedaban como `root` en el host.

### Reparacion manual

Ejecutar una sola vez desde la raiz del proyecto:

```bash
sudo chown -R "$USER:$USER" src
```

Verificar:

```bash
ls -ld src src/django src/django/app/urls.py
```

Deberia aparecer el usuario local como propietario, por ejemplo:

```text
guillenec guillenec src
guillenec guillenec src/django
guillenec guillenec src/django/app/urls.py
```

### Prevencion

Se agrego en `docker-compose.yml`:

```yaml
user: "${UID:-1000}:${GID:-1000}"
```

Esto hace que el contenedor ejecute el proceso con el mismo UID/GID del usuario local por defecto (`1000:1000`), evitando que cree archivos como `root`.

Si tu usuario no usa UID/GID `1000`, crear un archivo `.env` a partir de `.env.example`:

```bash
cp .env.example .env
id -u
id -g
```

Luego editar `.env` con esos valores:

```env
UID=1000
GID=1000
```

Recrear el contenedor si ya estaba levantado:

```bash
docker compose down
docker compose up --build
```
