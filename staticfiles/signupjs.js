function validateForm(event) {
    // You can add your validation logic here
    // For a simple example, let's just check if the password is at least 6 characters long
    var password = document.getElementById('password').value;
    if (password.length < 6) {
        alert('Password must be at least 6 characters long');
        event.preventDefault(); // Prevent the form from submitting
    }
}