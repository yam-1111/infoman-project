console.log("form loaded")
window.counter = 0;
const pages = ["personal_info", "children", "education"];
var formData = {}

$(document).ready(function () {
    // Function to load content
    window.loadPage = (page) => {

        $("input, select, textarea").each(function () {
            if ($(this).is(":radio")) {
                if ($(this).is(":checked")) {
                    formData[$(this).attr('name')] = $(this).val();
                }
            } else {
                formData[$(this).attr('name')] = $(this).val();
            }
        });

        $("#parentContainer").fadeOut(100, function () {
            $(this).load("/static/html/form/" + page + ".html", function () {
                $(this).fadeIn(150);
                // Repopulate the form data
                for (let name in formData) {
                    let element = $(`[name="${name}"]`);
                    if (element.is(":radio")) {
                        element.filter(`[value="${formData[name]}"]`).prop("checked", true);
                    } else {
                        element.val(formData[name]);
                    }
                }
                // Update navigation buttons visibility
                if (counter == 0) {
                    $("#prevButton").hide();
                } else {
                    $("#prevButton").show();
                }

                if (counter == 2) {
                    $("#nextButton").hide();
                    $("#buttonContainer").append('<button type="submit" class="btn btn-success" id="submitForm">Submit Form</button>');
                } else {
                    $("#nextButton").show();
                    // Ensure the submit button is removed if it exists and the counter is not 2
                    $("#submitForm").remove();
                }

            });
        });
    }

    loadPage("personal_info");

    // Handle navigation clicks
    window.nextPage = () => {
        counter++;
        if (counter >= pages.length) {
            counter = 0;
        }
        loadPage(pages[counter]);
    }

    window.prevPage = function () {
        if (counter > 0) {
            counter--;
        } else {
            counter = pages.length - 1;
        }
        loadPage(pages[counter]);
    }
});
