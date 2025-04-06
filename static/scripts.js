$(document).ready(function () {
	// Initially hide the sections until a body part is selected
	$('#messageResults').hide();
	$('.container h2').hide();
	$('#exercisesList').empty();
	$('#messagesList').empty();

	// Update severity label for exercises
	$('#severity').on('input', function () {
		const severityMap = { 1: 'Mild Pain', 2: 'Moderate Injury', 3: 'Major Injury' };
		$('#severity-label').text(severityMap[this.value]);
		loadExercises();
	});

	// Update severity label for messages
	$('#msg_severity').on('input', function () {
		const severityMap = { 1: 'Mild Pain', 2: 'Moderate Injury', 3: 'Major Injury' };
		$('#msg-severity-label').text(severityMap[this.value]);
		loadMessages();
	});

	// Handle changes in body part selection for exercises
	$('#body_part').on('change', function () {
		const bodyPart = $(this).val();
		if (bodyPart) {
			$('.container h2').show(); // Show "Recommended Exercises"
			loadExercises(); // Load exercises when a body part is selected
		} else {
			// Clear the exercises section when no body part is selected
			$('#exercisesList').empty();
			$('.container h2').hide(); // Hide "Recommended Exercises" heading
		}
	});

	// Handle changes in body part selection for messages
	$('#msg_body_part').on('change', function () {
		const bodyPart = $(this).val();
		if (bodyPart) {
			$('#messageResults').show(); // Show "Messages" section when a body part is selected
			loadMessages(); // Load messages when a body part is selected
		} else {
			// Clear the messages section when no body part is selected
			$('#messagesList').empty();
			$('#messageResults').hide(); // Hide "Messages" section when no body part is selected
		}
	});

	// Load exercises based on the selected body part and severity
	function loadExercises() {
		const bodyPart = $('#body_part').val();
		const severity = $('#severity').val();

		if (bodyPart && severity) {
			$.post('/get_exercises', { body_part: bodyPart, severity }, function (data) {
				const list = $('#exercisesList');
				list.empty();
				if (data.length === 0) {
					list.append('<li>No exercises found for this selection.</li>');
				} else {
					data.forEach(item => {
						list.append(`<li><strong>${item.exercise}</strong><br>${item.description}</li>`);
					});
				}
			});
		}
	}

	// Load messages based on the selected body part and severity
	function loadMessages() {
		const bodyPart = $('#msg_body_part').val();
		const severity = $('#msg_severity').val();

		if (bodyPart && severity) {
			$.post('/get_messages', { body_part: bodyPart, severity }, function (messages) {
				const list = $('#messagesList');
				list.empty();
				if (messages.length === 0) {
					list.append('<li>No messages yet for this selection.</li>');
				} else {
					messages.forEach(msg => list.append(`<li>${msg}</li>`));
				}
			});
		}
	}

	// Submit new message
	$('#messageForm').on('submit', function (e) {
		e.preventDefault();
		const data = {
			body_part: $('#msg_body_part').val(),
			severity: $('#msg_severity').val(),
			message: $('#messageText').val()
		};

		if (!data.body_part || !data.severity || !data.message.trim()) return;

		$.post('/submit_message', data, function () {
			$('#messageText').val('');
			loadMessages();
		});
	});
});
