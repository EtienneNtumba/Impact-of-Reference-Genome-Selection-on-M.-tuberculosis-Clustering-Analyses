import pybedtools

# Chemins vers vos fichiers BED
fichier_bed1 = 'N1177.LR.Asm_conservative_AF19-like_masking_file.bed'
fichier_bed2 = 'CP010329_H37Rv_conservative_AF19-like_masking_file.bed'

# Charger les fichiers BED en tant qu'objets BedTool
bed1 = pybedtools.BedTool(fichier_bed1)
bed2 = pybedtools.BedTool(fichier_bed2)

# Trouver l'intersection
intersection = bed1.intersect(bed2)

# Enregistrer l'intersection dans un nouveau fichier BED
chemin_sortie = 'intersection_pybedtools.bed'
intersection.saveas(chemin_sortie)

print(f"L'intersection a été enregistrée dans {chemin_sortie}")
