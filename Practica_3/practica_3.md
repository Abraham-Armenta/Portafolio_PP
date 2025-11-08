# **Práctica 3 -- Instalacion de Haskell

**Materia:** Paradigmas de la programacion
**Carrera:** Ingeniero en Software y Tecnologías Emergentes  
**Institución:** FIAD - UABC  
**Alumno:** Abraham Armenta Marrufo
**Fecha:** 08/Nov/2025

## 🧭 Introducción

En esta práctica se documenta el proceso de instalación, configuración y verificación del entorno de desarrollo para el lenguaje de programación funcional **Haskell**, utilizando herramientas modernas como **GHCup**, **GHC**, **Cabal**, **Stack** y **Haskell Language Server (HLS)**. El objetivo principal es preparar un entorno funcional y estable que permita compilar, ejecutar y depurar programas escritos en Haskell, tanto desde la terminal como desde un editor como Visual Studio Code.

Haskell es un lenguaje fuertemente tipado, puro y no estricto, ampliamente utilizado en contextos académicos y en aplicaciones donde la corrección formal y la concurrencia son críticas. Por ello, dominar su entorno de desarrollo es un paso fundamental para explorar paradigmas de programación funcional y comprender conceptos como evaluación perezosa, funciones de orden superior y tipos algebraicos.

Durante esta práctica se abordan los siguientes aspectos:

- Instalación de GHCup y selección de versiones recomendadas de GHC, Cabal, Stack y HLS.
- Configuración del sistema para que los ejecutables estén disponibles desde la terminal (ajuste del `PATH`).
- Solución de errores comunes como la ausencia del archivo `lib/settings`.
- Verificación del entorno mediante la ejecución de un programa básico en Haskell (`hello.hs`).
- Reflexión sobre la importancia del entorno funcional en el desarrollo de software confiable y expresivo.

Esta práctica sienta las bases para futuros proyectos en Haskell, incluyendo el desarrollo de aplicaciones funcionales, la exploración de estructuras de datos inmutables y la integración con herramientas de análisis estático y pruebas formales.

## **Como instalarlo**

---

## Requisitos previos

- Windows 10 o superior
- Acceso a PowerShell o CMD
- Conexión a internet

---

## 1. Descargar e instalar GHCup

1. Ve al sitio oficial:  
   👉 [https://www.haskell.org/ghcup/](https://www.haskell.org/ghcup/)

2. Descarga el instalador para Windows y ejecútalo.

3. Durante la instalación, selecciona:
   - GHC (compilador)
   - Cabal (gestor de paquetes)
   - Stack (gestor de proyectos)
   - HLS (Haskell Language Server)

---

## 2. Verificar instalación

Abre PowerShell y ejecuta:

```powershell
ghc --version
stack --version
cabal --version
ghcup --version
```

## Conclusiones

La instalación del entorno de desarrollo para Haskell mediante **GHCup** se presenta, en términos generales, como un proceso accesible, automatizado y bien documentado. Gracias a esta herramienta, es posible gestionar múltiples versiones de GHC, Cabal, Stack y HLS desde una sola interfaz, lo que facilita enormemente la configuración inicial para estudiantes y desarrolladores.

Sin embargo, esta práctica también evidenció que, aunque el proceso es sencillo en teoría, pueden surgir complicaciones técnicas en la práctica. En mi caso particular, tras completar la instalación, me encontré con errores al ejecutar comandos como `ghci` y `runghc`, los cuales arrojaban el mensaje: `Missing file: C:\ghcup\ghc\9.6.7\lib\settings`

Este error se debió a una instalación incompleta o corrupta del compilador GHC, lo que impidió el uso del intérprete interactivo y la ejecución directa de programas. La solución consistió en **reinstalar GHC** desde GHCup, lo cual resolvió el problema de forma efectiva.

Esta experiencia resalta la importancia de:

- Verificar que los ejecutables estén correctamente añadidos al **PATH del sistema**.
- Utilizar herramientas como `ghcup whereis` y `where` para diagnosticar problemas de configuración.
- No asumir que una instalación exitosa implica una configuración funcional; es necesario **probar el entorno con ejemplos simples** como `hello.hs`.

En resumen, instalar Haskell con GHCup es un proceso amigable, pero requiere atención a los detalles y una actitud proactiva para resolver posibles fallos. Esta práctica no solo permitió configurar el entorno correctamente, sino que también fortaleció habilidades de diagnóstico y resolución de errores, fundamentales en el desarrollo de software.
