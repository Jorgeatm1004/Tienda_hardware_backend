 Tienda de Hardware - Proyecto Django

Integrantes

Jorge Torres,
Angelo Vidal


 Propósito

Sitio web para una tienda de venta de hardware computacional, que permite a los
usuarios explorar un catálogo de productos, conocer los vendedores asociados a
la plataforma, y hacer seguimiento a sus pedidos.

 Proyección del proyecto

Esta es la primera versión navegable del sitio, desarrollada hasta el contenido
de templates. En etapas futuras del semestre se planea incorporar:
- Modelos y base de datos para productos, vendedores y pedidos reales
  (actualmente son datos de ejemplo definidos en las vistas)
- Búsqueda real de pedidos por ID de despacho
- Autenticación de vendedores, que puedan gestionar sus propios productos
- Carrito de compras y gestión de pedidos
- Una API REST para exponer el catálogo de productos

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

1. Clonar el repositorio:
   ```
   git clone https://github.com/Jorgeatm1004/Tienda_hardware_backend.git
   cd Tienda_hardware_backend
   
2. Crear entorno virtual:
   
   python -m venv .venv
   
3. Activar entorno virtual:
   
   .\.venv\Scripts\Activate.ps1
   
4. Instalar dependencias:
   
   pip install -r requirements.txt
   
5. Configurar la variable de entorno:

  Duplicar el archivo .env.ejemplo como .env en la raiz del proyecto y ajustar
  los valores de la conexion de la base de datos segun el entorno local.

6. Ejecutar migraciones:
   
   python manage.py migrate
   
6. Levantar el servidor:
   
   python manage.py runserver
   
7. Abrir en el navegador: `http://127.0.0.1:8000/`

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




