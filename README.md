# Feladat kiírás

Egy közismereti versenyen a versenyzőknek 13+1, azaz összesen 14 tesztfeladatot tűznek ki. A versenyzőknek minden
feladat esetén négy megadott lehetőség (A, B, C, D) közül kell a helyes választ megjelölniük. A versenybizottság
garantálja, hogy tesztlapon minden kérdéshez pontosan egy helyes válasz tartozik. A kitöltött tesztlapokat
elektronikusan rögzítik, a visszaélések elkerülése végett a versenyzőket betűkből és számokból álló kóddal azonosítják.

<p>
A helyes megoldást és a versenyzők válaszait a valaszok.txt szöveges állomány tartalmazza. A fájl első sorában a helyes
válaszok szerepelnek. A fájl többi sora a versenyzők kódjával kezdődik, ezt egy szóköz, majd az adott versenyző által
adott válaszok sorozata követi. A versenyzők kódja 5 karakterből áll, 2 betűből és 3 számból. A válaszok a feladatokkal
egyező sorrendben, elválasztójel nélkül, nagybetűvel szerepelnek. Ha a versenyző egy kérdésre nem válaszolt, akkor annak
helyén X betű szerepel. Például:<br>
BCCCDBBBBCDAAA<br>
AB123 BXCDBBACACADBC<br>
AD995 BABCDABCBCBBBA<br>
…
</p>

A 2. kérdésre a helyes válasz a C volt, de erre a kérdésre az AB123 kódú versenyző nem válaszolt.

Írjon programot az alábbi feladatok megoldására:
1. Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait!
2. Jelenítse meg a képernyőn a mintának megfelelően, hány versenyző vett részt a tesztersenyen!
3. Kérje be egy versenyző azonosítóját és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat! Ha nincs
ilyen kód, akkor jelenítse meg: Ilyen kóddal nem indult versenyző.
4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba tegyen "+" jelet, ha az adott feladatot az
előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt. A kiíratást a mintának megfelelő módon
alakítsa ki! Ha olyan kód volt megadva, ami nem szerepel a listában, úgy az 1. versenyző megoldását vizsgálja!
5. Kérje be egy feladat sorszámát, majd határozza meg, hány versenyző adott a feladatra helyes megoldást, és ez a 
versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, 2 tizedesjegy pontossággal írassa ki.
6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat
5 pontot, a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt
nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzzel elválasztva az általa elért pontszámot
tartalmazza!
7. A versenyen a 3 legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 db.
első és 2 db. második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki 
a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát, pontszám szerint csökkenő sorrendben!

## Minta a szöveges kimenetek kialakításához

A képernyőre írt üzeneteknek tartalmilag meg kell felelniük az alábbi mintának. A képernyőre írást nem igénylő
feladatok esetén nem szükséges a feladat sorszámát sem kiíratnia.

<pre>
1. feladat: Az adatok beolvasása.
2. feladat: A versenyen 303 versenyző indult.
3. feladat: Kérem adja meg a versenyző azonosítóját: AB123
BXCDBBACACADBC
4. feladat: A helyes megoldás:
BCCCDBBBBCDAAA
+ +  +   +    
5. feladat: Kérem adja meg a feladat sorszámát: 10
A feladatra 111 fő, a versenyzők 36.63%-a adott helyes választ.
6. feladat: A versenyzők pontszámának meghatározása.
7. feladat: A verseny legjobbjai:
1. díj (56 pont): JO001
2. díj (52 pont): DG490
2. díj (52 pont): UA889
3. díj (49 pont): FX387
</pre>

## Megoldás közben ügyeljen az alábbiakra

- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát!
- Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, milyen értéket vár!
- Ellenőrizze a felhasználó által megadott adatok helyességét, érvényességét!

# Feladat megoldása és benyújtás

1. A megoldáshoz hozzon létre új projektet ***ep21c2k*** néven: _File / New Project..._
2. Töltse le a projekt mappájába:
    - ***README.md*** (jelen feladatkiírás)
    - ***valaszok.txt***
3. Tötlse fel a projektet egy új repository-ba, ***ep21c2k*** néven: _VCS / Share Project on GitHub_
4. A feladat megoldására 3 óra áll rendelkezésre.
5. A feladat befejezésekor, de legkésőbb a 3. óra leteltekor kommitolja fel a megoldást.