var signupData = {};

console.log("I am executed");
$(document).ready(function () {
  // Handle signups
  window.submitSignupForm = (event) => {
    event.preventDefault();
    signupData = {}; // Clear previous data
    let isValid = true; // Track form validity

    $("input, select, textarea").each(function () {
      if ($(this).is(":radio")) {
        if ($(this).is(":checked")) {
          signupData[$(this).attr("name")] = $(this).val();
        }
      } else {
        signupData[$(this).attr("name")] = $(this).val();
      }

      // Check if the field is empty
      if (!$(this).val()) {
        isValid = false;
        $("#signupAlertError").show().text("Please fill out all fields");
      }
    });

    if (isValid) {
      $("#signupAlertError").hide().text("");
      $.ajax({
        url: "/signup",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(signupData),
        success: function (data) {
          console.log("success: ", data.status);
          window.location.href = "/login";
        },
        error: function (xhr, err) {
          let errorMessage = xhr.responseJSON
            ? xhr.responseJSON.error
            : "An error occurred";
          $("#signupAlertError").show().text(`Error: ${errorMessage}`);
        },
      });
    }
  };

  // Handle logins
  $("#loginForm").submit(function (event) {
    event.preventDefault();

    // Serialize form data into JSON object
    let formData = {
      email_address: $("#loginEmail").val(),
      password: $("#loginPassword").val(),
    };

    // Send AJAX request
    $.ajax({
      url: "/login",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(formData),
      success: function (data) {
        if (data.role === "admin") {
          window.location.href = "/admin";
        } else {
            window.location.href = "/user/forms";
        }
      },

      error: function (xhr, err) {
        let errorMessage = xhr.responseJSON
          ? xhr.responseJSON.error
          : "An error occurred";
        $("#loginAlertError").show().text(`Error: ${errorMessage}`);
      },
    });
  });
});
