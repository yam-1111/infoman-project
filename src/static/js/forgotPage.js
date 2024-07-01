$(document).ready(function () {
  $("#forgotBtn").click(function (event) {
    event.preventDefault();
    $(".password").removeClass("is-invalid");

    let formData = {
      email_address: $("#forgotEmail").val(),
      dataOfBirth: $("#dateOfBirth").val(),
      password: $("#forgotPassword").val().trim(),
      password2: $("#forgotPassword2").val().trim(),
    };

    let isPasswordEqual = formData.password === formData.password2;
    if (!formData.email_address || !formData.password) {
      $("#forgotAlertError").show().text("Please fill out all fields");
      return;
    } else {
      if (isPasswordEqual) {
        $.ajax({
          url: "/retrieve",
          type: "PUT",
          contentType: "application/json",
          data: JSON.stringify(formData),
          success: function (data) {
            console.log("success: ", data.status);
            $("#forgotAlertError")
              .show()
              .removeClass("alert-danger")
              .addClass("alert-success")
              .text("Password reset successfully. Redirecting to login page.");
              setTimeout(() => {
                window.location.href = "/login";
              }, 5000);
          },
          error: function (xhr, err) {
            let errorMessage = xhr.responseJSON
              ? xhr.responseJSON.error
              : "An error occurred";
            $("#forgotAlertError").show().text(`Error: ${errorMessage}`);
          },
        });
      } else {
        $(".password").addClass("is-invalid");
        $("#forgotAlertError").show().text(`Error: Passwords do not match.`);
      }
    }
  });
});
