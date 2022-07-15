import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True)

data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')
names = []

for i in data:
    if "All Users Profiles" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        names.append(i)
print("Systems Connected To Your WIFI ARE ")
print()
for name in names:
    print(name)