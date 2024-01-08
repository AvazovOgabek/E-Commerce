const form = document.getElementById('signinForm');
const loader = document.querySelector('.spinner'); 
const overlay = document.getElementById('overlay');
const error_message = document.getElementById('error_message');


form.addEventListener('submit', function(event) {
    event.preventDefault(); 

    overlay.style.display = 'block';
    loader.style.display = 'block';

    setTimeout(function() {
        form.submit();
    }, 2000);
});


function hideErrorMessage(closeButton) {
const errorContainer = closeButton.closest('.error');
if (errorContainer) {
    errorContainer.style.display = 'none';
}
}

const closeButtons = document.querySelectorAll('.error__close');
closeButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        hideErrorMessage(this);
    });
});
