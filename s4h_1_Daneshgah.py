#barnamei baraye be dast avardane tedat nafarat va asami daneshjuyani ke
#faghat dar yek kelas sabte nam karde and
kelase_fizik = {"Amir", "Reza", "Amirreza", "Shayan", "Saeed", "Maryam", "Sara"}
kelase_riazi = {"Shayan", "Behnam", "Yasin", "Shaghayegh", "Ali", "Amir", "Maryam"}
asami_afrad_2_kelas = list(kelase_fizik) + list(kelase_riazi)
tedad_afrad_2_kelas = len(asami_afrad_2_kelas)
tedad_fizik = len(kelase_fizik)
tedad_riazi = len(kelase_riazi)
eshterak_2_kelas = kelase_fizik.intersection(kelase_riazi)
tedad_nafarat_moshtarak_2kelas = len(eshterak_2_kelas)
#asami va tedad kasani ke faghat dar kelase riazi va fizik hastand
faghat_fizik = kelase_fizik - eshterak_2_kelas
tedad_faghat_fizik = len(faghat_fizik)
faghat_riazi = kelase_riazi - eshterak_2_kelas
tedad_faghat_riazi = len(faghat_riazi)
#asami va tedad nafarati ke faghat yek kelas darand
faghat_yek_kelas = faghat_fizik.union(faghat_riazi)
tedad_afrad_faghat_yek_kelas = len(faghat_yek_kelas)
print(f"dar 2 kelase daneshgahi {tedad_afrad_2_kelas} nafar sabtenam karde and \
{tedad_fizik} nafar dar darse fizik va {tedad_riazi} nafar dar darse riazi sabtenam \
karde and va {tedad_nafarat_moshtarak_2kelas} daneshju be asami \
{eshterak_2_kelas} dar har do kelas sherkat karde and\nva in danehjuyan \
{tedad_faghat_fizik} nafar {faghat_fizik} faghat dar kelase fizik va \
{tedad_faghat_riazi} nafar {faghat_riazi} faghat dar kelase riazi sherkat \
karde and va dar natije in daneshjuyan\n\
{faghat_yek_kelas} be tedade \
{tedad_afrad_faghat_yek_kelas} nafar faghat dar yek kelas sherkat karde and.")
