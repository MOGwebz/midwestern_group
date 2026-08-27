/* wkhtmltopdf header/footer helper: show .bottom-page only on the last page. */
if (typeof vars !== 'undefined') {
    var operations = {
        'bottom-page': function (elt) {
            elt.style.visibility = (vars.page === vars.topage) ? 'visible' : 'hidden';
        },
    };
    for (var klass in operations) {
        var y = document.getElementsByClassName(klass);
        for (var j = 0; j < y.length; ++j) {
            operations[klass](y[j]);
        }
    }
}
