$(document).ready(function() {
    $('#registrationForm').on('submit', function(event) {
        event.preventDefault(); 
        $('#errorMessages').empty(); 

        let valid = true;
        let errorMessages = [];

        const usernameRegex = /^[a-zA-Z0-9]{5,12}$/;
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!%.&])[A-Za-z\d!%.&]{5,12}$/;
        const phoneRegex = /^(\(\d{3}\) |\d{3}-|\d{10}|\d{3} \d{3} \d{4})$/;
        const postalCodeRegex = /^\d{5}(-\d{4})?$/;
        const emailRegex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;

        function showError(element, message) {
            $(element).css('border', '2px solid red');
            errorMessages.push(message);
            valid = false;
        }

        function clearError(element) {
            $(element).css('border', '');
        }

        $('#registrationForm').find('input').each(function() {
            const field = $(this);
            const value = field.val().trim();
            const id = field.attr('id');

            clearError(field);

            if (!value) {
                showError(field, `${id} is required.`);
            } else {
                switch (id) {
                    case 'username':
                        if (!usernameRegex.test(value)) showError(field, 'Username must be 5-12 characters.');
                        break;
                    case 'password':
                        if (!passwordRegex.test(value)) showError(field, 'Password must be 5-12 characters with at least one uppercase, one lowercase, one numeric, and one symbol (!, %, ., &).');
                        break;
                    case 'confirmPassword':
                        if (value !== $('#password').val()) showError(field, 'Passwords do not match.');
                        break;
                    case 'email':
                        if (!emailRegex.test(value)) showError(field, 'Invalid email address.');
                        break;
                    case 'confirmEmail':
                        if (value !== $('#email').val()) showError(field, 'Email addresses do not match.');
                        break;
                    case 'phone':
                        if (!phoneRegex.test(value)) showError(field, 'Invalid phone number format.');
                        break;
                    case 'postalCode':
                        if (!postalCodeRegex.test(value)) showError(field, 'Invalid postal code format.');
                        break;
                }
            }
        });

        if (!valid) {
            $('#errorMessages').html(errorMessages.join('<br>'));
            return false;
        }

        alert('Form submitted successfully!');
    });
});
