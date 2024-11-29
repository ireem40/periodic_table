import os
atom_numaraları={
	"1": "HYDROGEN: Hydrogen is colourless, odourless and tasteless, meaning it’s undetectable by human senses. It derives its name from hydrogenes meaning water-forming. Hydrogen is the lightest element in the periodic ",
	"3": "Lithium: Lithium-ion batteries are a type of battery that stores energy by the movement of lithium ions within the battery.",
	"2": "Helium: Helium helps maintain the superconducting properties of magnets, which is why it is used to cool the magnets in MRI machines. Helium gas is used to inflate airbags in cars.",
	"8": "OXYGEN: Oxygen gas is colourless and odourless. Liquid oxygen is pale blue and can be attracted by a magnet. Oxygen is %21 of Earth’s atmosphere, and oxygen atoms make up %65 of the mass of the human body. Its ability to dissolve easily in water allows oxygen-breathing organisms to live in aquatic environments.",
	"9": "FLUORINE: Fluorine, the most reactive element, is most commonly found in nature as fluorite. Fluoride compounds are included in toothpaste to help prevent tooth decay. Fluorine, a toxic gas, reacts with hydrogen to form hydrofluoric acid HF, the only acid capable of dissolving glass.",
	"10": "NEON: Neon is the most stable element in the periodic table. Liquid neon is an important coolant.Neon is used in neon signs, which glow with a distinctive reddish orange colour.",
	"11": "SODIUM: The most well-known compound of sodium is sodium chloride, commonly used as table salt. Your body needs sodium for muscle and nerve function and to regulate water levels. It also facilitates the transmission of signals between nerve cells.",
	"12": "MAGNESIUM: Magnesium is found in the chlorophyll compound, which enables plants to perform photosynthesis. It is also used in fireworks due to its ability to burn with sparks when exposed to air. Additionally, it has a soothing effect on sore muscles.",
	"13": "ALUMINIUM: It takes its name from the Latin word alumen, which means bitter salt. Aluminum is the most abundant element in the Earth's crust, but its extraction is challenging, which increases its cost. While pure aluminum is not very durable, it becomes strong when alloyed with other metals. It is also an excellent conductor of electricity.",
	"14": "SILICON: Silicon is a widely used semiconductor found in almost all electronic devices, particularly in integrated circuits or chips. It derives its name from the Latin word silicis, meaning flint. Flint is composed of silicate rocks formed by the combination of silicon and oxygen.",
	"15": "PHOSPHORUS: Phosphorus forms part of the sugar-phosphate backbone of DNA and RNA. White phosphorus glows when exposed to oxygen and its name means light-bearer in Greek. Red phosphorus is found in the material on the sides of matchboxes, used to ignite matches.",
	"16": "SULFUR: Most sulfur is used to produce sulfuric acid, which is utilized in making fertilizers, detergents, and other useful compounds. Additionally, sulfur compounds in garlic and onions are responsible for their odor, and due to their sharp smell, they are added to natural gas to help detect leaks. Sulfur also plays a role in hardening natural rubber.",
	"17": "CHLORINE: Chlorine kills bacteria and other microbes so is used to treat drinking water and swimming pool water. Chlorine is used to produce the plastic PVC, used in window frames, drainpipes, and flooring. It derives its name from the Greek word chloros, meaning greenish-yellow. Chlorine is a toxic green yellow gas. It was used as a chemical weapon during World War I.",
	"18": "ARGON: It derives its name from the Greek word argos, meaning inactive. Argon is a poor conductor of heat and is used to fill the gaps between panes in double-glazed windows. It is used in welding torches to prevent the welded area from oxidizing and also to preserve historical documents by storing them in special containers filled with argon to prevent oxygen-induced degradation.",

}
print("enter a word to a  search (to exist 'q').")

while True:
    aranan_kelime = input("\nthe atom you search: ").strip()

    if aranan_kelime.lower() == "q":
        print("exiting the program...")
        break

    if aranan_kelime in atom_numaraları:
        print(f"\n{aranan_kelime.capitalize()}: {atom_numaraları[aranan_kelime]}")
    else:
        print(f"\n'{aranan_kelime}' not found.")