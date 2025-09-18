def lexo_objektivat():
    days = ["Hënë", "Martë", "Mërkurë", "Enjte", "Premte", "Shtunë", "Diel"]
    obj_hene = obj_marte = obj_merkure = obj_enjte = obj_premte = obj_shtune = obj_diel = 0
    for i, day in enumerate(days):
        while True:
            inp = input(f"Jep objektivin e hapave për {day}: ")
            try:
                val = int(inp)
                if val <= 0:
                    print("Gabim! Jep një numër pozitiv.")
                    continue
                if i == 0:
                    obj_hene = val
                elif i == 1:
                    obj_marte = val
                elif i == 2:
                    obj_merkure = val
                elif i == 3:
                    obj_enjte = val
                elif i == 4:
                    obj_premte = val
                elif i == 5:
                    obj_shtune = val
                elif i == 6:
                    obj_diel = val
                break
            except ValueError:
                print("Gabim! Jep një numër të plotë.")
    return obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel


def lexo_hapat_dhe_vlereso(obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel):
    days = ["Hënë", "Martë", "Mërkurë", "Enjte", "Premte", "Shtunë", "Diel"]
    objektivat = [obj_hene, obj_marte, obj_merkure, obj_enjte, obj_premte, obj_shtune, obj_diel]
    hap_hene = hap_marte = hap_merkure = hap_enjte = hap_premte = hap_shtune = hap_diel = 0

    for i, day in enumerate(days):
        while True:
            inp = input(f"Jep hapat e bërë për {day}: ")
            try:
                val = int(inp)
                if val < 0:
                    print("Gabim! Jep një numër pozitiv.")
                    continue
                if i == 0:
                    hap_hene = val
                elif i == 1:
                    hap_marte = val
                elif i == 2:
                    hap_merkure = val
                elif i == 3:
                    hap_enjte = val
                elif i == 4:
                    hap_premte = val
                elif i == 5:
                    hap_shtune = val
                elif i == 6:
                    hap_diel = val

                if val >= objektivat[i]:
                    print("✔ Arritur")
                else:
                    mungon = objektivat[i] - val
                    print(f"✘ Jo e arritur (mungojnë {mungon} hapa)")
                break
            except ValueError:
                print("Gabim! Jep një numër të plotë.")
    return hap_hene, hap_marte, hap_merkure, hap_enjte, hap_premte, hap_shtune, hap_diel


def main():
    # Initial input
    obj = lexo_objektivat()
    haps = lexo_hapat_dhe_vlereso(*obj)
    while True:
        print("\nMENU:")
        print("1) Shfaq raportin javor")
        print("2) Ndrysho objektivat dhe rifillo futjen e hapave")
        print("3) Dil")
        zgjedhja = input("Zgjedhja: ")
        try:
            zgjedhja_num = int(zgjedhja)
        except ValueError:
            print("Gabim! Jep një numër nga 1 deri në 3.")
            continue

        match zgjedhja_num:
            case 1:
                # Prepare day names
                days = ["Hënë", "Martë", "Mërkurë", "Enjte", "Premte", "Shtunë", "Diel"]
                objektivat = obj
                hapat = haps
                print("\nDita      Objektivi    Realizimi   Statusi")
                print("----------------------------------------")
                arritur = 0
                total_obj = 0
                total_hapa = 0
                for i in range(7):
                    status = "✔" if hapat[i] >= objektivat[i] else f"✘ (mungojnë {objektivat[i] - hapat[i]})"
                    if hapat[i] >= objektivat[i]:
                        arritur += 1
                    total_obj += objektivat[i]
                    total_hapa += hapat[i]
                    print(f"{days[i]:9}{objektivat[i]:10}{hapat[i]:11}{status}")
                perc = (total_hapa / total_obj * 100) if total_obj > 0 else 0
                print(f"\nObjective achieved: {arritur}/7 dite")
                print(f"Total steps taken / Total objective: {total_hapa} / {total_obj}")
                print(f"Përqindja ndaj objektivit javor: {perc:.2f}%")
            case 2:
                obj = lexo_objektivat()
                haps = lexo_hapat_dhe_vlereso(*obj)
            case 3:
                print("Programi u përfundua.")
                break
            case _:
                print("Gabim! Jep një numër nga 1 deri në 3.")

    # To run:


main()