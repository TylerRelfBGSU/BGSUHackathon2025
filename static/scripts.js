// static/main.js

$(document).ready(function () {
	// Update severity label
	$('#severity').on('input', function () {
		const severityMap = { 1: 'Mild Pain', 2: 'Moderate Injury', 3: 'Major Injury' };
		$('#severity-label').text(severityMap[this.value]);
		loadExercises();
	});

	$('#body_part').on('change', loadExercises);

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

	// Severity label for messages
	$('#msg_severity').on('input', function () {
		const severityMap = { 1: 'Mild Pain', 2: 'Moderate Injury', 3: 'Major Injury' };
		$('#msg-severity-label').text(severityMap[this.value]);
		loadMessages();
	});

	$('#msg_body_part').on('change', loadMessages);

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
