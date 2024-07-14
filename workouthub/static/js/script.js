document.addEventListener('DOMContentLoaded', function() {
    const viewWorkoutsLink = document.getElementById('view-workouts');
    const addWorkoutLink = document.getElementById('add-workout');
    const workoutsContainer = document.getElementById('workouts-container');
    const addWorkoutContainer = document.getElementById('add-workout-container');
    const addExerciseButton = document.getElementById('add-exercise-button');
    const exercisesContainer = document.getElementById('exercises-container');
    let exerciseCount = 1; // Initialize exercise count

    // Toggle visibility of the view workouts container
    viewWorkoutsLink.addEventListener('click', function(event) {
        event.preventDefault();
        addWorkoutContainer.style.display = 'none';
        if (workoutsContainer.style.display === 'block') {
            workoutsContainer.style.display = 'none';
        } else {
            workoutsContainer.style.display = 'block';
        }
    });

    // Toggle visibility of the add workout container
    addWorkoutLink.addEventListener('click', function(event) {
        event.preventDefault();
        workoutsContainer.style.display = 'none';
        if (addWorkoutContainer.style.display === 'block') {
            addWorkoutContainer.style.display = 'none';
        } else {
            addWorkoutContainer.style.display = 'block';
        }
    });

    // Add a new exercise field in the form
    addExerciseButton.addEventListener('click', function(event) {
        event.preventDefault();
        const newExerciseDiv = document.createElement('div');
        newExerciseDiv.className = 'exercise form-group';
        newExerciseDiv.innerHTML = `
            <h5>Exercise ${exerciseCount + 1}</h5>
            <label for="exercise_name_${exerciseCount}">Exercise Name</label>
            <input type="text" class="form-control" id="exercise_name_${exerciseCount}" name="exercise_name[]" required>
            <label for="sets_${exerciseCount}">Sets</label>
            <input type="number" class="form-control" id="sets_${exerciseCount}" name="sets[]" required>
            <label for="reps_${exerciseCount}">Reps</label>
            <input type="number" class="form-control" id="reps_${exerciseCount}" name="reps[]" required>
        `;
        exercisesContainer.appendChild(newExerciseDiv);
        exerciseCount++;
    });
});