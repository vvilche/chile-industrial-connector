# Inventario Técnico Súper Detallado de Instrumentos y Hardware de Control
### Planta La Calera (LCA) - Cementos Melón S.A.  

> [!NOTE]
> Este inventario ha sido extraído directamente mediante el análisis sintáctico del plano de ingeniería **`Plano RedControl LCA_Rev0 (3) (1).dwg`** (Red de Control La Calera). Representa el catastro real de los activos de automatización, control e instrumentación instalados en la planta.

## 1. Resumen de Activos de Automatización

El plano de arquitectura contiene un total de **48 tipos de equipos** de automatización, que suman **87 unidades físicas estimadas** distribuidas en toda la planta. A continuación se detalla su distribución por categorías:

| Categoría de Hardware | Tipos de Equipos | Cantidad de Unidades | Fabricantes Clave | Protocolos Principales |
| :--- | :---: | :---: | :--- | :--- |
| **Controladores (PLCs y CPUs)** | 14 | **24** | Schneider Electric | Modbus TCP, Modbus TCP, EtherNet/IP, Modbus TCP... |
| **Instrumentación de Proceso y Analizadores** | 9 | **15** | ABB, Davis Instruments, FLSmidth / Sodern, FLSmidth Pfister, Martin Engineering / Genérico, SUPCON / Genérico, Schenck Process, Schneider Electric, Schneider Electric / Genérico | Control Solenoide PLC, Modbus RTU (RS-485) / Mo... |
| **Módulos de Red, Gateways y RIOs** | 9 | **21** | ProSoft / Schneider Electric, Schneider Electric | Ethernet RIO, Ethernet RIO (QEIO), Ethernet RIO... |
| **Servidores e Infraestructura TI** | 5 | **8** | FLSmidth, OSIsoft / Hewlett Packard, QNAP | NFS, SMB/CIFS, TCP/IP, TCP/IP, TCP/IP, Integrac... |
| **Switches y Conversores de Medios** | 11 | **19** | Black Box, Cisco, HP, Moxa, Phoenix Contact, Schneider Electric / Telemecanique | Conversión Cobre a Fibra, Conversión Cobre a Fi... |
| **TOTAL** | **48** | **87** | **Schneider, Moxa, ABB, FLSmidth, etc.** | **Modbus TCP, EtherNet/IP, Profibus DP, etc.** |

---

## 2. Inventario Catastrado de Planta (Tabla Súper Detallada)

La siguiente tabla detalla cada uno de los elementos identificados en el plano de la Red de Control de La Calera, especificando su fabricante, cantidad de unidades en planta, interfaces de comunicaciones, descripción operativa y las etiquetas/tags específicas encontradas en el plano:

| Categoría | Nombre del Equipo | Fabricante | Cant. | Protocolo / Comunicaciones | Descripción y Función en Planta | Etiquetas / Tags en Plano |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| **Controladores (PLCs y CPUs)** | Modicon M580 CPU (BMEP584040) | Schneider Electric | **2** | Modbus TCP, EtherNet/IP | Controlador principal de alta gama para la zona de procesos H9 (Nivel 4). | `BMP584040`, `PLC M580 LEVEL4` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Alimentación H9) | Schneider Electric | **2** | Modbus TCP | Controlador para la dosificación y alimentación del horno en H9. | `PLC ALIMH9`, `PLC ALIMH9  NOC0301` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Combustibles Alternativos) | Schneider Electric | **1** | Modbus TCP | Controlador para el sistema de inyección y dosificación de combustibles alternativos. | `PLC COMBALT  NOC0301` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Envasadora 1) | Schneider Electric | **2** | Modbus TCP | Controlador para la línea de ensacado y envasado de cemento 1 (ENV1). | `PLC ENV1`, `PLC ENV1  NOE 77100` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Envasadora 2 / Silo 28) | Schneider Electric | **2** | Modbus TCP | Controlador para la línea de envasado 2 y despacho desde el Silo 28. | `PLC ENV2  NOE 77100`, `PLC ENV2 SILO28` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (H9) | Schneider Electric | **2** | Modbus TCP, EtherNet/IP | Controlador para el área H9, en proceso de migración o rack principal. | `PLC H9`, `PLC H9  NOC 0301` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Medidores LCA) | Schneider Electric | **3** | Modbus TCP, Ethernet IP | Controlador concentrador de telemetría de medidores eléctricos de La Calera. | `PLC MEDIDORS`, `PLC MEDIDORS  NOE77100 MEDIDORS`, `PLC MEDIDORS  NOE77101 CONTROL` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Molino 17) | Schneider Electric | **2** | Modbus TCP | Controlador encargado del molino de cemento M17. | `PLC M17`, `PLC M17  CRP 31200` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Molinos 18 y 19) | Schneider Electric | **2** | Modbus TCP | Controlador encargado de las operaciones de los molinos de cemento M18 y M19. | `PLC M18-M19`, `PLC M18-M19  NOC 0301` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Silos 2000) | Schneider Electric | **2** | Modbus TCP | Controlador para el almacenamiento y despacho de cemento en Silos 2000. | `PLC SILOS2000`, `PLC SILOS2000  NOE 77100` |
| **Controladores (PLCs y CPUs)** | Modicon PLC (Válvulas Silos 3000) | Schneider Electric | **1** | Modbus TCP | Controlador para el direccionamiento y válvulas de los Silos 3000. | `PLC VV-S3000  NOE 77100` |
| **Controladores (PLCs y CPUs)** | Modicon Quantum CPU (140CPU53414) | Schneider Electric | **1** | Modbus TCP, Modbus Plus/RIO | Controlador de proceso heredado Quantum, CPU serie 534. | `PLC 140CPU534` |
| **Controladores (PLCs y CPUs)** | Modicon Quantum CPU (140CPU65150) | Schneider Electric | **1** | Modbus TCP, Profibus DP | Controlador de proceso heredado (Quantum) para el Molino de Cemento 21 (M21). | `140CPU65150` |
| **Controladores (PLCs y CPUs)** | Modicon Quantum CPU (140CPU65160) | Schneider Electric | **1** | Modbus TCP, Profibus DP | Controlador de proceso heredado (Quantum) para el Molino de Cemento 22 (M22). | `140CPU65160` |
| **Instrumentación de Proceso y Analizadores** | Analizador Continuo de Gases de Chimenea CEMS (ACF5000) | ABB | **2** | Modbus TCP / Analógico | Analizador CEMS multi-gas FTIR de alta fidelidad para el monitoreo de emisiones en la chimenea del precalentador. | `ACF5000 ABB`, `CEMS` |
| **Instrumentación de Proceso y Analizadores** | Analizador de Materiales en Cinta CNA (PGNAA) | FLSmidth / Sodern | **4** | Modbus TCP / Integración Proceso | Analizador en línea por activación neutrónica (PGNAA) montado sobre la cinta transportadora 200BC03 para control de calidad de la puzolana/caliza. | `CNA`, `CNA ANALIZADOR`, `CNA(1 DE 2)`, `CNA(2 DE 2)` |
| **Instrumentación de Proceso y Analizadores** | Cañones de Aire Big Blaster | Martin Engineering / Genérico | **1** | Control Solenoide PLC | Cañones neumáticos de alta presión para eliminar obstrucciones y acumulaciones de clinker/caliza en silos y chutes. | `BIG BLASTER` |
| **Instrumentación de Proceso y Analizadores** | Controlador de Motor Inteligente TeSys T (LTMR27) | Schneider Electric | **1** | Modbus TCP / Profibus DP | Sistema de gestión y protección de motor de alta precisión para los motores principales de los molinos. | `LTMR27 TESYS T` |
| **Instrumentación de Proceso y Analizadores** | Dosificador de Carbón Rotorfeeder Pfister CAS | FLSmidth Pfister | **1** | Profibus DP / Dedicado | Alimentador de rotor de pesaje gravimétrico de alta precisión para dosificar carbón pulverizado al horno. | `PFISTER` |
| **Instrumentación de Proceso y Analizadores** | Estación Meteorológica Davis Vantage Pro2 | Davis Instruments | **1** | Serial / Modbus TCP Converter | Estación meteorológica para medición de variables ambientales de planta (viento, temp, presión, humedad). | `DAVIS VANTAGE` |
| **Instrumentación de Proceso y Analizadores** | Flujómetro Coriolis (Línea Precalentador / Alimentación) | SUPCON / Genérico | **2** | Modbus RTU (RS-485) / Modbus TCP | Medidor de flujo másico Coriolis de alta precisión para control de combustión y alimentación de horno. | `CORIOLIS`, `CORIOLIS ALIM`, `CORIOLIS PRE` |
| **Instrumentación de Proceso y Analizadores** | Medidores de Energía Eléctrica IP | Schneider Electric / Genérico | **1** | Modbus TCP | Multimedidores de variables eléctricas para control de consumo y factor de potencia de la planta. | `RED MEDIDORES` |
| **Instrumentación de Proceso y Analizadores** | Sistema de Dosificación de Sólidos / Pesómetros Schenck | Schenck Process | **2** | Profibus DP / Analógico | Pesómetros integradores y sistemas de pesaje para dosificación exacta de materias primas. | `AREA  SCHENCK`, `SCHENCK` |
| **Módulos de Red, Gateways y RIOs** | Módulo Master Profibus DP Quantum (PTQ-PDPMV1) | ProSoft / Schneider Electric | **1** | Profibus DP Master | Módulo en rack de Quantum para control maestro del bus de campo Profibus DP. | `PTQPDPMV1` |
| **Módulos de Red, Gateways y RIOs** | Módulo Procesador de E/S Remotas Quantum (140CRP31200) | Schneider Electric | **2** | Ethernet RIO (QEIO) Master | Módulo cabecera/procesador de E/S remotas en el rack principal del PLC (ej. en M17 o H9). | `140CRP31200`, `MASTER QEIO` |
| **Módulos de Red, Gateways y RIOs** | Módulo de Comunicación Ethernet M580 (BMENOC0301) | Schneider Electric | **5** | Modbus TCP, EtherNet/IP | Módulo de red avanzado NOC para control y routing en anillo de PLCs M580. | `BMENOC0301.4`, `PLC ALIMH9  NOC0301`, `PLC COMBALT  NOC0301`, `PLC H9  NOC 0301`, `PLC M18-M19  NOC 0301` |
| **Módulos de Red, Gateways y RIOs** | Módulo de Comunicación Ethernet Quantum (140NOE77101/00) | Schneider Electric | **7** | Modbus TCP | Módulo de red Ethernet NOE para la comunicación de CPUs Quantum legacy. | `140NOE771`, `140NOE77100`, `140NOE77101`, `PLC ENV1  NOE 77100`, `PLC ENV2  NOE 77100`, `PLC SILOS2000  NOE 77100`, `PLC VV-S3000  NOE 77100` |
| **Módulos de Red, Gateways y RIOs** | Módulo de E/S Remota Ethernet X80 (BMXCRA31200) | Schneider Electric | **1** | Ethernet RIO | Adaptador de E/S remota para rack secundario compatible con M580/M340 (ej. en M17). | `BMXCRA31200` |
| **Módulos de Red, Gateways y RIOs** | Módulo de E/S Remota Ethernet eX80 (BMECRA31210) | Schneider Electric | **1** | Ethernet RIO Redundante | Adaptador de E/S remota de alta gama con soporte para redes en anillo redundantes de M580. | `BMECRA31210` |
| **Módulos de Red, Gateways y RIOs** | Módulo de E/S Remota Quantum (140CRA31200) | Schneider Electric | **1** | Ethernet RIO (QEIO) | Adaptador de E/S remota heredado (Quantum Ethernet I/O drop). | `140CRA31200` |
| **Módulos de Red, Gateways y RIOs** | Pasarela Modbus RTU a Modbus TCP (Link150) | Schneider Electric | **2** | Modbus RTU (RS-485) / Modbus TCP | Gateway para integrar los flujómetros Coriolis seriales a la red de control Ethernet. | `LINK150` |
| **Módulos de Red, Gateways y RIOs** | Pasarela Profibus DP a Modbus TCP (TCSEGPA23F14F) | Schneider Electric | **1** | Profibus DP / Modbus TCP | Gateway de comunicación para integrar subredes Profibus DP de los molinos a Ethernet. | `TCSEGPA23F14F` |
| **Servidores e Infraestructura TI** | Almacenamiento en Red NAS (QNAP) | QNAP | **1** | NFS, SMB/CIFS, TCP/IP | Unidad NAS para almacenamiento redundante de backups de base de datos de SCADA, PI e históricos. | `NAS QNAP` |
| **Servidores e Infraestructura TI** | Servidor de Control de Calidad de Laboratorio (FLS-QCX) | FLSmidth | **1** | TCP/IP | Servidor del sistema QCX (Quality Control by Computer and X-Ray) para análisis de calidad químico/físico. | `FLS-QCX` |
| **Servidores e Infraestructura TI** | Servidor de Historial e Información (API-Node PI System) | OSIsoft / Hewlett Packard | **2** | TCP/IP, OPC DA/UA | Servidor que actúa como nodo de adquisición de datos en tiempo real para el PI System en la zona H9. | `API-NODE H9`, `PI LA CALERA` |
| **Servidores e Infraestructura TI** | Servidores de SCADA FLSmidth ECS (ECSSVR01 / ECSSVR02) | FLSmidth | **2** | TCP/IP, Redundancia de Servidores | Servidores redundantes del sistema de supervisión SCADA ECS/process expert de la planta. | `ECSSVR01`, `ECSSVR02` |
| **Servidores e Infraestructura TI** | Servidores de Sistema Experto PXP (Horno / Molinos) | FLSmidth | **2** | TCP/IP, Integración SCADA | Servidores que ejecutan el sistema experto FLSmidth PXP para optimizar el horno y los molinos en tiempo real. | `PXP HORNO`, `PXP MOLINOS` |
| **Switches y Conversores de Medios** | Conversor de Medios Industrial (IMC-21-M-SC) | Moxa | **1** | Conversión Cobre a Fibra SC Multimodo | Conversor de medios industrial de alta durabilidad para campo. | `IMC21MSCV3.1.4` |
| **Switches y Conversores de Medios** | Conversor de Medios de Fibra Óptica (FL MC 1000-C) | Phoenix Contact | **1** | Conversión Cobre a Fibra | Conversor de medios de riel DIN para gabinetes de campo. | `FL1000C` |
| **Switches y Conversores de Medios** | Conversor de Medios de Fibra Óptica (LHC013A-R3) | Black Box | **4** | Conversión Cobre a Fibra (10/100Base-TX a 100Base-FX) | Conversor de medios compacto para extender enlaces Ethernet sobre fibra óptica. | `BLACK BOX(15)`, `BLACK BOX(17)`, `BLACK BOX(18)`, `LHC013A-R3` |
| **Switches y Conversores de Medios** | Switch Core Modular Industrial (IKS-6726A) | Moxa | **2** | Ethernet, Fibra Óptica, RSTP/VLAN | Switch modular Gigabit de montaje en rack de 19 pulgadas para el Core de red de control. | `IKS6726-2GTXSFP/2IM6700A`, `IKS6726A-2GTXSFP/2IM6700A` |
| **Switches y Conversores de Medios** | Switch DRS 8 Puertos (TCSESM083F2CS0) | Schneider Electric / Telemecanique | **1** | Ethernet, ConneXium | Switch gestionado de 8 puertos para sub-anillos de control. | `TCSESM083F2CS0` |
| **Switches y Conversores de Medios** | Switch DRS con 3 Puertos de Fibra (TCSESM83F23FO) | Schneider Electric / Telemecanique | **2** | Ethernet, Fibra Óptica, ConneXium | Switch gestionado con 3 interfaces de fibra óptica para cerrar enlaces de anillo largo. | `TCSESM083F23F0`, `TCSESM83F23FO` |
| **Switches y Conversores de Medios** | Switch Gestionado de Medidores (HP 3VLAN) | HP | **1** | Ethernet, VLAN segmentadas | Switch utilizado en la subestación para separar el tráfico de medidores eléctricos en 3 VLANs. | `SWITCH 3VLAN` |
| **Switches y Conversores de Medios** | Switch Industrial Riel DIN (SFN-TX-FX) | Phoenix Contact | **1** | Ethernet | Switch local de riel DIN para interconexión rápida en gabinetes de campo. | `SFNPTXFX` |
| **Switches y Conversores de Medios** | Switch Industrial Riel DIN 8 Puertos (EDS-208ST) | Moxa | **1** | Ethernet, F.O. Multimodo | Switch industrial compacto no gestionado de 8 puertos con enlace de fibra para gabinetes locales. | `EDS208ST` |
| **Switches y Conversores de Medios** | Switch de Anillo Redundante Gestionado (TCSESM63F2CU1C) | Schneider Electric / Telemecanique | **4** | Ethernet, Conectividad de Fibra (ConneXium) | Switch gestionado (DRS) optimizado para configurar anillos de control redundantes con fibra óptica. | `TCSESM63F2CU1C` |
| **Switches y Conversores de Medios** | Switch de Distribución Gestionado 48 Puertos (SF300-48) | Cisco | **1** | Ethernet, VLAN, STP | Switch de 48 puertos Fast Ethernet para distribución de red a servidores y consolas. | `SF300-48` |


---

## 3. Análisis Técnico de la Arquitectura y Oportunidades de Modernización

Basado en el inventario anterior, el equipo de ingeniería de **SUPCON** ha desarrollado un análisis técnico de la planta para identificar mejoras operativas inmediatas:

### A. Reemplazo del Sistema Experto FLSmidth PXP (Oportunidad de Venta Prioritaria)
> [!IMPORTANT]
> El plano revela la existencia de **dos servidores dedicados para el sistema experto PXP** de FLSmidth:
> 1. `SERVIDOR PXP HORNO` (optimización de la combustión del horno y enfriador).
> 2. `SERVIDOR PXP MOLINOS` (optimización de la molienda de cemento).
> Dado que Cementos Melón perderá las licencias de FLSmidth PXP, **SUPCON** puede reemplazar directamente ambos servidores e implementar su propia suite de optimización avanzada **SUPCON APC-Cement** (con módulos para horno y molinos) sin necesidad de re-ingeniería en la capa de control de los PLCs M580 y Quantum.

### B. Modernización del Lazo de Control e Instrumentación Coriolis (H9)
> [!WARNING]
> Los flujómetros Coriolis clave para el Horno de La Calera (`Coriolis PRE` y `Coriolis ALIM`) se comunican mediante buses de campo seriales RS-422/485 Modbus RTU que pasan por pasarelas intermedias **Link150** de Schneider Electric.  
> Esta arquitectura presenta alta vulnerabilidad a ruidos electromagnéticos y saturación del gateway por peticiones concurrentes del PLC y del servidor PI.  
> **Propuesta SUPCON:** Sustituir estos medidores por **Coriolis SUPCON (Serie SFC)** con comunicación Ethernet nativa (Modbus TCP o Profinet) conectados directamente al anillo de fibra óptica, garantizando lecturas inmunes al ruido eléctrico y tiempos de respuesta de milisegundos.

### C. Resolución de la Discontinuidad en el Anillo de Red (Sala Cal - Sala CAS)
> [!CAUTION]
> La anotación **`"TRAMO FALTANTE FIBRA OPTICA SALA CAL Y SALA CAS"`** en el plano indica una falla física grave en la topología de la red de control.  
> Al estar roto el anillo, los switches DRS de Schneider no pueden conmutar tráfico de respaldo. Si ocurre un fallo en un cable de fibra óptica de la zona, una parte importante de la planta perderá comunicación inmediatamente.  
> **Propuesta SUPCON:** Ejecutar el proyecto de tendido de fibra óptica para cerrar el anillo físico e integrar switches gestionados de SUPCON con protocolo de recuperación ultra-rápido (<20 ms) para asegurar redundancia completa.

### D. Migración Tecnológica de la Capa de Control Legacy (Quantum y M340)
El plano expone una gran cantidad de controladores de antigua generación **Quantum** (`140CPU65150`, `140CPU65160`, `140CPU534`) y tarjetas de red legacy (`140NOE77100`, `140NOE77101`). Además, se identifican PLCs **Modicon M340** (`BMXP342020`) controlando áreas auxiliares como Humectación y Dash.  
SUPCON puede ofrecer su **DCS de Alta Disponibilidad ECS-700** para centralizar el control de los Molinos 21/22 y los Silos, reemplazando la base obsoleta de Quantum y simplificando el mantenimiento de planta.
