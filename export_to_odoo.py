#!/usr/bin/env python3
import csv
import os
import xmlrpc.client

# ==============================================================================
# CONFIGURACIÓN DE ACCESO A ODOO
# Edite estos campos con las credenciales de su instancia de Odoo
# ==============================================================================
ODOO_URL = "https://tu-compania.odoo.com"  # URL de su Odoo (ej: https://miempresa.odoo.com)
ODOO_DB = "nombre_base_datos"              # Nombre de la base de datos (generalmente el subdominio)
USERNAME = "tu-usuario@correo.com"         # Correo de inicio de sesión del usuario de Odoo
API_KEY = "tu-api-key-o-contraseña"        # API Key generada en Preferencias de Odoo o contraseña

CSV_FILE = "base_empresas_procesos_chile.csv"

def run_import():
    # Verificar que el archivo CSV existe en la ruta actual
    if not os.path.exists(CSV_FILE):
        print(f"[-] Error: No se encontró el archivo '{CSV_FILE}' en el directorio actual.")
        print("Asegúrese de ejecutar este script en la misma carpeta donde está el CSV.")
        return

    print("[*] Iniciando proceso de exportación a Odoo CRM...")
    print(f"[*] Conectando a la instancia de Odoo en: {ODOO_URL}")
    
    try:
        # 1. Establecer conexión XML-RPC y autenticarse
        common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        uid = common.authenticate(ODOO_DB, USERNAME, API_KEY, {})
        
        if not uid:
            print("[-] Error: Falló la autenticación en Odoo. Verifique la URL, Base de Datos, Usuario y API Key.")
            return
            
        print(f"[+] Autenticación exitosa. ID de Usuario de Odoo: {uid}")
        
        # 2. Conectar al servicio de base de datos de objetos
        models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
        
        # 3. Leer y procesar el archivo CSV
        print(f"[*] Leyendo base de datos desde '{CSV_FILE}'...")
        count = 0
        
        with open(CSV_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                empresa = row.get("Empresa", "")
                rut = row.get("RUT", "")
                sector = row.get("Sector", "")
                planta = row.get("Planta", "")
                region = row.get("Region", "")
                comuna = row.get("Comuna", "")
                proceso_critico = row.get("Proceso_Critico", "")
                opp_control = row.get("Oportunidad_Control", "")
                opp_inst = row.get("Oportunidad_Instrumentacion", "")
                opp_elec = row.get("Oportunidad_Electrica", "")
                web = row.get("Pagina_Web", "")
                linkedin = row.get("LinkedIn", "")
                email = row.get("Email", "")
                sucursales = row.get("Sucursales", "1")
                
                # Armar una descripción detallada para el cuerpo del Lead en Odoo CRM
                descripcion = (
                    f"RUT de la Empresa: {rut}\n"
                    f"Sector Industrial: {sector}\n"
                    f"Ubicación de Planta: {comuna}, {region}\n"
                    f"Número de Sucursales en Chile: {sucursales}\n\n"
                    f"PROCESO INDUSTRIAL CRÍTICO:\n"
                    f"{proceso_critico}\n\n"
                    f"OPORTUNIDADES DE VENTA IDENTIFICADAS:\n"
                    f"- CONTROL INDUSTRIAL / DCS / PLC: {opp_control}\n"
                    f"- INSTRUMENTACIÓN DE PROCESOS: {opp_inst}\n"
                    f"- COMPONENTES ELÉCTRICOS Y POTENCIA: {opp_elec}\n\n"
                    f"CONTACTOS Y REDES:\n"
                    f"- Correo Electrónico: {email}\n"
                    f"- Sitio Web: {web}\n"
                    f"- Perfil LinkedIn: {linkedin}\n"
                )
                
                # Estructurar la data del Lead en Odoo
                lead_data = {
                    'name': f"Prospección Industrial: {empresa}",
                    'partner_name': empresa,
                    'email_from': email,
                    'website': web,
                    'description': descripcion,
                    'type': 'lead'
                }
                
                # Crear el registro de Lead en Odoo
                lead_id = models.execute_kw(
                    ODOO_DB, uid, API_KEY,
                    'crm.lead', 'create', [lead_data]
                )
                print(f"[+] Lead creado con éxito para: {empresa} | Odoo Lead ID: {lead_id}")
                count += 1
                
        print(f"[+] Proceso completado. Se importaron {count} leads con éxito a Odoo CRM.")
        
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado durante la comunicación con la API de Odoo:")
        print(f"    {str(e)}")

if __name__ == "__main__":
    run_import()
