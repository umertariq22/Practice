$.validator.addMethod( "letterswithspace", function( value, element ) {
	return this.optional( element ) || /^[a-z ]+$/i.test( value );
}, "Letters or punctuation only please" );