document.addEventListener('DOMContentLoaded', function() {
    const viewWorkoutsLink = document.getElementById('view-workouts');
    const addWorkoutLink = document.getElementById('add-workout');
    const workoutsContainer = document.getElementById('workouts-container');
    const addWorkoutContainer = document.getElementById('add-workout-container');
    const addExerciseButton = document.getElementById('add-exercise-button');
    const exercisesContainer = document.getElementById('exercises-container');

    // Get the existing number of exercises for the form
    let exerciseCount = document.querySelectorAll('#exercises-container .exercise').length;

    // Toggle the view workouts container
    if (viewWorkoutsLink) {
        viewWorkoutsLink.addEventListener('click', function(event) {
            event.preventDefault();
            addWorkoutContainer.style.display = 'none';
            if (workoutsContainer.style.display === 'block') {
                workoutsContainer.style.display = 'none';
            } else {
                workoutsContainer.style.display = 'block';
            }
        });
    }

    // Toggle the add workout container
    if (addWorkoutLink) {
        addWorkoutLink.addEventListener('click', function(event) {
            event.preventDefault();
            workoutsContainer.style.display = 'none';
            if (addWorkoutContainer.style.display === 'block') {
                addWorkoutContainer.style.display = 'none';
            } else {
                addWorkoutContainer.style.display = 'block';
            }
        });
    }

    // Add a new exercise field in the form
    if (addExerciseButton) {
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
                <button type="button" class="btn btn-danger delete-exercise-button">Remove Exercise</button> <!-- Added delete button -->
            `;
            exercisesContainer.appendChild(newExerciseDiv);
            exerciseCount++;
        });
    }

    // Added event listeners for added form elements
    exercisesContainer.addEventListener('click', function(event) {
        if (event.target && event.target.matches('.delete-exercise-button')) {
            event.preventDefault();
            const exerciseDiv = event.target.closest('.exercise');
            if (exerciseDiv) {
                exerciseDiv.remove();
                // Recalculate exercise count
                exerciseCount = document.querySelectorAll('#exercises-container .exercise').length;
                updateExerciseLabels(); // Update the exercise labels
            }
        }
    });

    // Updating exercise labels after deletion to ensure numbering is correct
    function updateExerciseLabels() {
        document.querySelectorAll('#exercises-container .exercise').forEach((div, index) => {
            div.querySelector('h5').textContent = `Exercise ${index + 1}`;
            div.querySelector('label[for^="exercise_name_"]').setAttribute('for', `exercise_name_${index}`);
            div.querySelector('input[name="exercise_name[]"]').setAttribute('id', `exercise_name_${index}`);
            div.querySelector('input[name="exercise_name[]"]').setAttribute('name', `exercise_name[]`);
            div.querySelector('label[for^="sets_"]').setAttribute('for', `sets_${index}`);
            div.querySelector('input[name="sets[]"]').setAttribute('id', `sets_${index}`);
            div.querySelector('input[name="sets[]"]').setAttribute('name', `sets[]`);
            div.querySelector('label[for^="reps_"]').setAttribute('for', `reps_${index}`);
            div.querySelector('input[name="reps[]"]').setAttribute('id', `reps_${index}`);
            div.querySelector('input[name="reps[]"]').setAttribute('name', `reps[]`);
        });
    }

    // Initialize event listeners for delete button
    document.querySelectorAll('#exercises-container .delete-exercise-button').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const exerciseDiv = button.closest('.exercise');
            if (exerciseDiv) {
                exerciseDiv.remove();
                // Recalculate exercise count
                exerciseCount = document.querySelectorAll('#exercises-container .exercise').length;
                updateExerciseLabels(); // Update the exercise labels
            }
        });
    });

    const form = document.querySelector('#add-workout-form, #edit-workout-form');
    if (form) {
        form.addEventListener('submit', function(event) {
        });
    }
});

// Show and Hide Modal

document.addEventListener('DOMContentLoaded', function () {
    // Function to set up the delete modal
    function setupDeleteModal(button) {
      const workoutId = button.getAttribute('data-workout-id');
      const actionUrl = button.getAttribute('data-action-url');

      // Set the form's action URL and workout ID
      const form = document.getElementById('confirmDeleteForm');
      form.action = actionUrl;
      document.getElementById('modal_workout_id').value = workoutId;

      // Show the modal
      $('#confirmDeleteModal').modal('show');
    }

    // Attach event listener to all delete buttons
    document.querySelectorAll('.delete-button').forEach(button => {
      button.addEventListener('click', function () {
        setupDeleteModal(this);
      });
    });
  });