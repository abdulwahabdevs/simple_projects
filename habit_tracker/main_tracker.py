import pandas as pd
from datetime import datetime
from habit_tracker import track_habit, Habit
from tabulate import tabulate

def main():
    habits: list[Habit] = [
        track_habit('Fizzy Drinks', datetime(2025, 1, 14, 8), cost=2_300, minutes_used=5),
        track_habit('CS2', datetime(2025, 1, 14, 8), cost=1_000, minutes_used=30),
        track_habit('Smoking', datetime(2025, 1, 14, 8), cost=4_500, minutes_used=5)
    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == '__main__':
    main()
