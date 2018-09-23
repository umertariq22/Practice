//TODO: Validate First Name
function validateFname() {
    let FnameHasError = false;
    let fname = $('#fname').val();
    let regex = new RegExp('[0-9\$?/,<>{};\']');
    let error = '';
    if (fname.length === 0){
        error = 'First Name is required'
        FnameHasError = true
    }else if((fname.match(/^\s+$/) && !regex.test(fname)) || fname.length < 3) {
        error = 'At least three characters are required';
        FnameHasError = true
    }else if (regex.test(fname)){
        error = 'Only letters and whitespaces are allowed';
        FnameHasError = true
    }else{
        error = '';
        FnameHasError = false
    }
    if (FnameHasError){
        $('label[for="fname"]').addClass('text-danger').removeClass('text-success');
        $('#fname').addClass('text-danger border border-danger').removeClass('text-success border-success');;
        $('#FnameError').html('<span class=\"text-danger\">* ' + error + '</span>')
    }else{
        $('label[for="fname"]').removeClass('text-danger').addClass('text-success');
        $('#fname').removeClass('text-danger border border-danger').addClass('text-success border-success');;
        $('#FnameError').html('')
    }
    return FnameHasError
}
//TODO: Validate Last Name
function validateLname() {
    let LnameHasError = false;
    let lname = $('#lname').val();
    let regex = new RegExp('[0-9\$?/,<>{};\']');
    let error = '';
    if (lname.length === 0) {
        error = 'Last Name is required'
        LnameHasError = true
    } else if ((lname.match(/^\s+$/) && !regex.test(lname)) || lname.length < 3) {
        error = 'At least three characters are required';
        LnameHasError = true
    } else if (regex.test(lname)) {
        error = 'Only letters and whitespaces are allowed';
        LnameHasError = true
    } else {
        error = '';
        LnameHasError = false
    }
    if (LnameHasError){
        $('label[for="lname"]').addClass('text-danger').removeClass('text-success');
        $('#lname').addClass('text-danger border-danger').removeClass('text-success border-success');
        $('#LnameError').html('<span class=\"text-danger\">* ' + error + '</span>')
    }else{
        $('label[for="lname"]').removeClass('text-danger').addClass('text-success');
        $('#lname').removeClass('text-danger border-danger').addClass('text-success border-success');
        $('#LnameError').html('')
    }

    return LnameHasError
}
//TODO: Validate Email
function validateEmail() {
    let EmailHasError = false;
    let email = $('#email').val();
    let regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let error = '';

    if (email === ''){
        error = 'Email is required';
        EmailHasError = true;
    }else if(!regex.test(email)){
        error = 'Invalid Email Format';
        EmailHasError = true;
    }else{
        error = '';
        EmailHasError = false;
    }
    if (EmailHasError){
        $('label[for="email"]').addClass('text-danger').removeClass('text-success');
        $('#email').addClass('text-danger border-danger').removeClass('text-success border-success');
        $('#EmailError').html('<span class=\"text-danger\">* ' + error + '</span>')
    }else{
        $('label[for="email"]').removeClass('text-danger').addClass('text-success');
        $('#email').removeClass('text-danger border-danger').addClass('text-success border-success');
        $('#EmailError').html('')
    }
    return EmailHasError;
}