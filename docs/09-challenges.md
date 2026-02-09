# 💼 Desafíos Prácticos - Cloud/DevOps

## Introducción

Los desafíos en la carpeta `Challenges/` están diseñados para aplicar Python en contextos reales de Cloud Computing y DevOps.

---

## Challenge 1: Filtrar VMs en Ejecución

### Objetivo
Filtrar instancias de máquinas virtuales que están en estado "RUNNING".

### Problema

```python
instances = [
    {"name": "vm1", "status": "RUNNING"},
    {"name": "vm2", "status": "TERMINATED"},
    {"name": "vm3", "status": "RUNNING"}
]
```

### Solución

```python
def get_running_vms(instances_list):
    running_instances = []
    
    # 'vm' representa el diccionario completo
    for vm in instances_list:
        # Acceder al valor por su clave
        if vm["status"] == "RUNNING":
            running_instances.append(vm["name"])
            
    return running_instances

# Uso
print(get_running_vms(instances))
# ['vm1', 'vm3']
```

### Conceptos Aplicados
- ✅ Iteración sobre listas
- ✅ Diccionarios y acceso por clave
- ✅ Condicionales
- ✅ Funciones con retorno

### Versión con List Comprehension

```python
def get_running_vms(instances_list):
    return [vm["name"] for vm in instances_list if vm["status"] == "RUNNING"]
```

---

## Challenge 2: Parsear Logs

### Objetivo
Extraer información específica de una entrada de log (nivel de error e IP).

### Problema

```python
log_entry = "2024-02-08 14:00:00 [ERROR] Connection failed at ip=10.0.0.5"
```

### Solución

```python
log_entry = "2024-02-08 14:00:00 [ERROR] Connection failed at ip=10.0.0.5"

# Limpiar caracteres especiales
clean_logentry = log_entry.replace("[", "").replace("]", "").replace("ip=", "")

# Dividir en palabras
clean_logentry = clean_logentry.split()

# Crear diccionario
dictionary = {}
dictionary["level"] = clean_logentry[2]   # ERROR
dictionary["ip"] = clean_logentry[-1]     # 10.0.0.5

print(dictionary)
# {'level': 'ERROR', 'ip': '10.0.0.5'}
```

### Conceptos Aplicados
- ✅ Métodos de strings (replace, split)
- ✅ Diccionarios
- ✅ Indexación (positiva y negativa)

### Versión Mejorada con Regex

```python
import re

def parse_log(log_entry):
    # Extraer nivel de error
    level_match = re.search(r'\[(.*?)\]', log_entry)
    level = level_match.group(1) if level_match else None
    
    # Extraer IP
    ip_match = re.search(r'ip=(\d+\.\d+\.\d+\.\d+)', log_entry)
    ip = ip_match.group(1) if ip_match else None
    
    return {"level": level, "ip": ip}

result = parse_log(log_entry)
print(result)
# {'level': 'ERROR', 'ip': '10.0.0.5'}
```

---

## Challenge 3: Calcular Almacenamiento Desperdiciado

### Objetivo
Calcular el total de almacenamiento en discos no adjuntos a ninguna VM.

### Problema

```python
disks = [
    {"id": "d-1", "size_gb": 100, "attached_to": "vm-1"},
    {"id": "d-2", "size_gb": 50,  "attached_to": None},
    {"id": "d-3", "size_gb": 200, "attached_to": None},
    {"id": "d-4", "size_gb": 500, "attached_to": "vm-2"}
]
```

### Solución

```python
def calculate_wasted_storage(disks):
    total_size = 0
    for disk in disks:
        if disk["attached_to"] is None:
            total_size += disk["size_gb"]
    return total_size

print(calculate_wasted_storage(disks))
# 250 (50 + 200)
```

### Conceptos Aplicados
- ✅ Iteración sobre listas de diccionarios
- ✅ Condicionales con None
- ✅ Acumulación de valores

### Versión con List Comprehension

```python
def calculate_wasted_storage(disks):
    return sum(disk["size_gb"] for disk in disks if disk["attached_to"] is None)
```

### Versión con Filter

```python
def calculate_wasted_storage(disks):
    unattached = filter(lambda d: d["attached_to"] is None, disks)
    return sum(disk["size_gb"] for disk in unattached)
```

---

## Challenge 4: Validar Tags Requeridos

### Objetivo
Identificar tags faltantes en recursos cloud.

### Problema

```python
required_tags = {"env", "owner", "cost_center"}  # Lo que EXIGE la empresa
current_tags = {"env", "created_by"}             # Lo que TIENE el recurso
```

### Solución

```python
required_tags = {"env", "owner", "cost_center"}
current_tags = {"env", "created_by"}

tags_faltantes = required_tags - current_tags
print(tags_faltantes)
# {'owner', 'cost_center'}
```

### Conceptos Aplicados
- ✅ Sets (conjuntos)
- ✅ Operaciones de conjuntos (diferencia)

### Versión con Función

```python
def validate_tags(required, current):
    missing = required - current
    extra = current - required
    
    return {
        "missing": missing,
        "extra": extra,
        "valid": len(missing) == 0
    }

result = validate_tags(required_tags, current_tags)
print(result)
# {
#   'missing': {'owner', 'cost_center'},
#   'extra': {'created_by'},
#   'valid': False
# }
```

### Aplicación Real

```python
class ResourceValidator:
    def __init__(self, required_tags):
        self.required_tags = set(required_tags)
    
    def validate_resource(self, resource):
        current_tags = set(resource.get("tags", {}).keys())
        missing = self.required_tags - current_tags
        
        return {
            "resource_id": resource["id"],
            "valid": len(missing) == 0,
            "missing_tags": list(missing)
        }
    
    def validate_resources(self, resources):
        return [self.validate_resource(r) for r in resources]

# Uso
validator = ResourceValidator(["env", "owner", "cost_center"])

resources = [
    {"id": "i-123", "tags": {"env": "prod", "owner": "team-a"}},
    {"id": "i-456", "tags": {"env": "dev", "owner": "team-b", "cost_center": "eng"}},
]

results = validator.validate_resources(resources)
for result in results:
    print(result)
```

---

## Challenge 5: Incompleto

### Estado
Este desafío está incompleto en el repositorio original.

### Código Actual

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
```

### Posible Implementación

```python
# Calcular el segundo puntaje más alto
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Remover duplicados y ordenar
    unique_scores = sorted(set(arr), reverse=True)
    
    # Obtener el segundo más alto
    if len(unique_scores) >= 2:
        print(unique_scores[1])
    else:
        print("No hay segundo puntaje")
```

---

## Terraform Challenge

### Archivo: Terraform.tf

```hcl
resource "google_storage_bucket" "backup_bucket" {
    name = "epam-interview-bucket-2024"
    location = "US"
    lifecycle {
        prevent_destroy = true
    }
}
```

### Conceptos de Terraform

#### 1. Resource
Define un recurso de infraestructura.

#### 2. Lifecycle
Controla el comportamiento del recurso:
- `prevent_destroy = true`: Previene eliminación accidental

### Integración Python + Terraform

```python
import subprocess
import json

class TerraformManager:
    def __init__(self, working_dir="."):
        self.working_dir = working_dir
    
    def init(self):
        """Inicializar Terraform"""
        subprocess.run(["terraform", "init"], cwd=self.working_dir)
    
    def plan(self):
        """Generar plan de ejecución"""
        result = subprocess.run(
            ["terraform", "plan", "-json"],
            cwd=self.working_dir,
            capture_output=True,
            text=True
        )
        return result.stdout
    
    def apply(self, auto_approve=False):
        """Aplicar cambios"""
        cmd = ["terraform", "apply"]
        if auto_approve:
            cmd.append("-auto-approve")
        subprocess.run(cmd, cwd=self.working_dir)
    
    def output(self):
        """Obtener outputs"""
        result = subprocess.run(
            ["terraform", "output", "-json"],
            cwd=self.working_dir,
            capture_output=True,
            text=True
        )
        return json.loads(result.stdout)

# Uso
tf = TerraformManager("./infrastructure")
tf.init()
tf.plan()
tf.apply(auto_approve=True)
outputs = tf.output()
print(outputs)
```

---

## Ejercicios Adicionales

### Ejercicio 1: Monitoreo de Instancias

```python
def check_instance_health(instances):
    """
    Verifica el estado de salud de instancias
    """
    healthy = []
    unhealthy = []
    
    for instance in instances:
        if instance["status"] == "RUNNING" and instance["health_check"] == "passing":
            healthy.append(instance["name"])
        else:
            unhealthy.append({
                "name": instance["name"],
                "status": instance["status"],
                "health": instance.get("health_check", "unknown")
            })
    
    return {
        "healthy_count": len(healthy),
        "unhealthy_count": len(unhealthy),
        "healthy": healthy,
        "unhealthy": unhealthy
    }
```

### Ejercicio 2: Análisis de Costos

```python
def analyze_costs(resources):
    """
    Analiza costos por tipo de recurso
    """
    costs_by_type = {}
    
    for resource in resources:
        resource_type = resource["type"]
        cost = resource["monthly_cost"]
        
        if resource_type not in costs_by_type:
            costs_by_type[resource_type] = 0
        
        costs_by_type[resource_type] += cost
    
    total_cost = sum(costs_by_type.values())
    
    return {
        "total": total_cost,
        "by_type": costs_by_type,
        "most_expensive": max(costs_by_type, key=costs_by_type.get)
    }
```

---

## Resumen

Los desafíos cubren:
- ✅ Filtrado de datos cloud
- ✅ Parsing de logs
- ✅ Análisis de recursos
- ✅ Validación de configuraciones
- ✅ Integración con Terraform
- ✅ Automatización DevOps

💡 **Tip**: Estos desafíos son representativos de tareas reales en roles de Cloud Engineer y DevOps.
