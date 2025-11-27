import sys
if len(sys.argv)==2:
  script_name=sys.argv[0]
  salary=float(sys.argv[1])
  print("user provided input values:")
else:
  salary=97000
  print("No input given-using default values:")

bonus=salary*0.10
total_salary=salary+bonus

print("Bonus:",bonus)
print("Updated salary:",total_salary)
