 Tienda de Hardware - Proyecto Django

Integrantes

Jorge Torres,
Angelo Vidal


 Propósito

Sitio web para una tienda de venta de hardware computacional, que permite a los
usuarios explorar un catálogo de productos, conocer los vendedores asociados a
la plataforma, y hacer seguimiento a sus pedidos.

 Proyección del proyecto

El catálogo de productos ya usa PostgreSQL y se expone mediante una API REST
protegida con JWT (ver la sección «API REST»). En etapas futuras se planea:
- Modelos y base de datos para vendedores y pedidos reales
  (actualmente son datos de ejemplo definidos en las vistas)
- Búsqueda real de pedidos por ID de despacho
- Autenticación de vendedores, que puedan gestionar sus propios productos
- Carrito de compras y gestión de pedidos

## Estructura del proyecto

```
backend/
├── config/          # Configuración principal del proyecto (settings, urls)
├── core/             # App: página de inicio y base.html (navegación común)
├── productos/        # App: catálogo de hardware
├── usuarios/          # App: vendedores/tiendas asociadas a la plataforma
├── pedidos/           # App: seguimiento de pedidos
├── requirements.txt
├── manage.py
└── README.md
```

## Rutas principales

| URL | Nombre | Vista | Template | 
|-----|--------|-------|----------|
| / | inicio` | core.views.inicio | core/inicio.html |
| /productos/ | catalogo | productos.views.catalogo | productos/catalogo.html |
| /pedidos/| pedidos | pedidos.views.pedidos | pedidos/pedidos.html | 
| /usuarios/ | usuarios_lista | usuarios.views.lista | usuarios/lista.html | 
| /usuarios/<int:id>/ | usuarios_detalle | usuarios.views.detalle | usuarios/detalle.html | 
|/productos/crear/	|crear_producto|	productos.views.crear_producto|	productos/crear.html|
|/productos/<int:id>/editar/|	producto_editar	|productos.views.editar_producto|	productos/editar.html|
|/productos/<int:id>/eliminar/|	producto_eliminar	|productos.views.eliminar_producto|	(Vista de acción / Redirección)|

 Contexto y contenido dinámico

- **`core.views.inicio`** envía `nombre_tienda` y `descripcion` como variables simples.
- **`productos.views.catalogo`** envía la lista `productos`; el template usa `{% for %}`
  para recorrerla y `{% if producto.stock > 0 %}` para mostrar disponibilidad o "Agotado".
- **`pedidos.views.pedidos`** envía la lista `pedidos` (cada uno con sus productos
  anidados); el template usa `{% for %}` (anidado, para pedido y sus productos) y
  `{% if pedido.estado_despacho == 'Entregado' %}` para el estado.
- **`usuarios.views.lista`** envía la lista `vendedores` y `total`; el template usa
  `{% for %}` para recorrerlos, `{% if v.activo %}` para el estado y `{% if %}/{% else %}`
  para el caso sin registros.
- **`usuarios.views.detalle`** envía `vendedor` (o `None`); el template usa
  `{% if vendedor %}/{% else %}` para el caso "no encontrado".

Instalación y ejecución

Requisitos: Python 3.12 o superior y un servidor PostgreSQL con una base de
datos creada para el proyecto.

1. Clonar el repositorio:
   ```
   git clone https://github.com/Jorgeatm1004/Tienda_hardware_backend.git
   cd Tienda_hardware_backend
   ```
2. Crear el entorno virtual:
   ```
   python -m venv .venv
   ```
3. Activar el entorno virtual:
   ```
   .\.venv\Scripts\Activate.ps1      # Windows (PowerShell)
   source .venv/bin/activate         # Linux / macOS
   ```
4. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Configurar las variables de entorno: duplicar `.env.ejemplo` como `.env` en
   la raíz del proyecto y completar `SECRET_KEY`, `DEBUG` y los datos de
   conexión a PostgreSQL. El archivo `.env` no se sube a GitHub.
6. Ejecutar migraciones y cargar los productos de ejemplo:
   ```
   python manage.py migrate
   python manage.py loaddata productos_ejemplo
   ```
7. Crear un superusuario:
   ```
   python manage.py createsuperuser
   ```
8. Levantar el servidor:
   ```
   python manage.py runserver
   ```
9. Abrir en el navegador: `http://127.0.0.1:8000/`

## API REST

La API usa Django REST Framework y autenticación JWT (`djangorestframework-simplejwt`).
Todas las respuestas son JSON.

### Endpoints

| Método | URL | Descripción | Requiere token | Respuesta correcta |
|--------|-----|-------------|----------------|--------------------|
| POST | `/api/token/` | Obtiene el token de acceso y el de refresco | No (usuario y contraseña) | 200 |
| POST | `/api/token/refresh/` | Renueva el token de acceso | No (token de refresco) | 200 |
| GET | `/api/productos/` | Lista los productos | No | 200 |
| GET | `/api/productos/<id>/` | Consulta un producto | No | 200 |
| POST | `/api/productos/` | Crea un producto | Sí | 201 |
| PUT / PATCH | `/api/productos/<id>/` | Modifica un producto | Sí | 200 |
| DELETE | `/api/productos/<id>/` | Elimina un producto | Sí | 204 |

### Autenticación

1. Pedir el token con `POST /api/token/` y el cuerpo
   `{"username": "...", "password": "..."}`.
2. Enviar el token de acceso en cada petición protegida con la cabecera
   `Authorization: Bearer <token>`.
3. El token de acceso dura 30 minutos y el de refresco 1 día.

### Permisos

La API usa `DjangoModelPermissionsOrAnonReadOnly`:
- Cualquiera puede leer (GET).
- Para crear, modificar o eliminar se necesita un token válido (sin token: 401)
  y los permisos del modelo `Producto` asignados en el Admin (sin ellos: 403).

### Validaciones

- `precio` debe ser mayor que 0.
- `stock` no puede ser negativo.
- `nombre`, `descripcion`, `precio` y `stock` son obligatorios.
- Si los datos no son válidos, la API responde 400 con el detalle de los errores.

### Usuarios de prueba

Se crean localmente; sus contraseñas no se publican en el repositorio.

| Usuario | Tipo | Uso |
|---------|------|-----|
| `admin_tienda` | Superusuario | Pruebas del CRUD completo |
| `usuario_normal` | Usuario sin permisos sobre `Producto` | Prueba del error 403 |

 Trabajo colaborativo con Git y GitHub

- Cada integrante trabajó en su propia rama (`dev/core`, `dev/productos`,
  `dev/pedidos`, `dev/usuarios`).
- Las ramas se integraron primero en una rama de prueba (`test-integracion`)
  para resolver conflictos con calma antes de fusionar a `main`.


 Dificultades y soluciones

- **Error `ImproperlyConfigured` por typo en `urls.py`** (`urlspatterns` en vez
  de `urlpatterns`). Solución: corregir el nombre exacto de la variable que
  Django espera.
- **Desajuste entre el contexto de la vista y el template en `pedidos`**: la
  vista enviaba la clave `pedido` (singular, un solo diccionario) pero el
  template esperaba `pedidos` (plural, una lista) para el `{% for %}`. Django
  no arrojaba error, solo omitía el contenido silenciosamente. Solución:
  ajustar la vista para enviar una lista bajo la clave `pedidos`.
- **`pip install -r requirements.txt` fallaba** con `Invalid requirement`.
  Causa: el archivo estaba en UTF-16 (guardado desde PowerShell). Solución:
  regenerarlo en UTF-8.
- **Conflictos de merge en `config/urls.py` y `base.html`**, ya que cada rama
  agregaba su propia línea en el mismo bloque. Solución: crear una rama de
  integración (`test-integracion`) para fusionar las 4 ramas una por una,
  resolviendo cada conflicto con calma antes de tocar `main`.
- Error 403 (CSRF token missing) al enviar el formulario de creación: El template HTML inicial no utilizaba la etiqueta de seguridad {% csrf_token %} o no heredaba correctamente del template base con el contexto del request.
Se soluciono incluyendo el token de seguridad de manera correcta y se ajusta la estructura basada en core/base.html.


Registro de uso de IA

Se hizo uso de de IA para resolver dudas y para la corrección de errores que se presentaron a lo largo del desarrollo del trabajo




