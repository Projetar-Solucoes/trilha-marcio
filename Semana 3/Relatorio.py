def relatorio(characters):
    if len(characters) != 0:
        print("----------------- RELATORIO -----------------")

        high_hp = -1
        high_level = -1
        media_exp = 0
        name_character = ""

        print(f"Existem {len(characters)} personagens")

        for personagem in characters:
            if personagem["HP"] > high_hp:
                high_hp = personagem["HP"]
                name_character = personagem["NAME"]

        print(f"O personagem com maior HP é {name_character}")
        print(f"HP: {high_hp}")

        for personagem in characters:
            if personagem["LEVEL"] > high_level:
                high_level = personagem["LEVEL"]
                name_character = personagem["NAME"]

        print(f"O personagem com maior level é {name_character}")
        print(f"Level: {high_level}")

        for personagem in characters:
            media_exp += personagem["EXP"]

        print(f"A média de experiência/XP é de: {media_exp / len(characters)}")

    else:
        print("Não há personagens cadastrados")

    input("Enter para sair do relatório: ")