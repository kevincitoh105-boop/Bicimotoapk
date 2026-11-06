#!/usr/bin/env python3
"""Cambia +86 -> +53 y la validacion de telefono (China -> Cuba) dentro del APK."""
import sys, zipfile

SRC, DST = sys.argv[1], sys.argv[2]
BASE = "assets/apps/__UNI__9928017/www/"

PATCHES = {
    BASE + "app-view.js": [
        ('t._v("+86")', 't._v("+53")', None),
    ],
    BASE + "app-service.js": [
        (r'/^1[34567890]\d{9}$/.test(e)', r'/^(5\d{7}|1[34567890]\d{9})$/.test(e)', 1),
        ('11==this.phone.length', '(8==this.phone.length||11==this.phone.length)', 1),
        ('phone:"18910311240"', 'phone:""', 1),
    ],
}

def apply(name, data):
    text = data.decode("utf-8")
    for old, new, expected in PATCHES[name]:
        n = text.count(old)
        if n == 0 or (expected is not None and n != expected):
            sys.exit(f"ERROR: en {name} se esperaba {expected} coincidencias de {old!r} y hay {n}")
        text = text.replace(old, new)
        print(f"OK {name.split('/')[-1]}: {n} cambio(s) -> {new[:40]}")
    return text.encode("utf-8")

with zipfile.ZipFile(SRC) as zin, zipfile.ZipFile(DST, "w") as zout:
    for item in zin.infolist():
        n = item.filename
        if n == "META-INF/MANIFEST.MF" or (n.startswith("META-INF/") and n.endswith((".SF", ".RSA", ".DSA", ".EC"))):
            continue
        data = zin.read(n)
        if n in PATCHES:
            data = apply(n, data)
        zi = zipfile.ZipInfo(n, date_time=item.date_time)
        zi.compress_type = item.compress_type
        zi.external_attr = item.external_attr
        zout.writestr(zi, data)
print("APK parchado (sin firmar):", DST)
