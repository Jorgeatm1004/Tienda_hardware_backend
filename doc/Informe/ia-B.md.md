# Registro de uso de Inteligencia Artificial - Parte B (Jorge Torres)

Para el desarrollo del CRUD de productos y la configuración de la API, se utilizó el modelo Gemini. A continuación se detallan las iteraciones y problemas resueltos:

| Iteración | Problema | Qué se hizo | Cómo se verificó |
| :--- | :--- | :--- | :--- |
| 1 | **Error 400/401 `bad_authorization_header`** al probar la API con token. | La IA explicó que se estaba pegando el JSON completo (`"access": "eyJ..."`) en el campo Bearer. Se corrigió para pegar únicamente el texto del token. | Thunder Client devolvió estado `201 Created` y `200 OK` en las peticiones posteriores. |
| 2 | **`ModuleNotFoundError: No module named 'productos.serializers'`**. | El archivo se había creado fuera del directorio correcto. La IA indicó la ruta exacta donde debía estar el archivo. | Se movió el archivo a la carpeta `productos/` y el servidor levantó sin errores. |
| 3 | **Contraseña del superusuario olvidada** debido al cambio de base de datos entre clones locales. | La IA recordó que Django no guarda claves legibles y proporcionó el comando `python manage.py changepassword jorge`. | Se generó exitosamente el token en `/api/token/` con la nueva clave. |
| 4 | **`AttributeError: get_succes_headers`** al crear un producto. | La IA detectó un error tipográfico en el código generado (faltaba una 's'). Se corrigió a `get_success_headers`. | El POST en `/api/productos/` retornó 201 y el `"mensaje": "Registro creado"`. |
| 5 | **Bloqueo de `Activate.ps1` en PowerShell** (políticas de grupo). | Se discutieron alternativas. Se optó por usar CMD (`\Scripts\activate.bat`) o activación manual de variables. | El entorno virtual se activó correctamente para correr el servidor. |
| 6 | **Confusión en el origen del error 400 por stock negativo**. | La IA asumió que el rechazo era exclusivo de `validate_stock`, pero detectamos que el modelo `PositiveIntegerField` lo ataja primero. | Se corrigió la redacción en el informe final para reflejar el comportamiento real de Django. |