document.addEventListener('DOMContentLoaded', function() {
    const viewWorkoutsLink = document.getElementById('view-workouts');
    const addWorkoutLink = document.getElementById('add-workout');
    const workoutsContainer = document.getElementById('workouts-container');
    const addWorkoutContainer = document.getElementById('add-workout-container');
    let workoutsFetched = false;

    viewWorkoutsLink.addEventListener('click', function(event) {
        event.preventDefault();

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
                            workoutDiv.className = 'workout';
                            workoutDiv.innerHTML = `
                                <h5>${workout.workout_name}</h5>
                                <p>${workout.workout_type}</p>
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

        if (addWorkoutContainer.style.display === 'block') {
            addWorkoutContainer.style.display = 'none';
        } else {
            addWorkoutContainer.style.display = 'block';
        }
    });
});