#!/usr/bin/env python3
"""Paraketa menü sayfasını üretir: kaynak/sablon.html + bu dosyadaki veri -> ../index.html

Menüde değişiklik: aşağıdaki MENU verisini düzenleyip `python3 kaynak/menu.py` çalıştırın.
Ürün biçimleri:
  ("Ad", "450 TL")                      tek fiyatlı ürün
  ("Ad", "450 TL", "Adet")              ürün + küçük not (Adet, Kg, 33 cl, 2019 ...)
  ("Ad", [("Tek","350 TL"),("Duble","600 TL")])   seçenekli ürün
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
    ("Söğüş", [(T, "350 TL"), (D, "600 TL")]),
    ("Mevsim Salatası", [(T, "350 TL"), (D, "600 TL"), (PT, "450 TL"), (PD, "700 TL")]),
    ("Bahçe Salatası", [(T, "350 TL"), (D, "600 TL")]),
    ("Koparma Salatası", [(T, "350 TL"), (D, "600 TL")]),
    ("Roka Salatası", [(T, "350 TL"), (PT, "450 TL"), (PD, "700 TL")]),
    ("Gavurdağı Salatası", [(T, "400 TL"), (D, "700 TL")]),
    ("İstanbul Salatası", [(T, "350 TL"), (D, "600 TL")]),
    ("Çoban Salatası", [(T, "350 TL"), (D, "600 TL")]),
    ("Göbek Salata", [(T, "350 TL"), (D, "600 TL")]),
    ("Yeşil Salata", [(T, "350 TL"), (PT, "450 TL"), (PD, "700 TL")]),
    ("Peynirli Karides Salatası", "1.100 TL"),
  ]),
  ("mezeler", "MEZELER", "Mezeler", None, [
    ("Peynir", "200 TL"),
    ("Levrek Marin", "700 TL"),
    ("Yosunlu Levrek Marin", "750 TL"),
    ("İsli Uskumru", "700 TL"),
    ("Lakerda", "600 TL", "Adet"),
    ("Somon Marin", "700 TL"),
    ("Akya Pastırma", "220 TL", "Adet"),
    ("Somon Füme", "200 TL", "Adet"),
    ("Ahtapot Söğüş", "1.100 TL"),
    ("Ahtapot Carpaccio", "1.250 TL"),
    ("Hançuez", "700 TL"),
    ("Çiroz", "700 TL"),
    ("Köpoğlu", "450 TL"),
    ("Atom", "450 TL"),
    ("Semizotu", "450 TL"),
    ("Kabak", "450 TL"),
    ("Zakko", "450 TL"),
    ("Patlıcan Salatası", "450 TL"),
    ("Patlıcan Söğüş", "450 TL"),
    ("Şakşuka", "450 TL"),
    ("Fava", "450 TL"),
    ("Pilaki", "450 TL"),
    ("Kuru Börülce", "450 TL"),
    ("Girit Ezme", "450 TL"),
    ("Rum Mezesi", "450 TL"),
    ("Pazı Kavurma", "450 TL"),
    ("Kuru Domates Salatası", "450 TL"),
    ("Kaya Koruğu", "450 TL"),
    ("Deniz Börülcesi", "450 TL"),
    ("Kuşkonmaz", "700 TL"),
    ("Yaban Mersini Salatası", "450 TL"),
    ("Karides Söğüş", "1.100 TL"),
    ("Palamut Pilaki", "700 TL"),
    ("Cibes Otu Salatası", "450 TL"),
    ("Turşu", "450 TL"),
    ("Kavun", "200 TL"),
    ("Kuru Cacık", "450 TL"),
    ("Avokadolu Karides Marin", "900 TL"),
    ("Kalamar Salatası", "700 TL"),
    ("Şevketibostan", "700 TL"),
  ]),
  ("ara-sicaklar", "ARA SICAKLAR", "Ara Sıcaklar", None, [
    ("Kalamar Tava", "1.100 TL"),
    ("Kalamar Izgara", "1.100 TL"),
    ("Kalamar Kokoreç", "1.000 TL"),
    ("Tereyağlı Karides", "1.100 TL"),
    ("Karides Güveç", "1.200 TL"),
    ("Kadayıflı Jumbo Sarma", "550 TL"),
    ("Enginar Kalbi", "450 TL"),
    ("İstiridye Mantarı", "550 TL"),
    ("Izgara Peynir", "550 TL"),
    ("Paçanga Böreği", "450 TL"),
    ("Deniz Mahsulleri Böreği", "500 TL"),
    ("Balık Mantı", "800 TL"),
    ("Balık Kokoreç", "800 TL"),
    ("Okyanus Lokumu", "450 TL", "Adet"),
    ("Levrek Sarma", "500 TL", "Adet"),
    ("Lavunya", "450 TL"),
    ("Ege Otlu Levrek Sarma", "500 TL"),
    ("Balık Köftesi", "450 TL"),
    ("Ahtapot Izgara", "10.000 TL", "Kg"),
    ("Ahtapot Beğendi", "1.500 TL"),
    ("Sıcak Ot", "500 TL"),
    ("Cips Patates", "400 TL"),
    ("Jumbo Karides Izgara", "6.500 TL", "Kg"),
  ]),
  ("baliklar", "BALIKLAR", "Balıklar", None, {
    "fish": ["Levrek", "Çupra", "Palamut", "Sarıkanat", "Lüfer", "Dil Balığı", "Pisi Balığı",
             "Dülger", "Eşkina", "Karagöz", "Tekir", "Barbun", "Jumbo Kalkan", "Kırlangıç",
             "Lipsoz", "Kofana", "Lagos", "Mercan", "Sinarit", "Sardalya", "Istakoz", "Böcek",
             "Pavurya", "Orfoz", "Minekop"],
    "note": "Balıklarımızın fiyatları günlük olarak değişmektedir.",
  }),
  ("tatlilar", "TATLILAR & MEYVELER", "Tatlılar", None, [
    ("Ayva Tatlısı", "450 TL"),
    ("Kabak Tatlısı", "450 TL"),
    ("Ekmek Kadayıfı", "450 TL"),
    ("İrmik", "450 TL"),
    ("Volkanik", "450 TL"),
    ("Kazandibi", "450 TL"),
    ("Fırın Helva", [(T, "450 TL"), (D, "800 TL")]),
    ("İncir Tatlısı", "450 TL"),
    ("Dondurma", "450 TL"),
    ("Serpme Meyve", [(T, "450 TL"), (D, "900 TL")]),
  ]),
  ("rakilar", "RAKILAR", "Rakılar", "İçecekler", [
    ("Sarızeybek", rakı("1.500 TL", "2.750 TL", "3.500 TL", "4.300 TL", "5.000 TL")),
    ("Yeni Rakı Yeni Seri", rakı("1.250 TL", "2.500 TL", "3.250 TL", "3.750 TL", "4.250 TL")),
    ("Beylerbeyi Göbek", rakı("1.500 TL", "2.750 TL", "3.500 TL", "4.300 TL", "5.000 TL")),
    ("Tekirdağ Göbek", rakı("1.500 TL", "2.750 TL", "3.500 TL", "4.300 TL", "5.000 TL")),
    ("Tek", "350 TL"),
    ("Duble", "550 TL"),
  ]),
  ("kirmizi", "KIRMIZI ŞARAPLAR", "Şaraplar", None, [
    ("Umurbey Cabernet Merlot", "2.250 TL"),
    ("Selendi Merlot", "5.550 TL", "2023"),
    ("Umurbey Kadeh", "600 TL"),
  ]),
  ("beyaz", "BEYAZ ŞARAPLAR", None, None, [
    ("Umurbey Sauvignon Blanc", "3.750 TL", "2020"),
    ("Yedi Bilgeler Anaxagoras", "5.250 TL"),
    ("Kayra Allure", "2.250 TL", "2019"),
    ("Cielo Sauvignon", "2.250 TL"),
    ("Cielo Kadeh", "600 TL"),
  ]),
  ("blush", "BLUSH", None, None, [
    ("Kızıl Alan", "3.150 TL"),
    ("Kızıl Alan Kadeh", "600 TL"),
  ]),
  ("biralar", "BİRALAR", "Biralar", None, [
    ("Efes Klasik", "350 TL", "33 cl"),
    ("Miller", "350 TL", "33 cl"),
    ("Heineken", "350 TL", "33 cl"),
    ("Corona", "350 TL", "35,5 cl"),
    ("Bitburger", "250 TL", "Alkolsüz"),
  ]),
  ("tekila", "TEKİLA", "Diğer İçkiler", None, [
    ("Patrón Silver", "7.000 TL"),
    ("Patrón Silver Shot", "450 TL"),
  ]),
  ("konyaklar", "KONYAKLAR", None, None, [
    ("Martell VSOP", "8.000 TL"),
    ("Hennessy VS", "5.000 TL"),
    ("Martell VSOP", "500 TL", "4 cl"),
    ("Martell VSOP", "800 TL", "8 cl"),
    ("Hennessy VS", "300 TL", "4 cl"),
    ("Hennessy VS", "500 TL", "8 cl"),
  ]),
  ("likorler", "LİKÖRLER", None, None, [
    ("Hare Kremalı Türk Kahvesi", "2.500 TL"),
    ("Hare Vişne", "2.500 TL"),
  ]),
  ("sampanya", "ŞAMPANYA", None, None, [("Cinzano Prosecco", "4.750 TL")]),
  ("gin", "GİN", None, None, [("Gordon's", "4.500 TL")]),
  ("viskiler", "VİSKİLER", None, None, [
    ("Hibiki", "16.500 TL"),
    ("Talisker 10 Yıl", "6.750 TL"),
    ("Chivas Regal 18 Yıl", "8.000 TL"),
    ("Black Label", "5.250 TL"),
    ("Aberlour 12 Yıl", "7.500 TL"),
    ("Lagavulin 8 Yıl", "7.500 TL"),
    ("Black Label Duble", "750 TL"),
    ("Black Label Tek", "500 TL"),
    ("Lagavulin 8 Yıl Tek", "650 TL"),
    ("Lagavulin 8 Yıl Duble", "950 TL"),
  ]),
  ("soft", "SOFT İÇECEKLER", "Soft İçecekler", None, [
    ("Coca Cola", "150 TL"),
    ("Coca Cola Zero", "150 TL"),
    ("Sprite", "150 TL"),
    ("Fanta", "150 TL"),
    ("Fusetea Şeftali", "150 TL"),
    ("Fusetea Limon", "150 TL"),
    ("Fusetea Ananas-Mango", "150 TL"),
    ("Cappy Vişne", "150 TL"),
    ("Cappy Şeftali", "150 TL"),
    ("Cappy Karışık", "150 TL"),
    ("Sade Soda", "100 TL"),
    ("Sıkma Limonlu Soda", "125 TL"),
    ("Küçük Şalgam", "200 TL"),
    ("Büyük Şalgam", "400 TL"),
    ("Büyük Su", "100 TL"),
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
