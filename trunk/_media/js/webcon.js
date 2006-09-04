
function $(id) {
	return document.getElementById(id);
}

function confirmDelete(what) {
	return confirm('Czy na pewno chcesz usunac '+what+'?');
}
