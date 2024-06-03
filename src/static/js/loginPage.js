console.log("i am executed")
$(document).ready(function() {
    // Function to load content
    window.loadPage = function (page) {
        $("#parentContainer").fadeIn(150, function() {
            $(this).load("/static/html/login/" + page + ".html", function() {
                // $(this).fadeIn(150);
            });
        });
    }
    // window.loadPage = function (page) {
    //     $("#parentContainer").load("/static/html/login/" + page + ".html");
    // }

    // Initial load
    loadPage("login");

    // Handle navigation clicks
    $(".nav-link").click(function(event) {
        event.preventDefault();
        var page = $(this).data("page");
        loadPage(page);
    });
});
