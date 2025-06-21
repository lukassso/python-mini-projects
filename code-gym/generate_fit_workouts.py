
# Przykład kodu Python do generowania pliku .FIT dla Garmin Forerunner 745
# Wymaga instalacji: pip install fit-tool

from fit_tool.fit_file import FitFile
from fit_tool.profile.messages.file_id_message import FileIdMessage
from fit_tool.profile.messages.workout_message import WorkoutMessage  
from fit_tool.profile.messages.workout_step_message import WorkoutStepMessage
from datetime import datetime

def create_garmin_workout_fit(workout_name, steps_config):
    """
    Tworzy plik .FIT z treningiem dla Garmin

    Args:
        workout_name (str): Nazwa treningu
        steps_config (list): Lista kroków treningu
    """

    # Utwórz nowy plik FIT
    fit_file = FitFile()

    # File ID Message (wymagane dla każdego pliku FIT)
    file_id = FileIdMessage()
    file_id.type = 5  # Workout file type
    file_id.manufacturer = 1  # Garmin
    file_id.product = 1234
    file_id.time_created = int(datetime.now().timestamp())
    fit_file.add(file_id)

    # Workout Message
    workout = WorkoutMessage()
    workout.wkt_name = workout_name
    workout.sport = 1  # Running
    workout.num_valid_steps = len(steps_config)
    fit_file.add(workout)

    # Dodaj kroki treningu
    for i, step_config in enumerate(steps_config):
        step = WorkoutStepMessage()
        step.message_index = i
        step.wkt_step_name = step_config['name']
        step.duration_type = step_config['duration_type']  # 0=time, 1=distance, etc.
        step.duration_value = step_config['duration_value']
        step.target_type = step_config['target_type']  # 1=heart_rate
        step.target_hr_zone = step_config['target_zone']
        step.intensity = step_config['intensity']  # 0=active, 1=rest, 2=warmup, 3=cooldown

        fit_file.add(step)

    return fit_file

# Przykład 1: Bieg spokojny 80 minut (Tydzień 5)
def create_week5_easy_run():
    """Tworzy trening z tygodnia 5 - bieg spokojny 80 min"""

    steps = [
        {
            'name': 'Rozgrzewka',
            'duration_type': 0,  # Time
            'duration_value': 600,  # 10 minut = 600 sekund
            'target_type': 1,  # Heart rate
            'target_zone': 1,  # Strefa Z1
            'intensity': 2  # Warmup
        },
        {
            'name': 'Bieg spokojny',
            'duration_type': 0,  # Time
            'duration_value': 3600,  # 60 minut = 3600 sekund
            'target_type': 1,  # Heart rate
            'target_zone': 2,  # Strefa Z2
            'intensity': 0  # Active
        },
        {
            'name': 'Schłodzenie',
            'duration_type': 0,  # Time
            'duration_value': 600,  # 10 minut = 600 sekund
            'target_type': 1,  # Heart rate
            'target_zone': 1,  # Strefa Z1
            'intensity': 3  # Cooldown
        }
    ]

    fit_file = create_garmin_workout_fit("T05_Bieg_spokojny_80min", steps)
    fit_file.to_file("T05_Bieg_spokojny_80min.fit")
    print("✅ Utworzono: T05_Bieg_spokojny_80min.fit")

# Przykład 2: Bieg progresywny 110 minut (Tydzień 10)
def create_week10_progressive_run():
    """Tworzy trening z tygodnia 10 - bieg progresywny 110 min"""

    steps = [
        {
            'name': 'Rozgrzewka',
            'duration_type': 0,
            'duration_value': 900,  # 15 minut
            'target_type': 1,
            'target_zone': 1,  # Z1
            'intensity': 2
        },
        {
            'name': 'Faza bazowa',
            'duration_type': 0,
            'duration_value': 1920,  # 32 minuty
            'target_type': 1,
            'target_zone': 2,  # Z2
            'intensity': 0
        },
        {
            'name': 'Faza tempowa',
            'duration_type': 0,
            'duration_value': 1920,  # 32 minuty
            'target_type': 1,
            'target_zone': 3,  # Z3
            'intensity': 0
        },
        {
            'name': 'Faza progowa',
            'duration_type': 0,
            'duration_value': 960,  # 16 minut
            'target_type': 1,
            'target_zone': 4,  # Z4
            'intensity': 0
        },
        {
            'name': 'Schłodzenie',
            'duration_type': 0,
            'duration_value': 900,  # 15 minut
            'target_type': 1,
            'target_zone': 1,  # Z1
            'intensity': 3
        }
    ]

    fit_file = create_garmin_workout_fit("T10_Bieg_narastajacy_110min", steps)
    fit_file.to_file("T10_Bieg_narastajacy_110min.fit")
    print("✅ Utworzono: T10_Bieg_narastajacy_110min.fit")

# Funkcja wsadowa do tworzenia wszystkich treningów
def create_all_workouts():
    """Tworzy wszystkie 20 treningów z planu"""

    # Plan treningów (skrócona wersja dla przykładu)
    all_workouts = [
        ("T01_Bieg_spokojny_40min", [
            {'name': 'Rozgrzewka', 'duration_type': 0, 'duration_value': 600, 'target_type': 1, 'target_zone': 1, 'intensity': 2},
            {'name': 'Bieg spokojny', 'duration_type': 0, 'duration_value': 1800, 'target_type': 1, 'target_zone': 2, 'intensity': 0},
            {'name': 'Schłodzenie', 'duration_type': 0, 'duration_value': 600, 'target_type': 1, 'target_zone': 1, 'intensity': 3}
        ]),
        # ... więcej treningów można dodać tutaj
    ]

    for workout_name, steps in all_workouts:
        fit_file = create_garmin_workout_fit(workout_name, steps)
        fit_file.to_file(f"{workout_name}.fit")
        print(f"✅ Utworzono: {workout_name}.fit")

if __name__ == "__main__":
    print("🏃‍♂️ Generowanie plików .FIT dla Garmin Forerunner 745")
    print("=" * 50)

    # Utwórz przykładowe treningi
    create_week5_easy_run()
    create_week10_progressive_run()

    print("\n📱 Instrukcje wgrania do zegarka:")
    print("1. Podłącz Forerunner 745 przez USB")
    print("2. Skopiuj pliki .fit do folderu GARMIN/NEWFILES/")
    print("3. Bezpiecznie odłącz zegarek")
    print("4. Treningi będą dostępne w: Menu → Trening → Moje treningi")
    
    
# Teraz przygotujemy pełny plan do eksportu w formacie TCX-ready (czytelny dla Garmina)
# Wygenerujemy uproszczoną tabelę, która może zostać potem skonwertowana do TCX lub FIT

# Przygotujmy 16-tygodniowy rzeczywisty plan na podstawie inteligentnego zagęszczenia

# Przykładowa wersja planu - uproszczony mockup do eksportu:
compressed_plan = [
    ("Week 1", "Easy Run", 45, "Zone 2"),
    ("Week 1", "Intervals 6x400m", 36, "Zone 4"),
    ("Week 1", "Long Run", 80, "Zone 2"),
    ("Week 2", "Easy Run", 50, "Zone 2"),
    ("Week 2", "Tempo Run", 30, "Zone 3"),
    ("Week 2", "Long Run", 90, "Zone 2"),
    ("Week 3", "Easy Run", 45, "Zone 2"),
    ("Week 3", "Intervals 8x400m", 40, "Zone 4"),
    ("Week 3", "Long Run", 100, "Zone 2"),
    ("Week 4", "Easy Run", 50, "Zone 2"),
    ("Week 4", "Tempo Run", 40, "Zone 3"),
    ("Week 4", "Long Run", 110, "Zone 2"),
    ("Week 5", "Easy Run", 45, "Zone 2"),
    ("Week 5", "Intervals 10x400m", 42, "Zone 4"),
    ("Week 5", "Long Run", 120, "Zone 2"),
    ("Week 6", "Easy Run", 50, "Zone 2"),
    ("Week 6", "Tempo Run", 50, "Zone 3"),
    ("Week 6", "Long Run", 130, "Zone 2"),
    ("Week 7", "Easy Run", 45, "Zone 2"),
    ("Week 7", "Intervals 12x400m", 48, "Zone 4"),
    ("Week 7", "Long Run", 135, "Zone 2"),
    ("Week 8", "Easy Run", 50, "Zone 2"),
    ("Week 8", "Tempo Run", 55, "Zone 3"),
    ("Week 8", "Long Run", 140, "Zone 2"),
    ("Week 9", "Easy Run", 45, "Zone 2"),
    ("Week 9", "Intervals 8x600m", 40, "Zone 4"),
    ("Week 9", "Long Run", 150, "Zone 2"),
    ("Week 10", "Easy Run", 50, "Zone 2"),
    ("Week 10", "Tempo Run", 60, "Zone 3"),
    ("Week 10", "Long Run", 120, "Zone 2"),
    ("Week 11", "Easy Run", 45, "Zone 2"),
    ("Week 11", "Intervals 10x600m", 42, "Zone 4"),
    ("Week 11", "Long Run", 100, "Zone 2"),
    ("Week 12", "Easy Run", 50, "Zone 2"),
    ("Week 12", "Tempo Run", 50, "Zone 3"),
    ("Week 12", "Long Run", 90, "Zone 2"),
    ("Week 13", "Easy Run", 45, "Zone 2"),
    ("Week 13", "Intervals 8x400m", 36, "Zone 4"),
    ("Week 13", "Long Run", 80, "Zone 2"),
    ("Week 14", "Easy Run", 40, "Zone 2"),
    ("Week 14", "Tempo Run", 30, "Zone 3"),
    ("Week 14", "Long Run", 60, "Zone 2"),
    ("Week 15", "Easy Run", 35, "Zone 2"),
    ("Week 15", "Easy Run", 30, "Zone 2"),
    ("Week 15", "Long Run", 45, "Zone 2"),
    ("Week 16", "Race Day", 240, "Zone 3"),
]

# Konwersja do DataFrame
export_df = pd.DataFrame(compressed_plan, columns=["Week", "Workout Type", "Duration (min)", "Target HR Zone"])

# Zapiszemy jako CSV
export_path = "/mnt/data/marathon_plan_16_weeks.csv"
export_df.to_csv(export_path, index=False)

export_path
