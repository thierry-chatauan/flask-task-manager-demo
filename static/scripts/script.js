document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const textField = document.querySelector('input[type="text"]');

    form.addEventListener('submit', function(event) {
        if (textField.value.trim() === '') {
            event.preventDefault();
            alert('Text field cannot be empty!');
        }
    });
});
