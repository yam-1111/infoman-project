/**TODO : do the submission to the api */

$(document).ready(function() {

    // submit the form 
    $(document).on('click', '#submitForm', function () {
        console.log("submitting form clicked");
        var combinedData = {
          formData: formData,
          childData: childData,
          educationData: educationData,
        };
        console.log(combinedData);
        $.ajax({
            url: '/user/submit',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(combinedData),
            success: function (data) {
                console.log("success: ", data);
            },
            error: function (err) {
                console.log("error: ", err);
            }
        
        })
    });
});



