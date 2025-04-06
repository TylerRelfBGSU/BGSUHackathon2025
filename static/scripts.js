$(document).ready(function() {
	const labels = ['Mild Pain', 'Moderate Injury', 'Major Injury'];

	$('#severity').on('input', function() {
		const severity = $(this).val();
		$('#severity-label').text(labels[severity - 1]);
	});

	$('#filterForm select, #severity').change(function() {
		const bodyPart = $('#body_part').val();
		const severity = $('#severity').val();

		$.post('/get_exercises', { body_part: bodyPart, severity: severity }, function(data) {
			$('#exercisesList').empty();

			if (data.length > 0) {
				data.forEach(function(exercise) {
					$('#exercisesList').append(
						`<li>
							<strong>${exercise.exercise}</strong><br>
							<small><em>(${exercise.body_part} - ${exercise.severity})</em></small><br>
							${exercise.description}
						</li>`
					);
				});
			} else {
				$('#exercisesList').append('<li>No exercises found for the selected options.</li>');
			}
		});
	});
});
