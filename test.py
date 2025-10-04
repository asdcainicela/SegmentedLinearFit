import subprocess
import random
from datetime import datetime, timedelta
import os

# Lista de mensajes de commit aleatorios
COMMIT_MESSAGES = [
    "Refactor file",
    "Modify source code",
    "Bug fixed",
    "Update logic",
    "Minor changes",
    "Add file problem",
    "Cleanup code"
]

# Lista de fechas (YYYY-MM-DD)
FECHAS = [
    "2025-06-26",
    "2025-06-30","2025-07-01","2025-07-02","2025-07-03","2025-07-04",
    "2025-07-31","2025-07-06","2025-07-9", "2025-07-10",
    "2025-08-02","2025-08-03","2025-08-04","2025-08-05","2025-08-06",
    "2025-08-09","2025-08-10",
    "2025-08-14","2025-08-15","2025-08-16",
    "2025-08-19","2025-08-23",
    "2025-09-02","2025-09-05","2025-09-11","2025-09-20","2025-09-21",
    "2025-09-23","2025-09-25","2025-09-27","2025-09-29"
]

def git_commit(file_path, commit_message, commit_date):
    """Hace commit en git con fecha forzada."""
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Asegurar cambio en archivo
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n# Commit automático {commit_message} - {date_str}\n")

    # git add
    subprocess.run(["git", "add", file_path], check=True)

    # Variables de entorno (para que respete la fecha)
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date_str

    # git commit
    subprocess.run(
        ["git", "commit", "--date", date_str, "-m", commit_message],
        check=True,
        env=env
    )
    print(f"[ok ]Commit en {date_str}: {commit_message}")


if __name__ == "__main__":
    file = "test.txt"  # archivo dentro de tu repo (puede ser cualquiera)
    
    for fecha in FECHAS:
        # Generar hora aleatoria entre 09:00 y 18:00
        hora = random.randint(9, 18)
        minuto = random.randint(0, 59)
        segundo = random.randint(0, 59)

        dt = datetime.strptime(fecha, "%Y-%m-%d")
        dt = dt.replace(hour=hora, minute=minuto, second=segundo)

        # Mensaje aleatorio
        mensaje = random.choice(COMMIT_MESSAGES)

        # Hacer commit
        git_commit(file, mensaje, dt)
