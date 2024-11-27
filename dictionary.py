import os
atom_numaraları={
	"atomnumarası_1": "HYDROGEN: Hydrogen is colourless, odourless and tasteless, meaning it’s undetectable by human senses. It derives its name from hydrogenes meaning water-forming. Hydrogen is the lightest element in the periodic ",
	"atomnumarası_3": "Lithium-ion batteries are a type of battery that stores energy"
}
print("Sözlükte arama yapmak için bir kelime girin (çıkmak için 'q').")

while True:
    aranan_kelime = input("\nAramak istediğiniz kelime: ").strip()

    if aranan_kelime.lower() == "q":
        print("Programdan çıkılıyor...")
        break

    if aranan_kelime in atom_numaraları:
        print(f"\n{aranan_kelime.capitalize()}: {atom_numaraları[aranan_kelime]}")
    else:
        print(f"\n'{aranan_kelime}' sözlükte bulunamadı.")