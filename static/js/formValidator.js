// TODO: Validate First Name
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
// TODO: Validate Last Name
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
// TODO: Validate Email
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
function password() {
            var pass = $('#pass').val();
            var length = pass.length;
            var strength = 0;
            var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
            PasswordHasError = false;
            if (length < 8){
                error = 'At least 8 characters are required';
                PasswordHasError = true;
                $('#eightChar').css('color','black')
            }else if(length >= 8 && length <= 15){
                PasswordHasError = false;
                strength += 4 * length;
                error = '';
                $('#eightChar').css('color','#28a745')
            }else if(length >15){
                strength += 60;
                PasswordHasError = false;
            }
            if (/[A-Z]/.test(pass)){
                strength += 10;
                PasswordHasError = false;
                $('#upperChar').css('color','#28a745')
            }else{
                $('#upperChar').css('color','black')
            }
            if (/[0-9]/.test(pass)){
                strength += 10;
                PasswordHasError = false;
                $('#numChar').css('color','#28a745')
            }else{
                $('#numChar').css('color','black')
            }
            if(format.test(pass)){
                strength += 10;
                PasswordHasError = false;
                $('#specialChar').css('color','#28a745')
            }else{
                $('#specialChar').css('color','black')
            }
            if(PasswordHasError){
                $('#pass').addClass('bad');
                $('#result').html('<p> * '+error+'</p>');
                $('#result').css('color','#dc3545')
                $('label[for="pass"]').css('color','#dc3545')
            }else{
                if (strength >=50 && strength <60){
                    $('#pass').addClass('bad').removeClass('good better strong');
                    $('#result').html('Bad Password').css('color','#dc3545');
                    $('label[for="pass"]').css('color','#dc3545')
                }
                else if(strength >=60 && strength < 70){
                    $('#pass').addClass('better').removeClass('good bad strong');
                    $('#result').html('Better Password').css('color','#ffc107');
                    $('label[for="pass"]').css('color','#ffc107')
                }
                else if(strength >=70 && strength <80){
                    $('#pass').addClass('good').removeClass('bad better strong');
                    $('#result').html('Good Password').css('color','#32CD32');
                    $('label[for="pass"]').css('color','#32CD32')
                }
                else if(strength >= 80){
                    $('#pass').addClass('strong').removeClass('good better bad');
                    $('#result').html('Strong Password').css('color','#28a745')
                    $('label[for="pass"]').css('color','#28a745')
                }

            }
            return PasswordHasError;
        }
function ConfirmPassword() {
    var pass = $('#pass').val();
    var cpass = $('#cpass').val();
    var CPassHasError = false;

    if (pass === cpass && cpass !== ''){
        CPassHasError = false;
        $('#cpass').addClass('strong');
        $('label[for="cpass"]').css('color','#28a745');
        $('#cpassError').html('* Password Matched').css('color','#28a745');
    }else if(cpass === '' ){
        CPassHasError = true;
        $('#cpass').addClass('bad');
        $('label[for="cpass"]').css('color','#dc3545');
        $('#cpassError').html('* At least 8 characters required').css('color','#dc3545');
    }else{
        CPassHasError = true;
        $('#cpass').addClass('bad');
        $('label[for="cpass"]').css('color','#dc3545');
        $('#cpassError').html('* Password not matched').css('color','#dc3545');
    }
    return CPassHasError
}
function GenderCheck() {
    GenderHasError = false;
    if($('input:radio[name="gender"]:checked').length === 0){
        GenderHasError = true;
        error = 'Please select your gender'
    }
    if (GenderHasError){
        $('#GenderError').css('color','#dc3545').html('<p> * '+error+'</p>');
    }else{
        $('#GenderError').html('');
    }
    return GenderHasError;

}
function ValidateDate(val) {
    DateHasError = false;
    if (val === '0') {
        DateHasError = true;
        error = 'This field is required'
    } else {
        error = '';
        DateHasError = false;
    }
    if (DateHasError){
        $('#dateError').html('<p> *'+error+'</p>').css('color','red')
    }else{
        $('#dateError').html('')
    }
    return DateHasError;
}

function ValidateMonth(val) {
    MonthHasError = false;
    if (val === '0') {
        MonthHasError = true;
        error = 'This field is required'
    } else {
        error = '';
        MonthHasError = false;
    }
    if (MonthHasError){
        $('#monthError').html('<p> *'+error+'</p>').css('color','red')
    }else{
        $('#monthError').html('')
    }
    return MonthHasError;
}
function ValidateYear(val) {
    YearHasError = false;
    if (val === '0') {
        YearHasError = true;
        error = 'This field is required'
    } else {
        error = '';
        YearHasError = false;
    }
    if (YearHasError){
        $('#yearError').html('<p> *'+error+'</p>').css('color','red')
    }else{
        $('#yearError').html('')
    }
    return YearHasError;
}