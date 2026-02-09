required_tags = {"env", "owner", "cost_center"} # Lo que EXIGE la empresa
current_tags = {"env", "created_by"}            # Lo que TIENE el recurso\

tags_faltantes = required_tags - current_tags
print(tags_faltantes)