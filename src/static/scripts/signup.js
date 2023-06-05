console.log("hi");
const usernameEl = document.querySelector('#username');
const emailEl = document.querySelector('#email');
const passwordEl = document.querySelector('#password1');
const confirmPasswordEl = document.querySelector('#password2');

const form = document.querySelector('#signup');


const isRequired = (value) => value === '' ? false : true;

const isBetween = (length, min, max) => length < min || length > max ? false : true;

const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    // test(str) is used to match the pattern. it returns boolean value 
    return re.test(password);
};


const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;

    input.style.border = "1px solid red";

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};


const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    input.style.border = "1px solid green";
    // formField.classList.remove('error');
    // formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}


const checkUsername = () => {

    // initially set validation to false
    let valid = false;
    const min = 3,
        max = 25;
        // remove spacing from starting and ending " ellai dhurai  " => "ellai dhurai"
    const username = usernameEl ? usernameEl.value.trim():"";

    if (!isRequired(username)) {
        showError(usernameEl, 'Username cannot be blank.');
    } else if (!isBetween(username.length, min, max)) {
        showError(usernameEl, `Username must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(usernameEl);
        valid = true;
    }
    return valid;
}

const checkEmail = () => {
    let valid = false;
    const email = emailEl ? emailEl.value.trim():'';
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'Email is not valid.')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
}


const checkPassword = () => {

    let valid = false;

    const password = passwordEl ? passwordEl.value.trim():'';

    if (!isRequired(password)) {
        showError(passwordEl, 'Password cannot be blank.');
    } else if (!isPasswordSecure(password)) {
        showError(passwordEl, 'Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)');
    } else {
        showSuccess(passwordEl);
        valid = true;
    }

    return valid;
};


const checkConfirmPassword = () => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmPasswordEl ? confirmPasswordEl.value.trim():'';
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'Please enter the password again');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, 'Confirm password does not match');
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }

    return valid;
};


form.addEventListener('submit', function (e) {
    // prevent the form from submitting or executing the request
    e.preventDefault();

    // validate forms
    let isUsernameValid = checkUsername(),
        isEmailValid = checkEmail(),
        isPasswordValid = checkPassword(),
        isConfirmPasswordValid = checkConfirmPassword();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid;

    // submit to the server if the form is valid
    if (isFormValid) {
        form.submit();
    }
});


const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce((e)=> {
    switch (e.target.name) {
        case 'username':
            checkUsername();
            break;
        case 'email':
            checkEmail();
            break;
        case 'password':
            checkPassword();
            break;
        case 'confirm-password':
            checkConfirmPassword();
            break;
    }
}));


// response error function

function error_fun(){
    // get the message data from p tag 
    const err_msg = document.getElementById("err").innerHTML;
    // replace all single quote json data to doubles quotes
    var a = err_msg.replaceAll(`'`, `"`)

    // convert json data to js object
    const err_data = JSON.parse(a); 

    for (i in err_data){
        // get the id with key of error data from messages (username:'username not match')
        const res_err = document.getElementById(i);

   
        // method to get the parent element (input field) of id=username 
        const err_field = res_err.parentElement;

        res_err.style.border = "1px solid red";
        // get the id of child element of err_field  
        const error = err_field.querySelector('small');

        // show the error value
        error.textContent = err_data[i];
}
}


