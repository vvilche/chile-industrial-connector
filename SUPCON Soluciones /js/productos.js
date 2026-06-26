const SUPCON_PRODUCTS = [
  {
    "id": "valvula-globo-1",
    "name": "Válvula de globo para control de fluidos modelo VG1",
    "category": "Válvulas de Globo",
    "description": "Válvula de alta precisión diseñada para regular el flujo de líquidos y gases en procesos industriales exigentes.",
    "features": [
      "Diseño robusto para alta presión",
      "Control de flujo preciso",
      "Mantenimiento sencillo"
    ],
    "specifications": {
      "diámetro_nominal": "DN50",
      "presión_máxima": "PN40",
      "fuga_asiento": "Clase IV"
    },
    "certificates": [
      "CE",
      "ATEX",
      "SIL3"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-globo-2",
    "name": "Válvula de globo criogénica modelo VG2",
    "category": "Válvulas de Globo",
    "description": "Válvula especial para el manejo de fluidos a temperaturas extremadamente bajas, asegurando estanqueidad.",
    "features": [
      "Aislamiento térmico mejorado",
      "Materiales de baja temperatura",
      "Operación suave"
    ],
    "specifications": {
      "diámetro_nominal": "DN80",
      "presión_máxima": "PN25",
      "fuga_asiento": "Clase V"
    },
    "certificates": [
      "CE",
      "SIL2"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-globo-3",
    "name": "Válvula de globo de alta presión modelo VG3",
    "category": "Válvulas de Globo",
    "description": "Equipo diseñado para aplicaciones críticas de vapor y fluidos a presiones extremas.",
    "features": [
      "Cuerpo de acero forjado",
      "Cierre hermético metálico",
      "Larga vida útil"
    ],
    "specifications": {
      "diámetro_nominal": "DN25",
      "presión_máxima": "PN100",
      "fuga_asiento": "Clase VI"
    },
    "certificates": [
      "CE",
      "ATEX"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-globo-4",
    "name": "Válvula de globo sanitaria modelo VG4",
    "category": "Válvulas de Globo",
    "description": "Válvula higiénica para la industria alimentaria y farmacéutica con pulido espejo.",
    "features": [
      "Conexión rápida clamp",
      "Fácil limpieza interna",
      "Material inoxidable 316L"
    ],
    "specifications": {
      "diámetro_nominal": "DN40",
      "presión_máxima": "PN10",
      "fuga_asiento": "Cero fugas"
    },
    "certificates": [
      "FDA",
      "CE"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-bola-1",
    "name": "Válvula de bola de paso total modelo VB1",
    "category": "Válvulas de Bola",
    "description": "Válvula de corte rápido de dos piezas para control general de fluidos limpios.",
    "features": [
      "Paso total sin obstrucciones",
      "Cuerpo de acero inoxidable",
      "Fácil automatización con actuador"
    ],
    "specifications": {
      "diámetro_nominal": "DN100",
      "presión_máxima": "PN16",
      "fuga_asiento": "Cero fugas"
    },
    "certificates": [
      "CE",
      "ATEX"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-bola-2",
    "name": "Válvula de bola de tres vías modelo VB2",
    "category": "Válvulas de Bola",
    "description": "Válvula de desvío y mezcla de flujos en sistemas de tuberías industriales.",
    "features": [
      "Configuración en T o L",
      "Sellos de teflón reforzado",
      "Operación manual o automática"
    ],
    "specifications": {
      "diámetro_nominal": "DN50",
      "presión_máxima": "PN25",
      "fuga_asiento": "Clase VI"
    },
    "certificates": [
      "CE"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-bola-3",
    "name": "Válvula de bola de alta temperatura modelo VB3",
    "category": "Válvulas de Bola",
    "description": "Válvula con asientos metálicos para fluidos a alta temperatura y lodos ligeros.",
    "features": [
      "Asientos metálicos endurecidos",
      "Resistencia a la abrasión térmica",
      "Vástago anti-expulsión"
    ],
    "specifications": {
      "diámetro_nominal": "DN80",
      "presión_máxima": "PN40",
      "fuga_asiento": "Clase V"
    },
    "certificates": [
      "CE",
      "ATEX",
      "SIL3"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-bola-4",
    "name": "Válvula de bola bridada modelo VB4",
    "category": "Válvulas de Bola",
    "description": "Válvula de bola monobloque bridada para la industria química y petroquímica.",
    "features": [
      "Diseño compacto y liviano",
      "Conexión por bridas estándar",
      "Dispositivo antiestático"
    ],
    "specifications": {
      "diámetro_nominal": "DN150",
      "presión_máxima": "PN16",
      "fuga_asiento": "Cero fugas"
    },
    "certificates": [
      "CE",
      "SIL3"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-mariposa-1",
    "name": "Válvula de mariposa concéntrica tipo wafer modelo VM1",
    "category": "Válvulas de Mariposa",
    "description": "Válvula de mariposa de uso general para sistemas de agua y fluidos no agresivos.",
    "features": [
      "Cuerpo compacto tipo wafer",
      "Asiento elastómero reemplazable",
      "Bajo par de operación"
    ],
    "specifications": {
      "diámetro_nominal": "DN200",
      "presión_máxima": "PN10",
      "fuga_asiento": "Cierre hermético"
    },
    "certificates": [
      "CE"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-mariposa-2",
    "name": "Válvula de mariposa de alto rendimiento modelo VM2",
    "category": "Válvulas de Mariposa",
    "description": "Válvula de doble excentricidad para control de fluidos en condiciones de vapor.",
    "features": [
      "Doble desplazamiento del disco",
      "Asiento de PTFE reforzado",
      "Larga vida útil del sello"
    ],
    "specifications": {
      "diámetro_nominal": "DN250",
      "presión_máxima": "PN25",
      "fuga_asiento": "Clase VI"
    },
    "certificates": [
      "CE",
      "ATEX",
      "SIL2"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-mariposa-3",
    "name": "Válvula de mariposa de triple excentricidad modelo VM3",
    "category": "Válvulas de Mariposa",
    "description": "Válvula de mariposa de triple desplazamiento para aislamiento hermético a altas presiones.",
    "features": [
      "Cierre hermético bidireccional",
      "Asiento laminado metal-metal",
      "Resistente a la fricción interna"
    ],
    "specifications": {
      "diámetro_nominal": "DN300",
      "presión_máxima": "PN40",
      "fuga_asiento": "Cero fugas"
    },
    "certificates": [
      "CE",
      "ATEX",
      "SIL3"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "valvula-mariposa-4",
    "name": "Válvula de mariposa tipo lug modelo VM4",
    "category": "Válvulas de Mariposa",
    "description": "Válvula con orejas roscadas para montaje en extremos de línea o mantenimiento.",
    "features": [
      "Cuerpo tipo lug roscado",
      "Fácil instalación y desmontaje",
      "Apta para vacío"
    ],
    "specifications": {
      "diámetro_nominal": "DN125",
      "presión_máxima": "PN16",
      "fuga_asiento": "Cierre hermético"
    },
    "certificates": [
      "CE"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "instrumento-1",
    "name": "Transmisor de presión inteligente modelo INS1",
    "category": "Otros Instrumentos",
    "description": "Transmisor industrial de alta estabilidad para medición continua de presión.",
    "features": [
      "Pantalla digital LCD",
      "Salida analógica de corriente",
      "Carcasa a prueba de explosión"
    ],
    "specifications": {
      "rango_medicion": "0-10 MPa",
      "exactitud_medicion": "0.1 por ciento",
      "alimentacion": "24 VCC"
    },
    "certificates": [
      "CE",
      "ATEX",
      "SIL2"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "instrumento-2",
    "name": "Caudalímetro electromagnético modelo INS2",
    "category": "Otros Instrumentos",
    "description": "Medidor de flujo volumétrico para líquidos conductivos en tuberías llenas.",
    "features": [
      "Sin piezas móviles",
      "Baja pérdida de carga",
      "Medición independiente de densidad"
    ],
    "specifications": {
      "diámetro_nominal": "DN80",
      "exactitud_medicion": "0.5 por ciento",
      "revestimiento": "PTFE"
    },
    "certificates": [
      "CE"
    ],
    "image_path": "images/placeholder.png"
  },
  {
    "id": "instrumento-3",
    "name": "Posicionador neumático inteligente modelo INS3",
    "category": "Otros Instrumentos",
    "description": "Controlador de posición para actuadores neumáticos de válvulas de control.",
    "features": [
      "Calibración automática",
      "Bajo consumo de aire",
      "Diagnóstico de fallas integrado"
    ],
    "specifications": {
      "entrada_control": "4-20 mA",
      "presión_alimentación": "0.6 MPa",
      "acción_actuador": "Lineal o rotativo"
    },
    "certificates": [
      "CE",
      "ATEX"
    ],
    "image_path": "images/placeholder.png"
  }
];
