console.log("i am executed")
window.counter = 0;
const pages = ["personal_info", "children", "education"];

$(document).ready(function () {
    // Function to load content
    window.loadPage = (page) => {
        $("#parentContainer").fadeOut(100, function () {
            $(this).load("/static/html/form/" + page + ".html", function () {
                $(this).fadeIn(150);
                // Update navigation buttons visibility
                if (counter == 0) {
                    $("#prevButton").hide();
                } else {
                    $("#prevButton").show();
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
