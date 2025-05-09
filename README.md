
# Frontend del Proyecto

Este repositorio contiene el frontend de la aplicación, desarrollado en **Vue 3** con **Vite** y **TypeScript**. A continuación, se describe cómo configurar el entorno de desarrollo, así como algunas consideraciones importantes para mantener el proyecto ordenado.

---

## 🔧 Configuración del entorno

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/usuario/nombre-del-repo.git
   cd nombre-del-repo
   ```

2. **Instalar dependencias**
   ```bash
   npm install
   ```

3. **Levantar el entorno de desarrollo**
   ```bash
   npm run dev
   ```

   Esto levantará el proyecto en `http://localhost:5173`

---

## 📁 Estructura del proyecto

Por el momento es importante **no eliminar** ni mover las siguientes carpetas:

- `src/components/`: contiene los componentes reutilizables de la aplicación.
- `src/assets/`: almacena imágenes, íconos, hojas de estilo o recursos estáticos.

Estas carpetas son requeridas para mantener el diseño modular del sistema y serán reorganizadas más adelante.
---

## 📦 Sobre el `package.json`

Actualmente, el archivo `package.json` contiene algunas dependencias que **no están siendo utilizadas activamente**. Estas se mantendrán temporalmente por compatibilidad, serán revisadas más adelante.

📌 **Próximamente** se realizará una depuración del archivo `package.json` para eliminar:

- Paquetes no utilizados.
- Dependencias duplicadas o redundantes.
- Scripts obsoletos.

Esto ayudará a reducir el peso del proyecto y mejorar los tiempos de instalación y compilación.

---

## ✅ Consideraciones

- Usa componentes desde la carpeta `components` siempre que sea posible.
- No borrar ni modificar directamente archivos del sistema sin validación previa.
- Para íconos, se utiliza `@iconify/vue`.

