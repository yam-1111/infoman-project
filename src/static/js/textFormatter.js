$(document).ready(function () {
    console.log("textFormatter.js is loaded");

    function toTitleCase(str) {
        return str.replace(/\b(\w+)(\s+[IVXLCDM]+)?\b/g, function (txt) {
            let parts = txt.split(' ');
            let mainPart = parts[0].charAt(0).toUpperCase() + parts[0].substr(1).toLowerCase();
            if (parts.length > 1) {
                let romanNumeral = parts.slice(1).join(' ');
                return mainPart + ' ' + romanNumeral.toUpperCase();
            }
            return mainPart;
        });
    }

    // Apply to all input fields within #parentContainer
    $('#parentContainer').on('input', 'input', function () {
        var input = $(this);
        input.val(toTitleCase(input.val()));
    });
});
