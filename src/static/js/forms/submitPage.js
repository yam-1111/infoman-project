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
        console.log("combinedData: ", combinedData);
    });
});
