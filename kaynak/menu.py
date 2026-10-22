#!/usr/bin/env python3
"""Paraketa menü sayfasını üretir: kaynak/sablon.html + bu dosyadaki veri -> ../index.html

Menüde değişiklik: aşağıdaki MENU verisini düzenleyip `python3 kaynak/menu.py` çalıştırın.
Ürün biçimleri:
  ("Ad", "450 ₺")                      tek fiyatlı ürün
  ("Ad", "450 ₺", "Adet")              ürün + küçük not (Adet, Kg, 33 cl, 2019 ...)
  ("Ad", [("Tek","350 ₺"),("Duble","600 ₺")])   seçenekli ürün
  ("--", "Alt başlık")                 bölüm içi küçük ara başlık
"""
import html, pathlib

HERE = pathlib.Path(__file__).resolve().parent

T, D, PT, PD = "Tek", "Duble", "Peynirli Tek", "Peynirli Duble"

def rakı(p20, p35, p50, p70, p100):
    return [("20 cl", p20), ("35 cl", p35), ("50 cl", p50), ("70 cl", p70), ("100 cl", p100)]

# (id, başlık, üst çubuk etiketi | None = önceki grubun parçası, grup id, içerik)
MENU = [
  ("salatalar", "SALATALAR", "Salatalar", None, [
    ("Söğüş", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Mevsim Salatası", [(T, "350 ₺"), (D, "600 ₺"), (PT, "450 ₺"), (PD, "700 ₺")]),
    ("Bahçe Salatası", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Koparma Salatası", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Roka Salatası", [(T, "350 ₺"), (PT, "450 ₺"), (PD, "700 ₺")]),
    ("Gavurdağı Salatası", [(T, "400 ₺"), (D, "700 ₺")]),
    ("İstanbul Salatası", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Çoban Salatası", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Göbek Salata", [(T, "350 ₺"), (D, "600 ₺")]),
    ("Yeşil Salata", [(T, "350 ₺"), (PT, "450 ₺"), (PD, "700 ₺")]),
    ("Peynirli Karides Salatası", "1.100 ₺"),
  ]),
  ("mezeler", "MEZELER", "Mezeler", None, [
    ("Peynir", "200 ₺"),
    ("Levrek Marin", "700 ₺"),
    ("Yosunlu Levrek Marin", "750 ₺"),
    ("İsli Uskumru", "700 ₺"),
    ("Lakerda", "600 ₺", "Adet"),
    ("Somon Marin", "700 ₺"),
    ("Akya Pastırma", "220 ₺", "Adet"),
    ("Somon Füme", "200 ₺", "Adet"),
    ("Ahtapot Söğüş", "1.100 ₺"),
    ("Ahtapot Carpaccio", "1.250 ₺"),
    ("Hançuez", "700 ₺"),
    ("Çiroz", "700 ₺"),
    ("Köpoğlu", "450 ₺"),
    ("Atom", "450 ₺"),
    ("Semizotu", "450 ₺"),
    ("Kabak", "450 ₺"),
    ("Zakko", "450 ₺"),
    ("Patlıcan Salatası", "450 ₺"),
    ("Patlıcan Söğüş", "450 ₺"),
    ("Şakşuka", "450 ₺"),
    ("Fava", "450 ₺"),
    ("Pilaki", "450 ₺"),
    ("Kuru Börülce", "450 ₺"),
    ("Girit Ezme", "450 ₺"),
    ("Rum Mezesi", "450 ₺"),
    ("Pazı Kavurma", "450 ₺"),
    ("Kuru Domates Salatası", "450 ₺"),
    ("Kaya Koruğu", "450 ₺"),
    ("Deniz Börülcesi", "450 ₺"),
    ("Kuşkonmaz", "700 ₺"),
    ("Yaban Mersini Salatası", "450 ₺"),
    ("Karides Söğüş", "1.100 ₺"),
    ("Palamut Pilaki", "700 ₺"),
    ("Cibes Otu Salatası", "450 ₺"),
    ("Turşu", "450 ₺"),
    ("Kavun", "200 ₺"),
    ("Kuru Cacık", "450 ₺"),
    ("Avokadolu Karides Marin", "900 ₺"),
    ("Kalamar Salatası", "700 ₺"),
    ("Şevketibostan", "700 ₺"),
  ]),
  ("ara-sicaklar", "ARA SICAKLAR", "Ara Sıcaklar", None, [
    ("Kalamar Tava", "1.100 ₺"),
    ("Kalamar Izgara", "1.100 ₺"),
    ("Kalamar Kokoreç", "1.000 ₺"),
    ("Tereyağlı Karides", "1.100 ₺"),
    ("Karides Güveç", "1.200 ₺"),
    ("Kadayıflı Jumbo Sarma", "550 ₺"),
    ("Enginar Kalbi", "450 ₺"),
    ("İstiridye Mantarı", "550 ₺"),
    ("Izgara Peynir", "550 ₺"),
    ("Paçanga Böreği", "450 ₺"),
    ("Deniz Mahsulleri Böreği", "500 ₺"),
    ("Balık Mantı", "800 ₺"),
    ("Balık Kokoreç", "800 ₺"),
    ("Okyanus Lokumu", "450 ₺", "Adet"),
    ("Levrek Sarma", "500 ₺", "Adet"),
    ("Lavunya", "450 ₺"),
    ("Ege Otlu Levrek Sarma", "500 ₺"),
    ("Balık Köftesi", "450 ₺"),
    ("Ahtapot Izgara", "10.000 ₺", "Kg"),
    ("Ahtapot Beğendi", "1.500 ₺"),
    ("Sıcak Ot", "500 ₺"),
    ("Cips Patates", "400 ₺"),
    ("Jumbo Karides Izgara", "6.500 ₺", "Kg"),
  ]),
  ("baliklar", "BALIKLAR", "Balıklar", None, {
    "fish": ["Levrek", "Çupra", "Palamut", "Sarıkanat", "Lüfer", "Dil Balığı", "Pisi Balığı",
             "Dülger", "Eşkina", "Karagöz", "Tekir", "Barbun", "Jumbo Kalkan", "Kırlangıç",
             "Lipsoz", "Kofana", "Lagos", "Mercan", "Sinarit", "Sardalya", "Istakoz", "Böcek",
             "Pavurya", "Orfoz", "Minekop"],
    "note": "Balıklarımızın fiyatları günlük olarak değişmektedir.",
  }),
  ("tatlilar", "TATLILAR & MEYVELER", "Tatlılar", None, [
    ("Ayva Tatlısı", "450 ₺"),
    ("Kabak Tatlısı", "450 ₺"),
    ("Ekmek Kadayıfı", "450 ₺"),
    ("İrmik", "450 ₺"),
    ("Volkanik", "450 ₺"),
    ("Kazandibi", "450 ₺"),
    ("Fırın Helva", [(T, "450 ₺"), (D, "800 ₺")]),
    ("İncir Tatlısı", "450 ₺"),
    ("Dondurma", "450 ₺"),
    ("Serpme Meyve", [(T, "450 ₺"), (D, "900 ₺")]),
  ]),
  ("rakilar", "RAKILAR", "Rakılar", "İçecekler", [
    ("Sarızeybek", rakı("1.500 ₺", "2.750 ₺", "3.500 ₺", "4.300 ₺", "5.000 ₺")),
    ("Yeni Rakı Yeni Seri", rakı("1.250 ₺", "2.500 ₺", "3.250 ₺", "3.750 ₺", "4.250 ₺")),
    ("Beylerbeyi Göbek", rakı("1.500 ₺", "2.750 ₺", "3.500 ₺", "4.300 ₺", "5.000 ₺")),
    ("Tekirdağ Göbek", rakı("1.500 ₺", "2.750 ₺", "3.500 ₺", "4.300 ₺", "5.000 ₺")),
    ("Tek", "350 ₺"),
    ("Duble", "550 ₺"),
  ]),
  ("kirmizi", "KIRMIZI ŞARAPLAR", "Şaraplar", None, [
    ("Umurbey Cabernet Merlot", "2.250 ₺"),
    ("Selendi Merlot", "5.550 ₺", "2023"),
    ("Umurbey Kadeh", "600 ₺"),
  ]),
  ("beyaz", "BEYAZ ŞARAPLAR", None, None, [
    ("Umurbey Sauvignon Blanc", "3.750 ₺", "2020"),
    ("Yedi Bilgeler Anaxagoras", "5.250 ₺"),
    ("Kayra Allure", "2.250 ₺", "2019"),
    ("Cielo Sauvignon", "2.250 ₺"),
    ("Cielo Kadeh", "600 ₺"),
  ]),
  ("blush", "BLUSH", None, None, [
    ("Kızıl Alan", "3.150 ₺"),
    ("Kızıl Alan Kadeh", "600 ₺"),
  ]),
  ("biralar", "BİRALAR", "Biralar", None, [
    ("Efes Klasik", "350 ₺", "33 cl"),
    ("Miller", "350 ₺", "33 cl"),
    ("Heineken", "350 ₺", "33 cl"),
    ("Corona", "350 ₺", "35,5 cl"),
    ("Bitburger", "250 ₺", "Alkolsüz"),
  ]),
  ("tekila", "TEKİLA", "Diğer İçkiler", None, [("Patrón Silver", "7.000 ₺")]),
  ("konyaklar", "KONYAKLAR", None, None, [
    ("Martell VSOP", "8.000 ₺"),
    ("Hennessy VS", "5.000 ₺"),
  ]),
  ("likorler", "LİKÖRLER", None, None, [
    ("Hare Kremalı Türk Kahvesi", "2.500 ₺"),
    ("Hare Vişne", "2.500 ₺"),
  ]),
  ("sampanya", "ŞAMPANYA", None, None, [("Cinzano Prosecco", "4.750 ₺")]),
  ("gin", "GİN", None, None, [("Gordon's", "4.500 ₺")]),
  ("viskiler", "VİSKİLER", None, None, [
    ("Hibiki", "16.500 ₺"),
    ("Talisker 10 Yıl", "6.750 ₺"),
    ("Chivas Regal 18 Yıl", "8.000 ₺"),
    ("Black Label", "5.250 ₺"),
    ("Aberlour 12 Yıl", "7.500 ₺"),
    ("Lagavulin 8 Yıl", "7.500 ₺"),
    ("Black Label Duble", "750 ₺"),
  ]),
]

e = html.escape

def item_html(it):
    name = it[0]
    if isinstance(it[1], list):
        opts = "".join(f"<dt>{e(o)}</dt><dd>{e(p)}</dd>" for o, p in it[1])
        return f'<li class="item multi"><h3>{e(name)}</h3><dl class="opts">{opts}</dl></li>'
    tag = f' <span class="tag">{e(it[2])}</span>' if len(it) > 2 else ""
    return f'<li class="item"><h3>{e(name)}{tag}</h3><span class="price">{e(it[1])}</span></li>'

def build():
    nav, secs, cur_nav = [], [], None
    for sid, title, navlbl, group, content in MENU:
        if group:
            secs.append(f'  <p class="group-title">{e(group)}</p>')
        if navlbl:
            cur_nav = sid
            nav.append(f'    <li><a href="#{sid}">{e(navlbl)}</a></li>')
        attr = "" if navlbl else f' data-nav="{cur_nav}"'
        if isinstance(content, dict):
            body = ('    <ul class="fishes">' + "".join(f"<li>{e(f)}</li>" for f in content["fish"]) +
                    f'</ul>\n    <p class="note">{e(content["note"])}</p>')
        else:
            body = '    <ul class="items compact">\n' + "\n".join("      " + item_html(i) for i in content) + "\n    </ul>"
        secs.append(f'  <section id="{sid}"{attr} aria-labelledby="h-{sid}">\n'
                    f'    <div class="frame"><h2 id="h-{sid}">{e(title)}</h2></div>\n{body}\n  </section>')
    t = (HERE / "sablon.html").read_text()
    t = t.replace("<!--LOGO-->", (HERE / "logo-inline.svg").read_text())
    t = t.replace("<!--NAV-->", "\n".join(nav)).replace("<!--SECTIONS-->", "\n\n".join(secs))
    (HERE.parent / "index.html").write_text(t)

if __name__ == "__main__":
    build()
    print("index.html güncellendi")
