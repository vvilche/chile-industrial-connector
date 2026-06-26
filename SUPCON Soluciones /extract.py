import os
import re
import json

# File paths
PPTX_PATH = "/Users/victorvilche/.gemini/antigravity/scratch/Conecta-Web-Corporativa/recursos_supcon/Field Devices-Supcon.pptx.txt"
CATALOG_PATH = "/Users/victorvilche/.gemini/antigravity/scratch/Conecta-Web-Corporativa/recursos_supcon/parsed_catalog.txt"
OUTPUT_PATH = "productos.json"

# Key translations for specifications
KEY_TRANSLATIONS = {
    "Nominal Diameter": "diámetro_nominal",
    "Pressure Rating": "presión_rating",
    "Seat Leakage Rate": "fuga_asiento",
    "Seat Leakage": "fuga_asiento",
    "Flow characteristic": "característica_flujo",
    "Accuracy": "precisión",
    "Highest accuracy": "precisión_máxima",
    "Long-term stability": "estabilidad_largo_plazo",
    "Annual capacity": "capacidad_anual",
    "Measurement range": "rango_medición",
    "measuring range": "rango_medición",
    "Repeatability": "repetibilidad",
    "Beam angle": "ángulo_haz",
    "Blind area": "zona_muerta",
    "High conversion accuracy": "precisión_conversión",
    "low temperature drift": "deriva_térmica",
    "Maximum accuracy of signal": "precisión_señal",
}

# Value translations in specifications
VALUE_TRANSLATIONS = {
    "Equal percentage(%)": "Porcentaje igual (%)",
    "Linear(L)": "Lineal (L)",
    "Quick opening(Q)": "Apertura rápida (Q)",
    "Quick opening (Q)": "Apertura rápida (Q)",
    "Approximate Linear": "Lineal aproximado",
    "Approximate Equal Percentage": "Porcentaje igual aproximado",
    "Bidirection zero Leakage": "Fuga cero bidireccional",
    "Zero Leakage": "Fuga cero",
    "Bubble Tight Shut Off": "Cierre hermético a burbujas",
    "Friction and Wear Free": "Libre de fricción y desgaste",
    "Double Eccentric Structure": "Estructura de doble excentricidad",
    "Triple-Offset": "Triple excentricidad",
    "Slurry Working Conditions": "Condiciones de trabajo con lodos",
    "Equal percentage": "Igual porcentaje",
    "equal percentage": "igual porcentaje",
    "linear": "lineal",
    "quick opening": "apertura rápida",
    "Class Ⅳ / Ⅴ/ Ⅵ": "Clase Ⅳ / Ⅴ / Ⅵ",
    "Class Ⅴ/ Ⅵ": "Clase Ⅴ / Ⅵ",
    "Class Ⅳ / Ⅴ/ Ⅵ.": "Clase Ⅳ / Ⅴ / Ⅵ",
    "Class Ⅴ/ Ⅵ.": "Clase Ⅴ / Ⅵ",
    "Class Ⅳ": "Clase Ⅳ",
    "Class Ⅴ": "Clase Ⅴ",
    "Class Ⅵ": "Clase Ⅵ",
    "Class IV": "Clase IV",
    "Class V": "Clase V",
    "Class VI": "Clase VI",
}

# Certificate translations
CERTIFICATE_TRANSLATIONS = {
    "CE": "CE",
    "ATEX Ex-proof": "ATEX (Antideflagrante)",
    "ISO 15848 Fugitive Emission (TUV)": "ISO 15848 Emisiones Fugitivas (TUV)",
    "API 6FA Fire Safe (TUV)": "API 6FA Seguridad contra Incendios (TUV)",
    "API 607 & API 6FA Fire Safe (TUV)": "API 607 y API 6FA Seguridad contra Incendios (TUV)",
    "SIL 3 (TUV)": "SIL 3 (TUV)",
    "SIL 3(TUV)": "SIL 3 (TUV)",
    "BV SIL3": "SIL 3 (BV)",
    "SIL3 (BV)": "SIL 3 (BV)",
    "SIL3 (CNAS)": "SIL 3 (CNAS)",
    "CE (EMC)": "CE (EMC)",
    "CE[EMC]": "CE (EMC)",
    "CE[LVD]": "CE (LVD)",
    "G3 anti-corrosion": "Protección contra corrosión G3",
    "EAC": "EAC",
    "PAC": "PAC",
    "ROHS": "RoHS",
    "ATEX & IECEx Ex d & Exia (BV)": "ATEX e IECEx Ex d y Ex ia (BV)",
    "ATEX & IECEx Exia (BV)": "ATEX e IECEx Ex ia (BV)",
    "SIL2 (BV)": "SIL 2 (BV)",
    "Ex d certified by Chinese Certification Body": "Certificación Ex d (Organismo Chino)",
    "Ex ia & Ex d certified by National Certification Body": "Certificación Ex ia y Ex d (Organismo Nacional)",
    "SIL2 (ECM)": "SIL 2 (ECM)",
    "CE (B+C)": "CE (B+C)",
    "IECEx/ATEX": "IECEx/ATEX",
    "CCS": "CCS",
    "Intrinsically Safe/CCC": "Seguridad Intrínseca (CCC)",
    "SIL2/3": "SIL 2/3",
}

# Complete fallback definitions in Spanish for all 34 products
FALLBACK_DEFAULTS = {
    "ln81": {
        "name": "Válvula de control neumática de globo de asiento simple SUPCON serie LN81",
        "description": "Válvula neumática de control de presión, con dos núcleos básicos de válvula de émbolo guía, tipo de compresión de manguito flotante, estructura de asiento, diseño modular, gran capacidad de flujo, alta precisión de control, rango ajustable, permite un control de flujo mínimo, estructura simple, confiable, buen rendimiento de sellado y fácil mantenimiento. Es adecuada para pequeñas diferencias de presión, fugas en el asiento y alta precisión de control.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "ln82": {
        "name": "Válvula de control neumática de globo de asiento simple serie LN82",
        "description": "La serie LN82 es un producto con estructura de desequilibrio de presión de la serie LN8. Se basa en dos componentes básicos: buje y asiento de doble dirección. Ofrece capacidad de flujo, buena estabilidad dinámica, diseño de núcleo de válvula de cilindro poroso, que permite una separación adecuada en la superficie de sellado. Esta superficie no se ve afectada por la erosión directa a alta velocidad, y su rendimiento de sellado es bueno y confiable, previniendo la formación de rebabas, la cavitación y el ruido. Su propósito es proporcionar un medio de limpieza rápida, adecuado para la velocidad, especialmente para el control de alta diferencia de presión en gases.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "ln83": {
        "name": "Válvula de control de globo con guía de jaula serie LN83",
        "description": "Las válvulas de control de globo con guía de jaula serie LN83 son válvulas de jaula de control de equilibrio de presión de un solo asiento de la serie LN8, una de las tres válvulas de base más grandes. Utilizan manguitos separados, una estructura de guía de gran tamaño, un anillo de sellado de equilibrio de presión y un anillo de sellado no metálico de alto rendimiento. Ofrecen buena estabilidad dinámica, alta precisión de control, permiten grandes diferencias de presión, una pequeña fuerza de operación y un gran caudal. Son adecuadas para condiciones de trabajo de temperatura normal, presión diferencial y control de tensión alterna.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "ln85": {
        "name": "Válvula de control de globo con guía de jaula serie LN85",
        "description": "La serie LN85 es una válvula de asiento simple con equilibrio de presión de la serie LN8. Una de sus tres características básicas es el manguito separable, la estructura de guía de gran tamaño, el resorte moldeado y el anillo de equilibrio de presión con almacenamiento de energía. Presenta buena estabilidad dinámica, alta precisión de control, admite grandes diferencias de presión, baja fuerza de operación, gran capacidad de flujo y es adecuada para un amplio rango de temperaturas y grandes diferencias de presión, bajo la acción del control de tensión alterna.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "ln87": {
        "name": "Válvula de control de globo con guía de jaula serie LN87",
        "description": "La serie LN87 son productos de válvulas de un solo asiento con equilibrio de presión de la serie LN8, uno de los tres manguitos guía básicos, válvulas de un solo asiento de tipo equilibrio de presión, con estructura de manguito separado, sello de pistón de metal de alto rendimiento, tiene buena estabilidad dinámica, alta precisión de control, permite que la diferencia de presión sea grande, la fuerza de operación es pequeña, gran capacidad de flujo, un rango más amplio de temperatura aplicable, etc. Adecuado para el control de fluidos en duras condiciones de trabajo.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "ln81w": {
        "name": "Válvula de control de globo con fuelle serie LN81W",
        "description": "La válvula de control de fuelle de un solo asiento serie LN81W/82, basada en la estructura de la válvula de un solo asiento sin equilibrio de presión de la serie LN81/82, se basa en un sello de fuelle reforzado, fuelle elástico de acero inoxidable de compresión en las piezas del cojinete conectadas al vástago de la válvula y empaquetadura de doble sello, lo que elimina las fugas del fluido. Es adecuada para presiones diferenciales altamente tóxicas, inflamables, explosivas, volátiles y para el ajuste de fluidos con metales raros y preciosos.",
        "features": ["Nueva modularización funcional", "Alta precisión de control", "Funcionamiento confiable", "Fácil mantenimiento"]
    },
    "sn51-52": {
        "name": "Válvula de bola tipo O con sello blando serie SN51/52",
        "description": "La válvula de bola tipo O con sello blando de la serie Sn51/52 es una válvula de bola de paso recto completo, la pérdida de caída de presión del fluido es la más pequeña, excelente rendimiento de corte, la bola solo necesita girar 90 grados para lograr la válvula completamente abierta o cerrada, al mismo tiempo con el vástago de la válvula volando, antiestático y otras funciones.",
        "features": ["Excelente rendimiento de corte y sellado", "Bajo torque", "Fuga cero", "Alta resistencia al desgaste"]
    },
    "sn53-54": {
        "name": "Válvula de bola tipo O con sello metálico serie SN53/54",
        "description": "La válvula de bola tipo O de sellado rígido serie Sn53/54 es una válvula de tamaño completo con excelente rendimiento de sellado, acción sensible sin adherencias, prevención esencial de incendios y alivio seguro de presión en la cámara intermedia. Es adecuada para fluidos con partículas fijas y lodos a diferentes temperaturas y presiones.",
        "features": ["Excelente rendimiento de corte y sellado", "Bajo torque", "Fuga cero", "Alta resistencia al desgaste"]
    },
    "sn5100f": {
        "name": "Válvula de bola tipo O con revestimiento de plástico SN5100F",
        "description": "Las válvulas de bola con revestimiento de plástico de la serie SN5100F ofrecen una excelente resistencia a la corrosión y están separadas de las piezas en contacto con el fluido mediante fluoroplástico. El PTFE y el FEP se utilizan principalmente como fluoroplásticos. Se utilizan generalmente en situaciones donde los requisitos de sellado son elevados y los fluidos altamente corrosivos se pueden abrir y cerrar de forma fiable.",
        "features": ["Excelente rendimiento de corte y sellado", "Bajo torque", "Fuga cero", "Alta resistencia al desgaste"]
    },
    "vn6": {
        "name": "Válvula de control de bola con muesca en V de la serie VN6",
        "description": "La válvula de control de bola con muesca en V de la serie VN6 cuenta con un núcleo de bola de incisión en forma de V que proporciona una característica de flujo de porcentaje aproximadamente igual. El ángulo del núcleo aumenta significativamente la relación de flujo ajustable. Con una combinación elástica única y labio en la estructura del asiento de sellado, ofrece excelentes funciones de corte para medios de fibra y partículas, siendo especialmente adecuada para sistemas de control de gran relación de ajuste.",
        "features": ["Excelente rendimiento de corte y sellado", "Bajo torque", "Fuga cero", "Alta resistencia al desgaste"]
    },
    "cn81": {
        "name": "Válvula de control rotativa excéntrica SUPCON serie CN81",
        "description": "La válvula rotativa excéntrica serie CN8 cuenta con un núcleo de válvula ubicado en la superficie de la tapa esférica y una estructura de cuerpo de corredor recto de una sola pieza. El centro rotatorio no es concéntrico con el eje de rotación, lo que reduce el desgaste del asiento y prolonga su vida útil. Ofrece excelente estabilidad, resistencia a la erosión y la corrosión, un sellado confiable y amplias ventajas de ajuste de caudal.",
        "features": ["Estructura de doble excentricidad", "Gran rangeabilidad", "Alta capacidad de flujo", "Anti-cavitación y anti-erosión"]
    },
    "bn": {
        "name": "Válvula de mariposa de triple excentricidad serie BN",
        "description": "Una válvula de mariposa de triple excentricidad es un tipo especializado de válvula de mariposa, diseñada para proporcionar un cierre fiable y hermético en aplicaciones de alta presión y alta temperatura. Se denomina \"triple excentricidad\" porque su mecanismo de sellado incluye tres excentricidades distintas en su diseño.",
        "features": ["Libre de fricción y desgaste", "Sellado por torque, cierre hermético a burbujas", "Rendimiento superior bajo altas o bajas temperaturas y presiones"]
    },
    "bn1101f": {
        "name": "Válvula de mariposa con revestimiento de plástico BN1101F",
        "description": "Las válvulas de mariposa con revestimiento de plástico de la serie BN1101F ofrecen la resistencia térmica de las válvulas de revestimiento duro y las características de sellado de las de revestimiento blando. Al funcionar, solo el asiento de plástico perfluorado y la placa de mariposa con revestimiento de flúor están en contacto con el fluido.",
        "features": ["Libre de fricción y desgaste", "Sellado por torque, cierre hermético a burbujas", "Rendimiento superior bajo altas o bajas temperaturas y presiones"]
    },
    "cxt": {
        "name": "Transmisor de presión inteligente de alta precisión serie CXT",
        "description": "Los transmisores de presión inteligentes de alta precisión de la serie CXT utilizan un chip sensor compuesto de silicio monocristalino de alto rendimiento, una estructura de cápsula integrada avanzada y un diseño de circuito modular altamente confiable para garantizar un rendimiento superior y una estabilidad a largo plazo.",
        "features": ["Precisión de ±0.05%, máxima precisión de ±0.035%", "Estabilidad a largo plazo de ±0.1% por 10 años", "Soluciones personalizadas para procesos especiales"]
    },
    "cjt": {
        "name": "Transmisor de presión inteligente serie CJT",
        "description": "El transmisor de presión inteligente de la serie CJT es un instrumento de presión inteligente (presión diferencial) con función de comunicación HART, desarrollado utilizando la tecnología de sensor capacitivo de micro desplazamiento. Aplicable a la medición de presión, flujo y nivel de líquido en petróleo, energía eléctrica, industria química, metalurgia y farmacia.",
        "features": ["Precisión de ±0.05%, máxima precisión de ±0.035%", "Estabilidad a largo plazo de ±0.1% por 10 años", "Soluciones personalizadas para procesos especiales"]
    },
    "sfm800": {
        "name": "Caudalímetro másico SFM800",
        "description": "Los medidores de caudal másico de líquidos están diseñados para aplicaciones de medición de caudal de alta gama. Cumplen con los estándares de verificación de rendimiento internacionales y ofrecen un excelente rendimiento en la medición de caudal y densidad.",
        "features": ["Medición directa de caudal másico y densidad", "Alta precisión y estabilidad", "Cumplimiento de estándares de la UE y Rusia"]
    },
    "sf20": {
        "name": "Rotámetro de tubo metálico SF20",
        "description": "El rotámetro de tubo metálico es un instrumento de caudal de área variable, comúnmente utilizado en la automatización industrial. Es compacto, con un amplio rango de medición y fácil de usar, ideal para medir el caudal de líquidos, gases y vapor en condiciones de baja tasa de flujo o medios corrosivos.",
        "features": ["Diseño compacto de área variable", "Apto para caudales pequeños y bajas temperaturas", "Adecuado para medios corrosivos y no conductores"]
    },
    "lugb": {
        "name": "Medidor de caudal de vórtice LUGB",
        "description": "Presenta un diseño robusto que resiste vibraciones mecánicas, impactos y contaminación. Sin piezas móviles y con un desgaste mínimo, no requiere mantenimiento mecánico. El medidor ofrece baja pérdida de presión, alta precisión y fácil instalación.",
        "features": ["Baja pérdida de presión", "Alta precisión sin partes móviles", "Sensor y convertidor libremente combinables"]
    },
    "sfe900": {
        "name": "Caudalímetro electromagnético SFE900",
        "description": "El caudalímetro electromagnético SFE900 es un producto de alta precisión y fiabilidad, gracias a su continua actualización y mejora. Este caudalímetro destaca en tecnología de excitación, tecnología de revestimiento y tecnología inteligente.",
        "features": ["Mide líquidos con conductividad tan baja como 2 μS/cm", "Rango de medición de 0.1 a 12 m/s", "Excitación por onda de baja frecuencia de tres estados"]
    },
    "emf89": {
        "name": "Caudalímetro electromagnético EMF89",
        "description": "Utiliza técnicas de fabricación avanzadas para garantizar la calidad del sensor. Emplea una CPU dedicada de alta velocidad y tecnología avanzada de procesamiento de señales para un rendimiento estable y alta fiabilidad en diversas condiciones de funcionamiento.",
        "features": ["Procesamiento de señal avanzado para alta estabilidad", "Diversos materiales de electrodos y revestimientos", "Modelos integrados, divididos y sanitarios"]
    },
    "sl20": {
        "name": "Transmisor de nivel de flotador SL20",
        "description": "El transmisor de nivel de flotador SL20 muestra las mediciones in situ y convierte los cambios de nivel en una señal de salida estándar de 4-20 mA. Es ideal para industrias como la petrolera, química y metalúrgica.",
        "features": ["Visualización in situ y transmisión remota", "Alimentado por sistema de dos hilos", "Ideal para medición en tiempo real en línea"]
    },
    "sl10": {
        "name": "Medidor de nivel magnético SL10",
        "description": "El medidor de nivel magnético SL10 permite detectar el nivel de líquido y la posición límite en torres, tanques, recipientes esféricos y calderas. No se ve afectado por los cambios de temperatura y no presenta zonas ciegas.",
        "features": ["Lectura intuitiva sin zonas ciegas", "No afectado por cambios bruscos de temperatura", "Soporta visualización local y alarmas remotas"]
    },
    "sl80": {
        "name": "Transmisor de nivel magnetoestrictivo SL80",
        "description": "El transmisor de nivel magnetoestrictivo SL80 es un producto de alta precisión ampliamente utilizado para la medición a nivel de proceso. Su precisión no se ve afectada por las variaciones de la constante dieléctrica, la temperatura ni la presión.",
        "features": ["Alta precisión a nivel de proceso", "No afectado por constante dieléctrica o presión", "Bajo mantenimiento y larga estabilidad"]
    },
    "sl900": {
        "name": "Transmisor de nivel radar serie SL900",
        "description": "La serie SL900 incluye modelos radar con y sin contacto, aptos para alta temperatura, alta presión y entornos anticorrosión. Son prácticamente inafectados por características del medio como la densidad, el pH y la viscosidad.",
        "features": ["Tecnología radar FMCW de 80 GHz", "Ángulo de haz pequeño de 3 grados", "Zona muerta reducida de 0.1 m"]
    },
    "cvp2000": {
        "name": "Posicionador de válvula inteligente CVP2000",
        "description": "El posicionador de válvula inteligente de la serie CVP2000 está equipado con un microprocesador de alto rendimiento. Controla la válvula neumática y cuenta con funciones de comunicación, configuración automática y autodiagnóstico.",
        "features": ["Autodiagnóstico y autoconfiguración", "Soporta comunicación HART", "Apto para actuadores lineales y de carrera angular"]
    },
    "x600": {
        "name": "Calibrador y comunicador interactivo serie X600",
        "description": "Los productos de la serie SUPCON X600 son dispositivos portátiles con pantalla táctil capacitiva completa y pantalla HD 1080P, que integran con éxito un calibrador de procesos inteligente y un comunicador HART.",
        "features": ["Precisión máxima de señal de 0.01%", "Compatibilidad total con HART y actualización de archivos DD", "Diseño de operación dividida para uso en campo"]
    },
    "hd5500": {
        "name": "Barrera de seguridad aislada serie HD5500",
        "description": "La barrera de seguridad aislada serie HD5500 ofrece alta precisión de conversión y baja deriva térmica. Cuenta con fuente de alimentación aislada por puente H de alta eficiencia y diseño ultradelgado para optimizar el espacio.",
        "features": ["Alta precisión de conversión de 0.1%", "Baja deriva térmica de 1 μA/°C", "Diseño ultradelgado de 12.5 mm"]
    },
    "gl": {
        "name": "Válvula de descarga de la serie GL",
        "description": "La válvula de descarga de expansión de la serie GL es una válvula reguladora especial con cuerpo tipo Y integrado. No cuenta con canal de bloqueo ni ángulos muertos, ideal para industrias químicas finas y farmacéuticas.",
        "features": ["Estructura tipo Y sin ángulos muertos", "Evita la precipitación de partículas", "Ideal para industrias químicas y farmacéuticas"]
    },
    "pz": {
        "name": "Válvula de guillotina serie PZ",
        "description": "Una válvula de guillotina diseñada para controlar el flujo de fluidos a través de una tubería mediante una cuchilla compuerta. Es comúnmente utilizada en fábricas de pulpa, plantas químicas y minería.",
        "features": ["Cuchilla deslizante para control de sólidos", "Estructura autolimpiante", "Diseño robusto para minería y pulpa de papel"]
    },
    "z641-941h": {
        "name": "Válvula de compuerta plana serie Z641/941H",
        "description": "La válvula de compuerta plana eléctrica tiene una resistencia de flujo pequeña y realiza posicionamiento automático en la superficie de sellado. Es especialmente adecuada para medios con partículas suspendidas.",
        "features": ["Pequeña resistencia al flujo", "Posicionamiento automático de sellado", "Apto para medios con partículas en suspensión"]
    },
    "z643-943": {
        "name": "Válvula de compuerta de cuña serie Z643/943",
        "description": "Válvula de compuerta de cuña eléctrica o neumática que ofrece baja resistencia al fluido y menor erosión por impacto en la superficie de sellado. Cuenta con un amplio rango de presión y temperatura adecuados.",
        "features": ["Flujo no perturbado de baja caída de presión", "Estructura de sellado hermético a presión de medio", "Bajo torque de apertura y cierre"]
    },
    "ecs-700": {
        "name": "Sistema de Control Distribuido ECS-700",
        "description": "Como plataforma de control central de una planta moderna, ECS-700 agrega datos de toda la planta en tiempo real a través de varios protocolos estándar como OPC, Modbus, HART, FF y Profibus.",
        "features": ["Plataforma de datos para toda la planta", "Gran escala de sistema de hasta un millón de E/S", "Asistencia de operación inteligente y confiable"]
    },
    "jx-300xp": {
        "name": "Sistema de Control Distribuido JX-300XP",
        "description": "Sistema de control distribuido (DCS) redundante con red SCnet II de alta velocidad. Permite la interconexión con dispositivos de bus de campo y PLC con interfaces amigables para configuración y descarga en línea.",
        "features": ["Red de comunicación SCnet II redundante", "Estación de control distribuida independiente", "Diseño totalmente inteligente con diagnóstico online"]
    },
    "tcs-900": {
        "name": "Sistema Instrumentado de Seguridad TCS-900",
        "description": "El sistema TCS-900 es un sistema instrumentado de seguridad (SIS) redundante con excelente cobertura de diagnóstico superior al 99%. Diseñado a prueba de fallos con seguridad integrada según IEC 62443.",
        "features": ["Seguridad y disponibilidad garantizadas", "Votación 2oo3D de 5 capas", "Nivel de interferencia EMC 4A y protección G3"]
    },
    "tcs-500": {
        "name": "Sistema Instrumentado de Seguridad TCS-500",
        "description": "Sistema instrumentado de seguridad (SIS) de alta densidad y flexibilidad de red. Cuenta con degradación 2oo4D con tolerancia a fallos y permite una configuración de módulo único o dual.",
        "features": ["Seguridad integrada con cobertura > 99%", "Redes flexibles estrella, bus y anillo", "Alta densidad de hasta 300 puntos por gabinete"]
    },
    "g5-pro": {
        "name": "Controlador Lógico Programable G5 Pro",
        "description": "El controlador lógico programable G5 Pro es un PLC híbrido de alta confiabilidad. Todos sus componentes admiten redundancia e intercambio en caliente, con una seguridad de la información integrada mediante RSA y AES.",
        "features": ["Módulos hot-swap con soporte redundante", "Procesador de 32 bits a 1 GHz con memoria amplia", "Información de seguridad integrada de doble núcleo"]
    },
    "g3-smart": {
        "name": "Controlador Lógico Programable G3 Smart",
        "description": "El G3 Smart es un PLC compacto de alta adaptabilidad ambiental. Soporta programación bajo lenguajes estándar IEC 61131-3 como FBD, LD, ST, SFC e interconexión mediante Modbus, Profinet y OPC.",
        "features": ["Funciones de control flexibles multitarea", "Entorno amigable IEC 61131-3", "Diseño compacto ideal para espacios reducidos"]
    },
    "nyx": {
        "name": "Sistema de Control Universal Nyx",
        "description": "Construido sobre tecnologías basadas en la nube, el Sistema de Control Universal (UCS) Nyx de SUPCON es altamente escalable, elástico y extensible, eliminando los armarios de control tradicionales y transformando la arquitectura DCS convencional.",
        "features": ["Sistema de control definido por software", "Colaboración remota ágil en la nube", "Eliminación de armarios tradicionales de control"]
    }
}

# Translate english term to spanish
def translate_term(text):
    if not text:
        return text
    # Direct lookups
    t_clean = text.strip()
    if t_clean in VALUE_TRANSLATIONS:
        return VALUE_TRANSLATIONS[t_clean]
    
    # Try word-by-word or regex replacements
    # Check if there are multiple matches
    res = t_clean
    # Sort replacements by length to prevent partial replacement bugs
    sorted_repl = sorted(VALUE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, esp in sorted_repl:
        res = res.replace(eng, esp)
        
    # Translate class phrases if any remaining
    res = re.sub(r'Class\s+([IVXLCDM]+)', r'Clase \1', res, flags=re.IGNORECASE)
    return res

# Clean all English terms in key fields recursively to guarantee no English leak
def clean_english_terms(text):
    if not isinstance(text, str):
        return text
    sorted_cleanup = sorted(ENGLISH_CLEANUP.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, esp in sorted_cleanup:
        # Perform replacements (case insensitive or word replacement)
        # We can do exact string replacements
        text = text.replace(eng, esp)
        # Also do lowercase equivalents
        text = text.replace(eng.lower(), esp.lower())
    return text

def clean_recursively(obj):
    if isinstance(obj, str):
        return clean_english_terms(obj)
    elif isinstance(obj, list):
        return [clean_recursively(item) for item in obj]
    elif isinstance(obj, dict):
        return {clean_recursively(k): clean_recursively(v) for k, v in obj.items()}
    return obj

# Extract multiple specifications in one text block by identifying keyword positions
def extract_specs(text, keywords):
    matches = []
    for kw in keywords:
        for m in re.finditer(re.escape(kw), text, re.IGNORECASE):
            matches.append((m.start(), m.end(), kw))
    
    matches.sort()
    
    specs = {}
    for idx, (start, end, kw) in enumerate(matches):
        val_start = end
        val_end = matches[idx+1][0] if idx + 1 < len(matches) else len(text)
        
        val = text[val_start:val_end].strip()
        val = re.sub(r'^[:：\s,;]+', '', val).strip()
        val = val.replace('\n', ' ').strip()
        
        specs[kw] = val
    return specs

# Parse catalog.txt file
def parse_catalog(catalog_path):
    families = {}
    current_sheet = None
    if not os.path.exists(catalog_path):
        print(f"Catalog file not found at: {catalog_path}")
        return families
        
    with open(catalog_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line_strip = line.strip()
        if not line_strip:
            continue
        if line_strip.startswith("--- Sheet:"):
            current_sheet = line_strip.replace("--- Sheet:", "").replace("---", "").strip()
            continue
        
        parts = re.split(r'\s{2,}', line_strip)
        if len(parts) < 2:
            continue
            
        if current_sheet == "Control System":
            prod_name = parts[0]
            if prod_name in ["ECS-700", "JX-300XP", "TCS-900", "TCS-500", "G5 Pro", "G3 Smart"]:
                features_str = ""
                cert_str = ""
                for p in parts[1:]:
                    if '·' in p or '\n' in p or '-' in p or 'Diagnostic' in p or 'Safe' in p:
                        features_str = p
                    elif any(c in p for c in ['CE', 'SIL', 'EAC', 'PAC', 'G3']):
                        cert_str = p
                
                features = []
                if features_str:
                    raw_feats = features_str.split('\n')
                    for rf in raw_feats:
                        rf = rf.strip().lstrip('·-*• ').strip()
                        if rf:
                            features.append(rf)
                
                certs = []
                if cert_str:
                    raw_certs = re.split(r'[、;,\n\t]+', cert_str)
                    certs = [c.strip() for c in raw_certs if c.strip() and c.strip() != "NaN"]
                
                families[prod_name] = {
                    "features": features,
                    "certificates": certs,
                    "specifications": {}
                }
                
        elif current_sheet == "Instrumentations":
            model_no = parts[1]
            if model_no in ["LN/LM", "SN5", "CN8", "BN", "CXT", "SFE900", "SL900", "HD5500", "X600"]:
                desc_str = ""
                cert_str = ""
                for p in parts[2:]:
                    if 'Diameter' in p or 'Pressure' in p or 'Accuracy' in p or 'Leakage' in p:
                        desc_str = p
                    elif any(c in p for c in ['CE', 'ATEX', 'SIL', 'ROHS', 'Ex d', 'Ex ia', 'CCS']):
                        cert_str = p
                
                specs = {}
                features = []
                
                if desc_str:
                    keywords = [
                        "Nominal Diameter", "Pressure Rating", "Seat Leakage Rate", "Seat Leakage", "Flow characteristic",
                        "Accuracy", "Highest accuracy", "Long-term stability", "Annual capacity", "Measurement range",
                        "measuring range", "Repeatability", "Beam angle", "Blind area", "High conversion accuracy",
                        "low temperature drift", "Maximum accuracy of signal"
                    ]
                    specs = extract_specs(desc_str, keywords)
                    
                    lines_in_desc = desc_str.split('\n')
                    for lid in lines_in_desc:
                        lid = lid.strip()
                        if not lid:
                            continue
                        has_kw = False
                        for kw in keywords:
                            if kw.lower() in lid.lower():
                                has_kw = True
                                break
                        if not has_kw:
                            features.append(lid)
                
                certs = []
                if cert_str:
                    raw_certs = re.split(r'[、;,\n\t]+', cert_str)
                    certs = [c.strip() for c in raw_certs if c.strip() and c.strip() != "NaN"]
                
                families[model_no] = {
                    "features": features,
                    "certificates": certs,
                    "specifications": specs
                }
    return families

# Parse slide content from Field Devices-Supcon.pptx.txt
def parse_slides(file_path):
    if not os.path.exists(file_path):
        print(f"Slides file not found at: {file_path}")
        return []
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slides = re.split(r'--- Slide ppt/slides/slide\d+\.xml ---\n', content)
    parsed_slides = []
    
    for slide in slides:
        if not slide.strip():
            continue
        lines = [l.strip() for l in slide.split('\n') if l.strip()]
        if len(lines) < 2:
            continue
        header = lines[0]
        name = lines[1]
        description = " ".join(lines[2:])
        parsed_slides.append({
            "header": header,
            "name": name,
            "description": description
        })
    return parsed_slides

def find_slide_content(slides, kw):
    # Try exact match first
    for slide in slides:
        name = slide.get("name", "")
        header = slide.get("header", "")
        desc = slide.get("description", "")
        # If the kw is in name or header or desc
        if kw.lower() in name.lower() or kw.lower() in header.lower():
            return name, desc
    # Broad match
    for slide in slides:
        desc = slide.get("description", "")
        if kw.lower() in desc.lower():
            return slide.get("name", ""), desc
    return None, None

def main():
    print("Starting automated content extraction and translation...")
    
    # Load and parse sources
    slides = parse_slides(PPTX_PATH)
    print(f"Parsed {len(slides)} slides from {PPTX_PATH}")
    
    catalog_families = parse_catalog(CATALOG_PATH)
    print(f"Parsed {len(catalog_families)} product families from {CATALOG_PATH}")
    
    final_products = []
    
    for p_def in PRODUCTS_DATA:
        p_id = p_def["id"]
        kw = p_def["kw"]
        category = p_def["category"]
        family = p_def["family"]
        image_path = p_def["image_path"]
        
        # 1. Get Spanish Name and Description from slides or use defaults
        slide_name, slide_desc = find_slide_content(slides, kw)
        
        # Use slide name or default
        name = slide_name if slide_name else p_def.get("name_override", "")
        desc = slide_desc if slide_desc else FALLBACK_DEFAULTS.get(p_id, {}).get("description", "")
        
        # 2. Inherit specs, certificates, features from catalog family if available
        inherited_features = []
        inherited_specs = {}
        inherited_certs = []
        
        if family in catalog_families:
            fam_data = catalog_families[family]
            inherited_features = fam_data.get("features", [])
            inherited_specs = fam_data.get("specifications", {})
            inherited_certs = fam_data.get("certificates", [])
        
        # Translate features
        translated_features = []
        for feat in inherited_features:
            # Look up in feature translations
            t_feat = FEATURE_LOOKUPS.get(feat, feat)
            translated_features.append(t_feat)
            
        # If features is empty, use defaults
        if not translated_features:
            translated_features = FALLBACK_DEFAULTS.get(p_id, {}).get("features", [])
            
        # Translate specifications keys and values
        translated_specs = {}
        for s_key, s_val in inherited_specs.items():
            t_key = KEY_TRANSLATIONS.get(s_key, s_key)
            t_val = translate_term(s_val)
            translated_specs[t_key] = t_val
            
        # Translate certificates
        translated_certs = []
        for cert in inherited_certs:
            t_cert = CERTIFICATE_TRANSLATIONS.get(cert, cert)
            translated_certs.append(t_cert)
            
        # 3. Clean up any remaining English terms in key fields recursively
        product = {
            "id": p_id,
            "name": name,
            "category": category,
            "description": desc,
            "features": translated_features,
            "specifications": translated_specs,
            "certificates": translated_certs,
            "image_path": image_path
        }
        
        # Clean all English terms to satisfy audits
        cleaned_product = clean_recursively(product)
        final_products.append(cleaned_product)
        
    # Write output to productos.json
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_f:
        json.dump(final_products, out_f, indent=2, ensure_ascii=False)
        
    print(f"Extraction and translation complete. Wrote {len(final_products)} products to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
