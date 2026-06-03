
from pyscript import document, window, when

@when("click", "#continue-button")
def workout_page_selector(event):
    workout = document.querySelector('input[name="workout-selection"]:checked')
    duration = document.querySelector('input[name="workout-duration"]:checked')
    difficulty = document.querySelector('input[name="workout-difficulty"]:checked')

    if not workout or not duration or not difficulty:
        window.alert("Please select all options")
        return

    w = workout.value.strip()
    t = duration.value.strip()
    d = difficulty.value.strip()

    if w == "P":
        folder = "plyometrics"
    elif w == "UB":
        folder = "upper_body"
    elif w == "LB":
        folder = "lower_body"

    url = f"workout_selection_kayson/{folder}/{w}-{t}-{d}-workout.html"
    window.location.href = url


