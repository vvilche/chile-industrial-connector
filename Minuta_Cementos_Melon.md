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
    *   **PLC MOLINO 21 y PLC MOLINO 22:** Controladores **Quantum (140CPU65150 y 140CPU65160)** que utilizan módulos Ethernet **140NOE771** y cuentan con buses de campo **Profibus** para la integración de instrumentación y de los sistemas de protección de motores **TeSys T (LTMR27)**.
*   **Otras Áreas de Control Mapeadas:**
    *   **PLC M18-M19** (con migración pendiente de `PLC OLDM18` Quantum a M580).
    *   **PLC M17:** Integra una isla de E/S remotas mediante módulo **BMXCRA31200 / CRP 31200**.
    *   **PLC SECADOR:** Asociado a un switch local Moxa EDS208ST.
    *   **PLC HUMECTAC** (Humectación, Modicon M340 con CPU `BMXP342020`).
    *   **PLC DASH** (Tablero auxiliar, Modicon M340 con CPU `BMXP342020`).
    *   **PLC ENV1 (Envasadora 1) y PLC ENV2 (Envasadora 2 / Silo 28):** Equipados con módulos **NOE 77100**.
    *   **PLC VALVULAS SILOS 3000 y PLC SILOS 2000:** Módulos Ethernet **NOE 77100**.
    *   **PLC MEDIDORES ELÉCTRICOS LCA:** Concentra la telemetría eléctrica mediante módulos Ethernet **NOE77101**, operando en la subred de medidores (`192.168.10.0`) y la red de control VTS (`10.180.0.0`).
*   **Servidores de Datos:**
    *   **SERVIDOR API-NODE H9 PI LA CALERA:** Servidor concentrador de datos para el sistema de información e historial de planta (OSIsoft PI System) en la zona H9.

### B. Capa de Red e Infraestructura de Comunicaciones
*   **Switches Core de Planta:** La red principal está soportada por switches industriales Moxa de alta capacidad de la serie **IKS (Moxa IKS6726-2GTXSFP/2IM6700A)** en configuración de redundancia y switches Cisco **SF300-48**.
*   **Switches de Distribución / Anillo (DRS):** Se utilizan switches Schneider/Telemecanique de la serie **TCSESM (TCSESM63F2CU1C y TCSESM083F2CS0)** configurados con anillos redundantes y segmentación mediante VLANs (Master Ring VLAN y Slave Ring VLAN).
*   **Medio de Transmisión:** Enlaces de Fibra Óptica (FO) multimodo/monomodo y cableado de cobre Ethernet.

---

## 3. Identificación de Puntos de Dolor y Oportunidades para SUPCON

### Oportunidad 1: Solución al Problema de Medición de Flujo (Bypass / Purga de Horno)
*   **El Problema Operativo:** El cliente utilizaba un medidor de gas/aire de dispersión térmica modelo **E-T-A FC01-CA** instalado en una línea de **1" (DN25)** con presión máxima de **100 mBar** y salida **4-20 mA**. El equipo se dañó mecánicamente debido a una caída accidental de personal. La tubería transporta gas/aire expuesto directamente a **alta temperatura, polvo altamente abrasivo (CKD - Cement Kiln Dust) y concentraciones corrosivas de Cloro**.
*   **El Diagnóstico de SUPCON:** Los medidores de dispersión térmica de inserción tradicionales presentan sondas expuestas y delgadas que se doblan o rompen con facilidad ante impactos mecánicos. Asimismo, el Cloro ataca químicamente al acero inoxidable estándar (316L) y el polvo abrasivo de horno (CKD) se acumula en el sensor caliente, actuando como aislante y falseando la lectura de flujo.
*   **Solución y Alternativas Tecnológicas de SUPCON:**
    1.  **Alternativa 1 (Reemplazo Directo Reforzado): Medidor de Masa Térmica In-line SUPCON (Serie SRF-I)**  
        Un medidor térmico integrado en un cuerpo sólido de tubería bridada de 1" con carcasa robusta de aluminio fundido IP67. La sonda sensor se suministra en **Hastelloy C-276** (inmune a la corrosión por Cloro) o con **recubrimiento cerámico** contra la abrasión del CKD. Soporta flujos ultra-bajos desde 0.1 m/s.
    2.  **Alternativa 2 (La Recomendada - Máxima Robustez Mecánica y de Proceso): Tubo Venturi 1" + Transmisor de Presión Diferencial SUPCON CXT**  
        Se instala un tubo Venturi o placa de orificio compacta en la tubería de 1" (sin partes móviles ni elementos internos que puedan romperse o incrustarse de polvo). El **transmisor de presión diferencial SUPCON CXT se monta de forma remota** en un soporte protegido, totalmente a salvo de golpes por caída de personal y fuera del contacto directo con el gas corrosivo.
    3.  **Alternativa 3 (Alta Temperatura): Medidor Vortex In-line SUPCON (Serie SFV-I)**  
        Medidor de 1" en línea sin partes móviles y con el cristal piezoeléctrico sellado tras una pared de acero. Resistente al CKD y soporta altas temperaturas, pero requiere un caudal mínimo para generar vórtices.

---

### Oportunidad 2: Reemplazo del Sistema Experto (FLSmidth PXP)
*   **El Diagnóstico:** El plano confirma la existencia de dos servidores dedicados para el sistema experto: `SERVIDOR PXP HORNO` y `SERVIDOR PXP MOLINOS`. Ante la pérdida de licencias de FLSmidth PXP, Cementos Melón requiere una alternativa de optimización experta.
*   **Solución SUPCON:** Ofrecer la suite de Control Avanzado de Procesos **SUPCON APC-Cement** (con módulos de control predictivo multivariable - MPC - para la optimización del horno/enfriador y de los Molinos 21/22). Esta solución se instala a nivel de servidores y se conecta mediante OPC UA con el SCADA ECS e históricos de planta, logrando mejoras de t/h y consumo energético sin necesidad de reprogramar la lógica de control de los PLCs.

---

### Oportunidad 3: Vulnerabilidad de Red - Anillo de Fibra Óptica Roto
*   **El Diagnóstico:** El plano documenta la falta del tramo de fibra óptica entre la Sala de Cal y la Sala CAS (`"TRAMO FALTANTE FIBRA OPTICA SALA CAL Y SALA CAS"`). Esto rompe la redundancia física de la red de control.
*   **Solución SUPCON:** Ofrecer el diseño, canalización y tendido del tramo de fibra óptica faltante, cerrando físicamente el anillo de la red de control e integrando switches gestionados de SUPCON con protocolo de recuperación redundante rápido (<20 ms).

---

## 4. Plan de Acción Comercial y de Ingeniería

1.  **Presentación Técnica del Dashboard y Propuestas:** Utilizar el archivo interactivo `dashboard_calera.html` para presentar visualmente a Cementos Melón el catastro de sus activos, el diagnóstico detallado de las pasarelas Link150 del horno, la propuesta de cierre de anillo de fibra, y las alternativas de reemplazo para el flujómetro FC01-CA.
2.  **Visita Técnica a Terreno:** Inspeccionar el punto de instalación del medidor de flujo de 1" de H9 para validar la factibilidad del montaje remoto del transmisor DP SUPCON CXT (Alternativa 2) o del medidor térmico robusto (Alternativa 1).

---

## 5. Propuesta de Correo de Respuesta para el Cliente (Refinada con Alternativas de Flujo)

***

**Asunto:** Propuestas de Optimización, Redundancia de Red e Instrumentación de Flujo para Bypass - Planta La Calera Melón

Estimado [Nombre del Contacto],

Junto con saludar, y agradeciendo la información técnica provista y el plano **"RedControl LCA_Rev0"**, nuestro equipo de aplicaciones de instrumentación y control ha elaborado una propuesta dedicada para abordar sus desafíos de automatización en la Planta La Calera.

En particular, hemos analizado el caso del reemplazo de su medidor de aire/gas **E-T-A modelo FC01-CA de 1"**, el cual sufrió daños por un impacto mecánico externo en una línea que opera a baja presión (**100 mBar**) y que, por su conexión, está expuesta a condiciones muy severas de alta temperatura, polvo abrasivo (**CKD**) y concentraciones corrosivas de **Cloro**.

En **SUPCON** proponemos dos soluciones tecnológicas de alta gama que superan las limitaciones de robustez física y química del instrumento anterior, manteniendo la salida de lazo de corriente de **4-20 mA**:

1.  **Alternativa 2 (Recomendada por Robustez Física y de Proceso): Sistema de Presión Diferencial (Tubo Venturi 1" + Transmisor de Presión Diferencial SUPCON CXT)**  
    Esta es la solución más robusta del mercado. Consiste en instalar un elemento primario Venturi de acero sólido en la línea (sin partes móviles ni sensores internos expuestos a la incrustación del CKD o ataque químico del cloro). El **Transmisor de Presión Diferencial SUPCON CXT se monta de forma remota** en una zona de soporte protegida. Esto elimina al 100% el riesgo de daño físico por impacto o caídas accidentales de personal, y aísla la electrónica sensible de la zona corrosiva.
2.  **Alternativa 1 (Reemplazo Directo de Alta Sensibilidad): Medidor de Masa Térmica In-Line SUPCON (Serie SRF-I)**  
    Si se requiere mantener el principio de medición térmica para registrar caudales extremadamente bajos, proponemos nuestro medidor en línea de 1" bridadizado. A diferencia de las sondas de inserción tradicionales, este cuerpo bridado es altamente resistente a impactos mecánicos. Para soportar el cloro y la abrasión del CKD, el elemento sensor se suministra con **vaina de Hastelloy C-276** y recubrimiento cerámico protector, garantizando una vida útil muy superior a la del sensor original.

Asimismo, queremos aprovechar esta oportunidad para reiterarles nuestro apoyo en dos proyectos críticos identificados en su arquitectura:
*   **Reemplazo del Sistema Experto (FLSmidth PXP):** Ofrecemos nuestra suite de control avanzado **SUPCON APC-Cement** para optimizar el horno H9 y los Molinos 21/22 (soportados por PLCs Quantum y M580), permitiendo una transición suave ante el vencimiento de sus licencias PXP actuales.
*   **Cierre de Anillo de Comunicaciones:** Ponemos a su disposición nuestra ingeniería y suministro para completar el **"Tramo Faltante de Fibra Óptica entre la Sala Cal y la Sala CAS"** documentado en su plano, restituyendo la redundancia física y la tolerancia a fallas de su red de control.

Para revisar estas alternativas en detalle, le propongo agendar una breve videoconferencia técnica de 30 minutos para el próximo Martes a las 10:00 AM. ¿Le acomoda esa alternativa?

Quedo muy atento a sus valiosos comentarios.

Saludos cordiales,

**Víctor Vilches**  
[Tu Cargo / SUPCON Chile]  
[Contacto / Teléfono]  

***
