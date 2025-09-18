DAYS = ["Hënë", "Martë", "Mërkurë", "Enjte", "Premte", "Shtunë", "Diel"]

def read_goals():
    goals = []
    for day in DAYS:
        while True:
            inp = input(f"Jep objektivin e hapave për {day}: ")
            try:
                val = int(inp)
                if val <= 0:
                    print("Gabim! Jep një numër pozitiv.")
                    continue
                goals.append(val)
                break
            except ValueError:
                print("Gabim! Jep një numër të plotë.")
    return goals

def read_steps_and_evaluate(goals):
    steps = []
    for i, day in enumerate(DAYS):
        while True:
            inp = input(f"Jep hapat e bërë për {day}: ")
            try:
                val = int(inp)
                if val < 0:
                    print("Gabim! Jep një numër pozitiv.")
                    continue
                steps.append(val)
                if val >= goals[i]:
                    print("✔ Arritur")
                else:
                    print(f"✘ Jo e arritur (mungojnë {goals[i] - val} hapa)")
                break
            except ValueError:
                print("Gabim! Jep një numër të plotë.")
    return steps

def print_report(goals, steps):
    print("\nDita      Objektivi    Realizimi   Statusi")
    print("----------------------------------------")
    achieved = 0
    total_goal = sum(goals)
    total_steps = sum(steps)
    for i in range(7):
        status = "✔" if steps[i] >= goals[i] else f"✘ (mungojnë {goals[i] - steps[i]})"
        if steps[i] >= goals[i]:
            achieved += 1
        print(f"{DAYS[i]:9}{goals[i]:10}{steps[i]:11}{status}")
    perc = (total_steps / total_goal * 100) if total_goal > 0 else 0
    print(f"\nObjective achieved: {achieved}/7 dite")
    print(f"Total steps taken / Total objective: {total_steps} / {total_goal}")
    print(f"Përqindja ndaj objektivit javor: {perc:.2f}%")

def main():
    goals = read_goals()
    steps = read_steps_and_evaluate(goals)
    while True:
        print("\nMENU:")
        print("1) Shfaq raportin javor")
        print("2) Ndrysho objektivat dhe rifillo futjen e hapave")
        print("3) Dil")
        try:
            choice = int(input("Zgjedhja: "))
        except ValueError:
            print("Gabim! Jep një numër nga 1 deri në 3.")
            continue

        if choice == 1:
            print_report(goals, steps)
        elif choice == 2:
            goals = read_goals()
            steps = read_steps_and_evaluate(goals)
        elif choice == 3:
            print("Programi u përfundua.")
            break
        else:
            print("Gabim! Jep një numër nga 1 deri në 3.")

if __name__ == "__main__":
    main()
