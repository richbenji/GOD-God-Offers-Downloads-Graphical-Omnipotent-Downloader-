# 🎓 Tutorial – GOD (God Offers Downloads)

## 🚀 Presentación

¡Bienvenido al tutorial de uso de la aplicación! Esta aplicación permite descargar vídeos y listas de reproducción de YouTube en formato de vídeo o audio, con soporte para listas de reproducción privadas.

La aplicación ofrece dos modos principales:

- 📥 **Descarga simple**: para gestionar vídeos uno por uno (o listas de reproducción)
- 📋 **Descarga por lotes (Batch)**: para descargar varias URLs de una sola vez

------

## 📥 Descarga simple

1. **Copia la URL** del vídeo de YouTube 🔗

2. **Pégala** en el campo de URL

3. **Haz clic** en el botón "➕ Verificar"

4. **Espera** a que se cargue la información del vídeo (miniatura, duración, tamaño)

   **Selecciona** tus opciones:

   - 🎥 **Vídeo**: elige la resolución (Best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, 144p)
   - 🎵 **Solo audio**: elige la tasa de bits (Best, 320, 256, 192, 128, 96, 64, 32 kbps) y el formato (M4A o MP3)

   **Haz clic** en "⬇️ Descargar"

   **Selecciona** la carpeta de destino

### Consejos 💡

- Puedes **añadir varios vídeos** a la cola antes de iniciar la descarga
- El **tamaño total** y el número de vídeos se muestran en el botón de descarga
- Usa el botón **🗑️ Vaciar cola** para eliminar todos los vídeos pendientes
- Haz clic en el botón **ℹ️** junto a cada vídeo para ver información detallada (formatos disponibles, descripción, etc.)
- Haz clic en **❌** para eliminar un vídeo de la cola

------

## 📚 Listas de reproducción

### Listas de reproducción públicas

¡Simplemente copia la URL de la lista de reproducción en la pestaña "Descarga simple", la aplicación detectará automáticamente todos los vídeos! Puedes modificar las opciones de vídeo/audio antes de iniciar la descarga.

La aplicación:

- ✅ Carga automáticamente todos los vídeos de la lista de reproducción
- ✅ Muestra una miniatura e información para cada vídeo
- ✅ Permite personalizar las opciones para cada vídeo individualmente
- ✅ Descarga todo en una sola operación

### 🍪 Listas de reproducción privadas

#### Método 1: Conexión automática a través del navegador (Recomendado ⭐)

**¡La aplicación utiliza automáticamente tus cookies de Firefox si estás conectado a YouTube!**

1. **Conéctate** a tu cuenta de YouTube en Firefox
2. **Copia** la URL de tu lista de reproducción privada
3. **Pégala** en la aplicación
4. ✅ **¡Funciona automáticamente!** La aplicación accede a tus cookies de Firefox

> 💡 **Consejo**: Mantente conectado a YouTube en Firefox para que la aplicación pueda acceder siempre a tus listas de reproducción privadas sin manipulación adicional.

#### Método 2: Exportación manual de cookies (Alternativa)

Si el método automático no funciona o si usas otro navegador, debes proporcionar tus **cookies de YouTube**:

1. Instala una extensión del navegador:
   - **Firefox**: [cookies.txt](https://addons.mozilla.org/es/firefox/addon/cookies-txt/) o [get cookies](https://addons.mozilla.org/es/firefox/addon/get_cookies/)
   - **Chrome**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore)
2. Conéctate a YouTube
3. **Exporta** tus cookies en formato Netscape (archivo `.txt`)
4. **Haz clic** en el botón "🍪 ⬆️ cookies.txt" en la parte superior izquierda de la aplicación
5. **Selecciona** tu archivo `cookies.txt`
6. **Prueba** con tu lista de reproducción privada

> ⚠️ **Advertencia**: ¡Nunca compartas tu archivo cookies.txt, contiene tus credenciales de inicio de sesión!

### ⚠️ Consejos

- No elimines el archivo cookies.txt
- Si aparece un error, recarga las cookies

------

## 📦 Descarga por lotes (Batch)

La pestaña "Descarga por lotes" permite descargar varios vídeos con los **mismos parámetros** para todos.

### Uso

1. **Abre** la pestaña "Descarga por lotes"
2. **Introduce** las URLs de los vídeos (una por línea) en el área de texto
   - O haz clic en "⬆️ Cargar desde archivo" para importar un archivo `.txt` que contenga tus URLs
3. **Selecciona** el tipo:
   - 🎥 **Vídeo**: con resolución común para todos
   - 🎵 **Solo audio**: con tasa de bits común para todos
4. **Elige** la resolución (si es vídeo) y la tasa de bits de audio
5. **Haz clic** en "⬇️ Descargar"
6. **Selecciona** la carpeta de destino

### Diferencia con la descarga simple

| Descarga simple                            | Descarga por lotes                 |
| ------------------------------------------ | ---------------------------------- |
| Opciones **personalizadas** por vídeo      | Opciones **idénticas** para todos  |
| Muestra miniaturas e información detallada | Interfaz simplificada              |
| Ideal para algunos vídeos variados         | Ideal para muchos vídeos similares |

------

## ⚙️ Opciones avanzadas

### Resolución de vídeo

| Resolución          | Uso recomendado                         | Tamaño aproximado (1h) |
| ------------------- | --------------------------------------- | ---------------------- |
| **Best**            | Mejor calidad disponible                | Variable               |
| **2160p (4K)**      | Pantallas 4K, archivado                 | ~4-8 GB                |
| **1440p (2K)**      | Monitores de alta definición            | ~2-4 GB                |
| **1080p (Full HD)** | Uso estándar, mejor compromiso ⭐        | ~1-2 GB                |
| **720p (HD)**       | Dispositivos móviles, ahorro de espacio | ~500 MB-1 GB           |
| **480p**            | Conexión lenta, almacenamiento limitado | ~300-500 MB            |
| **360p**            | Conexión muy lenta                      | ~200-300 MB            |

> 💡 **Consejo**: Para uso diario, **1080p** ofrece el mejor compromiso calidad/tamaño.

### Tasa de bits de audio

| Tasa de bits | Calidad           | Uso recomendado           | Tamaño (1h) |
| ------------ | ----------------- | ------------------------- | ----------- |
| **Best**     | Máximo disponible | Archivado, audiófilos ⭐   | Variable    |
| **320 kbps** | Excelente         | Música de alta calidad    | ~140 MB     |
| **256 kbps** | Muy buena         | Uso estándar              | ~115 MB     |
| **192 kbps** | Buena             | Compromiso calidad/tamaño | ~85 MB      |
| **128 kbps** | Correcta          | Podcasts, conferencias    | ~60 MB      |
| **96 kbps**  | Aceptable         | Solo voz                  | ~45 MB      |
| **64 kbps**  | Baja              | Conexión muy lenta        | ~30 MB      |

### Formato de audio

- **M4A**:
  - ✅ Mejor calidad con el mismo tamaño
  - ✅ Archivos más ligeros
  - ✅ Formato nativo de YouTube (sin conversión)
  - ❌ Menos compatible con reproductores antiguos
- **MP3**:
  - ✅ Compatible con todos los dispositivos
  - ✅ Ampliamente soportado
  - ✅ Personalizable (tasa de bits a elección)
  - ❌ Requiere conversión (FFmpeg necesario)

------

## Personalización

### 🌍 Cambiar idioma

Haz clic en el selector de idioma 🌐 en la parte superior izquierda para elegir entre los idiomas disponibles.

### 🌓 Modo oscuro / claro

Usa el interruptor **🌙 / ☀️** para cambiar entre temas.

------

## ❓ Problemas frecuentes

### "The playlist does not exist"

**Causas posibles:**

1. La lista de reproducción es **privada** → Asegúrate de estar conectado a YouTube en Firefox, o proporciona un archivo `cookies.txt`
2. La URL es incorrecta → Verifica que hayas copiado la URL completa de la lista de reproducción
3. La lista de reproducción fue eliminada → Verifica que todavía existe en YouTube

### "ERROR: unable to download video data"

**Causas posibles:**

1. Conexión a Internet inestable
2. Vídeo eliminado o privado
3. YouTube cambió su formato → Actualiza yt-dlp: `pip install -U yt-dlp`

### Descarga lenta

- **Soluciones:**
  - ✅ Verifica tu conexión a Internet 📶
  - ✅ YouTube a veces limita la velocidad según tu ubicación
  - ✅ Intenta descargar en otro momento
  - ✅ Descarga una resolución más baja (720p en lugar de 1080p)

### Error de conversión MP3

**Error**: `ERROR: ffmpeg not found`

**Solución**: La conversión MP3 requiere **FFmpeg** instalado en tu sistema.

**Instalación de FFmpeg:**

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Windows (Chocolatey)
choco install ffmpeg
```

**Verificar instalación:**

```bash
ffmpeg -version
```

### La descarga se detiene al 99%

¡Es normal! La aplicación está **fusionando** el vídeo y el audio (o convirtiendo a MP3). Este paso puede tardar desde unos segundos hasta unos minutos según:

- El tamaño del archivo
- La potencia de tu ordenador
- La resolución elegida

> 💡 **Consejo**: ¡No cierres la aplicación mientras la barra de progreso está al 99%!

### "Permission denied" durante la descarga

**Causas posibles:**

1. La carpeta de destino está protegida contra escritura
2. Un archivo con el mismo nombre ya está abierto
3. Tu antivirus está bloqueando la escritura

**Soluciones:**

- ✅ Elige una carpeta en tu directorio personal (Documentos, Descargas)
- ✅ Cierra cualquier archivo de vídeo abierto
- ✅ Añade una excepción en tu antivirus

## 📞 Soporte

### Obtener ayuda

Para cualquier pregunta o problema:

- 🐛 Reporta un error en [GitHub](https://github.com/richbenji/Ultimate-GUI-YouTube-Downloader-yt-dlp-Ctk)
- 💬 **Pregunta**: Consulta primero este tutorial, luego abre un issue en GitHub
- ⭐ **¿Te gusta la aplicación?**: ¡Dale una estrella en GitHub!

### Contribuir

¡El proyecto es de código abierto! Las contribuciones son bienvenidas:

- 🔧 Corrección de errores
- ✨ Nuevas funcionalidades
- 🌍 Traducciones adicionales
- 📖 Mejoras en la documentación

------

## 📜 Aviso legal

### Uso responsable

Esta aplicación es una herramienta de descarga. **Tú eres responsable** del uso que le des:

- ✅ **Permitido**: Descargar tus propios vídeos, contenido con licencia libre, o contenido del que tengas autorización
- ❌ **Prohibido**: Descargar contenido protegido por derechos de autor sin permiso, redistribuir contenido descargado

> ⚠️ **Importante**: Respeta siempre los términos de servicio de YouTube y las leyes de derechos de autor de tu país.

------

**¡Feliz descarga! 🎉**