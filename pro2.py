import sys
if len(sys.argv) ==2:
  Empsalary=int(sys.argv[1])
  Empbonus=int(sys.argv[2])
  print("user provided input values:")
else:
  script_name=sys.argv[0]
  Empsalary=90000
  Empbonus=0.10
  print("No input given-using default values:")

  salary=Empsalary*Empbonus

print("empsalary:",Empsalary)
print("empbonus:",Empbonus)
print("Salary:",salary)
