from datetime import datetime

out={}
out["city"]="SPB"
wo=["test", "werew", "rewrew"]
for put_out in wo:
  print(put_out)
  out[put_out] = {}
  out[put_out]["test"] = "adsadsadsa"

print(out)

dt=[1632096000, 1632106800, 1632117600, 1632128400, 1632223200]

for d in dt:
  print(datetime.fromtimestamp(d).strftime("%Y-%m-%d"))
#print(dt)

days = 3
days = days*8
print(days)
