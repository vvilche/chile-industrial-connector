# Minuta de Trabajo y Oportunidades Comerciales: Cementos Melón S.A.

**Fecha:** 26 de junio de 2026  
**Preparado por:** Víctor Vilches / Equipo de Automatización SUPCON  
**Cliente:** Cementos Melón S.A.  
**Asunto:** Diagnóstico Tecnológico, Oportunidades de Control Avanzado (APC) y Soluciones de Instrumentación  

---

## 1. Ficha Técnica del Cliente: Cementos Melón S.A.

*   **Razón Social:** Melón S.A.
*   **Sector Industrial:** Cemento, Cal y Materiales
*   **Sitio Web:** [https://www.melon.cl](https://www.melon.cl)
*   **Planta Analizada:** **Planta La Calera (LCA)**, Región de Valparaíso, Chile.

---

## 2. Diagnóstico de la Arquitectura de Control (Basado en Plano: *RedControl LCA_Rev0*)

Tras realizar la extracción y análisis técnico de los elementos y metadatos del plano de arquitectura de comunicaciones **"RedControl LCA_Rev0" (Planta La Calera)**, se ha mapeado con precisión la infraestructura de control, comunicaciones y los puntos críticos del proceso:

### A. Capa de Control (PLCs) y Servidores
La planta cuenta con una arquitectura mixta de controladores Schneider Electric (Quantum y M580):
*   **Área H9 (Clave para Procesos de Combustión/Horno):** 
    *   **PLC H9:** Controlador asociado a un módulo de comunicaciones Ethernet **NOC 0301**. Controla directamente la zona de quemadores e instrumentación crítica.
    *   **PLC ALIMH9 (Alimentación H9):** Encargado de la dosificación y alimentación, equipado también con un módulo **NOC 0301**.
    *   **PLC COMBUST ALTERNAT (Combustibles Alternativos):** Controla el sistema de inyección de combustibles alternos (co-procesamiento), con módulo **NOC 0301**.
*   **Área de Molienda:**
    *   **PLC MOLINO 21 y PLC MOLINO 22:** Controladores **Quantum (140CPU65150 y 140CPU65160)** que utilizan módulos Ethernet **140NOE771** y cuentan con buses de campo **Profibus** para la integración de instrumentación y accionamientos de molinos.
*   **Otras Áreas de Control Mapeadas:**
    *   **PLC M18-M19** (con migración pendiente de `PLC OLDM18` Quantum a M580).
    *   **PLC M17:** Integra una isla de E/S remotas mediante módulo **BMXCRA31200 / CRP 31200**.
    *   **PLC SECADOR:** Asociado a un switch local Moxa EDS208ST.
    *   **PLC HUMECTAC** (Humectación).
    *   **PLC ENV1 (Envasadora 1) y PLC ENV2 (Envasadora 2 / Silo 28):** Equipados con módulos **NOE 77100**.
    *   **PLC VALVULAS SILOS 3000 y PLC SILOS 2000:** Módulos Ethernet **NOE 77100**.
    *   **PLC MEDIDORES ELÉCTRICOS LCA:** Concentra la telemetría eléctrica mediante módulos Ethernet **NOE77101**, operando en la subred de medidores (`192.168.10.0`) y la red de control VTS (`10.180.0.0`).
*   **Servidores de Datos:**
    *   **SERVIDOR API-NODE H9 PI LA CALERA:** Servidor concentrador de datos para el sistema de información e historial de planta (OSIsoft PI System) en la zona H9.

### B. Capa de Red e Infraestructura de Comunicaciones
*   **Switches Core de Planta:** La red principal está soportada por switches industriales Moxa de alta capacidad de la serie **IKS (Moxa IKS6726-2GTXSFP/2IM6700A)** en configuración de redundancia y switches Cisco **SF300-48**.
*   **Switches de Distribución / Anillo (DRS):** Se utilizan switches Schneider/Telemecanique de la serie **TCSESM (TCSESM63F2CU1C y TCSESM083F2CS0)** configurados con anillos redundantes y segmentación mediante VLANs (Master Ring VLAN y Slave Ring VLAN).
*   **Medio de Transmisión:** Mezcla de enlaces de Fibra Óptica (FO) multimodo/monomodo y cableado de cobre Ethernet.

---

## 3. Identificación de Puntos de Dolor y Oportunidades para SUPCON

El análisis del plano ha revelado dos problemas críticos en la planta de La Calera que representan oportunidades inmediatas de venta de soluciones y servicios para SUPCON:

### Oportunidad 1: Diagnóstico y Solución al Problema de Medición de Flujo (Coriolis en H9)
El plano detalla la conexión de los flujómetros de la zona H9:
*   **Arquitectura de Conexión del Plano:**
    *   `RED 422/485 LINK150 CORIOLIS PRE`
    *   `RED 422/485 LINK150 CORIOLIS ALIM`
*   **Análisis del Problema:** Los caudalímetros Coriolis de la línea de **Precalentador (PRE)** y de **Alimentación (ALIM)** se comunican mediante un enlace serial RS-422/RS-485 (Modbus RTU) que se conecta a la red Ethernet de control a través de pasarelas **Link150 (Schneider Electric)** hacia el **PLC H9**.
*   **Causas Probables del Fallo de Medición/Comunicación:**
    1.  *Ruido Electromagnético (EMI):* La planta de cemento presenta altos niveles de ruido eléctrico por variadores de frecuencia y motores de gran potencia. Un tendido serial RS-485 largo sin aislamiento galvánico adecuado corrompe las tramas Modbus, provocando pérdidas de comunicación.
    2.  *Saturación del Gateway Link150:* Si el PLC H9 y el servidor PI (API-Node) consultan simultáneamente al gateway Link150 a alta velocidad, este se satura, generando pérdidas de paquetes y demoras en las variables críticas de control.
    3.  *Efecto Bifásico / Aire Arrastrado:* En la línea de combustibles líquidos o aditivos, la presencia de burbujas de aire (flujo bifásico) desestabiliza los tubos sensores de los Coriolis legacy, deteniendo la medición o arrojando errores graves de densidad.
*   **Solución Propuesta por SUPCON:**
    *   **Sustitución Tecnológica:** Suministrar **Coriolis SUPCON (Serie SFC)** con transmisores avanzados que cuentan con algoritmos de procesamiento digital de señales (DSP) para compensar el flujo bifásico (aire arrastrado) y alta inmunidad al ruido.
    *   **Migración de Comunicaciones:** Eliminar la pasarela intermedia Link150 y cablear los flujómetros directamente mediante enlaces con aislamiento galvánico o transitando a protocolos Ethernet nativos como **Modbus TCP** o **Profinet** directamente desde el transmisor del flujómetro SUPCON al switch de anillo.

---

### Oportunidad 2: Vulnerabilidad de Red - "Tramo Faltante de Fibra Óptica"
*   **Hallazgo del Plano:** El plano contiene la alerta explícita: **"TRAMO FALTANTE FIBRA OPTICA SALA CAL Y SALA CAS"**.
*   **Impacto Operativo:** Este tramo faltante impide el cierre físico del anillo de fibra óptica entre la Sala de Cal y la Sala CAS. Al no estar cerrado el anillo, la red de control pierde su capacidad de **redundancia física**. Ante cualquier corte de fibra o falla en un switch de esa zona, se producirá una parada de comunicaciones y la pérdida de control de los procesos asociados, sin posibilidad de conmutación automática (RSTP/ERPS).
*   **Solución Propuesta por SUPCON:**
    *   Ofrecer el **diseño, suministro y canalización del tramo de fibra óptica faltante** para cerrar el anillo.
    *   Suministrar e integrar switches gestionados de SUPCON con soporte de protocolos de recuperación ultra-rápida ante fallos de anillo (tiempo de recuperación < 20 ms).

---

### Oportunidad 3: Reemplazo del Sistema Experto (FLSmidth PXP)
*   Dado que el cliente perderá las licencias de FLSmidth PXP y requiere una alternativa robusta para la optimización de la planta, **SUPCON APC-Suite (APC-Cement)** encaja perfectamente para integrarse con la base instalada de PLCs M580 y Quantum mapeada en el plano, optimizando el horno y los Molinos 21/22.

---

## 4. Plan de Acción Comercial

1.  **Validación con el Cliente:** Enviar el correo de respuesta demostrando que hemos analizado su arquitectura (PLC H9, Molinos 21/22, gateways Link150 de Coriolis, y el anillo de fibra). Esto generará un alto impacto y confianza técnica.
2.  **Preparación de Propuestas Dedicadas:**
    *   *Propuesta A:* Optimización Experta con SUPCON APC-Cement.
    *   *Propuesta B:* Solución de instrumentación para los Coriolis de PRE y ALIM con tecnología inmune al ruido y al flujo bifásico.
    *   *Propuesta C:* Proyecto de cierre de anillo de fibra óptica (Tramo Sala Cal - Sala CAS).

---

## 5. Propuesta de Correo de Respuesta para el Cliente (Refinada con Hallazgos del Plano)

***

**Asunto:** Propuestas de Optimización, Redundancia de Red e Instrumentación Coriolis - Planta La Calera Melón

Estimado [Nombre del Contacto en Cementos Melón],

Agradezco enormemente su respuesta detallada y el envío del plano de arquitectura **"RedControl LCA_Rev0"** de la Planta La Calera. Nuestro equipo de ingeniería ha revisado en detalle el diagrama unilineal y la distribución de sus sistemas de control. 

En base a este análisis técnico de su arquitectura (basada en switches de core Moxa, anillos de distribución Schneider TCSESM, y la base de PLCs Quantum y M580), hemos identificado tres áreas críticas donde **SUPCON** puede aportar soluciones de alto valor e impacto inmediato para sus operaciones:

1.  **Alternativa para el Reemplazo del Sistema Experto (Optimización del Proceso):**
    Observamos que áreas de alta criticidad como el Horno (asociado al PLC H9) y los **Molinos 21 y 22** (soportados por PLCs Quantum con buses Profibus) son candidatos ideales para la implementación de nuestra suite de Control Avanzado de Procesos **SUPCON APC-Cement**. 
    Dado el próximo vencimiento de sus licencias de *FLSmidth PXP*, nuestra suite —basada en Control Predictivo Multivariable (MPC)— puede integrarse de manera transparente con su plataforma actual (incluyendo los nuevos PLCs M580 y el Servidor API-Node PI de H9) para estabilizar la operación del horno y maximizar la eficiencia energética y la capacidad de producción (t/h) de los molinos. Nos gustaría proponerle un **estudio de viabilidad técnica (Feasibility Study)** sin costo comercial inicial para evaluar el retorno de inversión en estas unidades.

2.  **Solución Integral al Problema de Medición en los Flujómetros Coriolis (H9):**
    En el plano identificamos las líneas de medición seriales RS-422/485 conectadas a través de pasarelas **Link150** (`CORIOLIS PRE` y `CORIOLIS ALIM`) hacia el **PLC H9**. En procesos cementeros, esta arquitectura suele presentar inconvenientes debido a la inducción de ruido electromagnético en los lazos seriales o a la saturación de las pasarelas por consultas concurrentes del PLC y sistemas de información como PI.
    Para resolver esto de raíz, en **SUPCON** proponemos el uso de nuestros **Coriolis de la serie SFC**, los cuales cuentan con procesamiento digital de señales (DSP) de alta inmunidad al ruido y opción de comunicación Ethernet nativa (Modbus TCP/Profinet), eliminando intermediarios y garantizando la estabilidad de la lectura de flujo y densidad en condiciones severas.

3.  **Robustecimiento de la Red de Control (Cierre de Anillo de Fibra Óptica):**
    Hemos tomado nota de la indicación en su plano sobre el **"Tramo Faltante de Fibra Óptica entre la Sala Cal y la Sala CAS"**. Esta discontinuidad impide el cierre del anillo físico de comunicaciones, dejando a la planta sin redundancia ante cortes de fibra o fallos de switches en esa sección. 
    Ponemos a su disposición nuestra capacidad de integración para suministrar e instalar este tramo de fibra óptica y configurar los protocolos de redundancia industrial necesarios para asegurar que su red de control cuente con una tolerancia a fallas de nivel de clase mundial.

Le propongo que agendemos una sesión técnica virtual de 30 minutos la próxima semana para revisar estos puntos y presentarle nuestras tecnologías aplicadas. ¿Tendría disponibilidad el [Sugerir día, ej. Martes 30 de junio] a las 10:00 AM?

Quedo atento a su confirmación y a sus comentarios.

Saludos cordiales,

**Víctor Vilches**  
[Tu Cargo / SUPCON Chile]  
[Contacto / Teléfono]  

***
