def main():
    name = input("What is your name? ").strip()
    activity = input("What activity helps you relax? ").strip()
    minutes_text = input("How many whole minutes will you study today? ").strip()

    if name == "":
        name = "friend"
    if activity == "":
        activity = "taking a quiet break"

    if minutes_text.isdigit():
        study_minutes = int(minutes_text)
    else:
        study_minutes = 0
        print("I could not read that time, so I will make a zero-minute plan.")

    focus_blocks = study_minutes // 25
    leftover_minutes = study_minutes % 25
    suggested_break = study_minutes // 5
    name_badge = name + " the curious learner"

    print("\nHi, " + name_badge + "!")
    print(
        "I am arshtyi, a Python student who likes quiet reading between study sessions."
    )

    if study_minutes >= 25:
        print(
            f"Your {study_minutes}-minute plan contains {focus_blocks} complete "
            f"25-minute focus block(s) and {leftover_minutes} extra minute(s)."
        )
    else:
        print(
            f"A {study_minutes}-minute session is a gentle start; "
            "one full focus block takes 25 minutes."
        )

    if "read" in activity.lower() or "book" in activity.lower():
        print(f"You relax by {activity}, so we have reading in common!")
    else:
        print(f"You relax by {activity}. I would use that as a reward after studying.")

    if study_minutes > 0:
        print(f"Afterward, consider a {suggested_break}-minute break. Good luck!")
    else:
        print("Choose a positive study time next time and I will build a full plan.")


if __name__ == "__main__":
    main()
