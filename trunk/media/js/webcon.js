
function $(id) {
	return document.getElementById(id);
}

function confirmDelete(what) {
	return confirm('Czy na pewno chcesz usunac '+what+'?');
}

function confirmBlock(what) {
	return confirm('Czy na pewno chcesz zablokowac konto '+what+'?');
}

function confirmActivate(what) {
	return confirm('Czy na pewno chcesz aktywowac konto '+what+'?');
}

function genPass() {
	newpass = 'hRbcK';
	$('id_pass1').value = newpass;
	$('id_pass2').value = newpass;
	$('id_gen_pass').innerHTML = 'wygenerowane haslo: '+newpass;
}
