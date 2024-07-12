$(document).ready(function(){
    console.log('educationTable loaded');
    
    /**
     * Edit functionality for the educationTable
     */
    $('.editBtn').click(function(){
        window.Education_ID = $(this).attr('data-id');
        var cscID = $('#td-cscID'+Education_ID).text();
        var schoolName = $('#td-schoolName'+Education_ID).text();
        var graduationDate = $('#td-graduationDate'+Education_ID).text();

        // Fetch the data
        $.ajax({
            url: '/admin/table/education', 
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
               parentID: cscID
            }),
            success: function(response){
                var educationDetails = response.educations;
                var cscId = response.cscIds;

                // Populate modal fields
                $('#schoolName').val(schoolName);
                $('#graduationDate').val(graduationDate);

                // Populate dropdown select
                var selectDropdown = $('#cscId'); // Assuming the id of your dropdown select is cscId
                selectDropdown.empty(); // Clear previous options

                // Loop through educationDetails to populate options
                educationDetails.forEach(function(education) {
                    selectDropdown.append('<option value="' + education.cscIdNo + '">' + education.schoolName + '</option>');
                });

                // Select the option based on the current parentID
                selectDropdown.val(cscID);
            },
            error: function(xhr, status, error){
                alert('Unable to fetch the information for education id: ' + Education_ID);
            }
        });

        // Update button handler for saving changes
        $('#saveChangesBtn').click(function(){
            var updatedSchoolName = $('#schoolName').val();
            var updatedGraduationDate = $('#graduationDate').val();
            var updatedCscId = $('#cscId').val(); // Assuming this is the ID of the selected option

            // Perform PATCH request to update the education data
            $.ajax({
                url: '/admin/table/education',
                type: 'PATCH',
                contentType: 'application/json',
                data: JSON.stringify({
                    Education_ID: Education_ID,
                    schoolName: updatedSchoolName,
                    graduationDate: updatedGraduationDate,
                    CSC_ID_No: updatedCscId
                }),
                success: function(response){
                    // Optionally handle success response, e.g., close modal or update UI
                    alert('Data updated successfully:', response);
                    location.reload();
                },
                error: function(xhr, status, error){
                    console.log('Unable to update education information.');
                    console.error('Error:', error);
                }
            });
        });
    });

    /**
     * ADD functionality for the educationTable
     */

    $('#saveAddChangesBtn').on('click', function() {
        var cscId = $('#addcscId').val();
        var educationLevel = $('#addeducationLevel').val();
        var schoolName = $('#addschoolName').val();
        var degreeName = $('#adddegreeName').val();
        var gradStart = $('#addgradStart').val();
        var gradEnd = $('#addgradEnd').val();
        var graduate = $('#addGraduate').is(':checked');
        var highestAttainment = graduate ? '' : $('#addhighestAttainment').val();
        var achievement = $('#addAchievementInput').val();
    
        // Validate required fields
        if (!cscId || !educationLevel || !schoolName || !degreeName || !achievement) {
            alert('Please fill in all required fields.');
            return;
        }
    
        // Validate date range
        if (new Date(gradEnd) < new Date(gradStart)) {
            alert('End date cannot be earlier than start date.');
            return;
        }
    
        var formData = {
            CSC_ID_No: cscId,
            educationLevel: educationLevel,
            schoolName: schoolName,
            degree: degreeName,
            gradsStart: gradStart,
            gradsEnd: gradEnd,
            graduate: graduate,
            highestAttainment: highestAttainment,
            yearGraduated: graduate ? gradEnd : '',
            AchievementInput: achievement
        };
    
        $.ajax({
            url: '/admin/add/education',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                // Handle success
                alert('Education entry added successfully!');
                $('#addModal').modal('hide');
                // Optionally, refresh the page or update the UI
            },
            error: function(xhr, status, error) {
                // Handle error
                alert('An error occurred while adding the education entry.');
            }
        });
    });

    /**
     * EDIT functionality for the educationTable
     */

    $('.editBtn').click(function() {
        var educationId = $(this).attr('data-id');
        $.ajax({
            url: `/admin/table/education`,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ educationId: educationId }),
            success: function(response) {
                var education = response.data;
                $('#editcscId').val(education.CSC_ID_No);
                $('#editeducationLevel').val(education.educationLevel);
                $('#editschoolName').val(education.schoolName);
                $('#editdegreeName').val(education.degree);
                $('#editgradStart').val(education.gradsStart);
                $('#editgradEnd').val(education.gradsEnd);
                $('#editGraduate').prop('checked', education.graduate);
                if (education.graduate) {
                    $('#editHighestAttainmentContainer').hide();
                } else {
                    $('#editHighestAttainmentContainer').show();
                    $('#edithighestAttainment').val(education.highestAttainment);
                }
                $('#editAchievementInput').val(education.AchievementInput);
                $('#editModal').modal('show');
            },
            error: function(xhr, status, error) {
                alert('Unable to fetch education entry. Please try again.');
            }
        });
    });
    

});
