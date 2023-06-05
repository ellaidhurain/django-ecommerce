console.log('sign');
// const passwordEl = document.querySelector('#pass1');
const form = document.querySelector('#signin');


form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();
    form.submit();
    
})


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

