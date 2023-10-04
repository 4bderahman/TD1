s = int(input("entrer nombre de secondes:"))

jours = s // (24 * 60 * 60) 
seconds = s % (24 * 60 * 60)
hours = seconds // (60 * 60)
soconds = seconds % (60 * 60)
minutes = seconds // 60
seconds = seconds % 60

print("jours:", jours, "hours:", hours, "minutes:", minutes, "seconds:", seconds)