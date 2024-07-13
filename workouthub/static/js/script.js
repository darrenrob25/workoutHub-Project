document.addEventListener('DOMContentLoaded', function() {
    const viewWorkoutsLink = document.getElementById('view-workouts');
    const addWorkoutLink = document.getElementById('add-workout');
    const workoutsContainer = document.getElementById('workouts-container');
    const addWorkoutContainer = document.getElementById('add-workout-container');
    const addExerciseButton = document.getElementById('add-exercise-button');
    const exercisesContainer = document.getElementById('exercises-container');
    let exerciseCount = 1; // Initialize exercise count
    let workoutsFetched = false;

    viewWorkoutsLink.addEventListener('click', function(event) {
        event.preventDefault();

        // Hide the add workout container when view workouts is clicked
        addWorkoutContainer.style.display = 'none';

        if (workoutsContainer.style.display === 'block') {
            workoutsContainer.style.display = 'none';
        } else {
            if (!workoutsFetched) {
                fetch('/workouts')
                    .then(response => response.json())
                    .then(data => {
                        if (data.error) {
                            alert(data.error);
                            return;
                        }

                        const workoutsList = document.getElementById('workouts-list');
                        workoutsList.innerHTML = '';
                        
                        data.forEach(workout => {
                            const workoutDiv = document.createElement('div');
                            workoutDiv.className = 'col-md-6 col-lg-6 mb-4';
                            workoutDiv.innerHTML = `
                            <div class="your-workout-container bg-dark p-3 text-white">
                                <h5>${workout.workout_name}</h5>
                                <p>${workout.workout_type}</p>
                                ${workout.exercises.map(exercise => `
                                    <p>${exercise.exercise_name}: ${exercise.sets} sets, ${exercise.reps} reps</p>
                                `).join('')}
                                <div class="row">
                                <a href="#"class="edit-button col"> <i class="fa fa-arrow-right" aria-hidden="true"></i> Edit Workout</a>
                                <a type="submit"href="{{ url_for('delete_workout', workout_id=workout.id)}}" class="delete-button col"><i class="fa fa-minus" aria-hidden="true"></i> Delete Workout</a>
                                </div>
                            </div>
                            `;
                            workoutsList.appendChild(workoutDiv);
                        });

                        workoutsFetched = true;
                    })
                    .catch(error => {
                        console.error('Error fetching workouts:', error);
                    });
            }
            workoutsContainer.style.display = 'block';
        }
    });

    addWorkoutLink.addEventListener('click', function(event) {
        event.preventDefault();

        // Hide the workouts container when add workout is clicked
        workoutsContainer.style.display = 'none';

        if (addWorkoutContainer.style.display === 'block') {
            addWorkoutContainer.style.display = 'none';
        } else {
            addWorkoutContainer.style.display = 'block';
        }
    });

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