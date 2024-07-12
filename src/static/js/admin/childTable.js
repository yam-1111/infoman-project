$(document).ready(function(){
    console.log('childTable loaded');
    
    /**
     * Edit functionality for the childTable
     */
    $('.editBtn').click(function(){
        window.Children_ID = $(this).attr('data-id');
        var cscID = $('#td-cscID'+Children_ID).text();
        var fullName = $('#td-fullName'+Children_ID).text();
        var birthDay = $('#td-birthDay'+Children_ID).text();

        // Fetch the data
        $.ajax({
            url: '/admin/table/children', 
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
               parentID: cscID
            }),
            success: function(response){
                var childDetails = response.persons;
                var cscId = response.cscIds;

                // Populate modal fields
                $('#fullName').val(fullName);
                $('#birthDay').val(birthDay);

                // Populate dropdown select
                var selectDropdown = $('#cscId'); // Assuming the id of your dropdown select is cscId
                selectDropdown.empty(); // Clear previous options

                // Loop through childDetails to populate options
                childDetails.forEach(function(child) {
                    selectDropdown.append('<option value="' + child.cscIdNo + '">' + child.fullName + '</option>');
                });

                // Select the option based on the current parentID
                selectDropdown.val(cscID);
            },
            error: function(xhr, status, error){
                alert('Unable to fetch the information for child id: ' + Children_ID);
            }
        });

        // Update button handler for saving changes
        $('#saveChangesBtn').click(function(){
            var updatedFullName = $('#fullName').val();
            var updatedBirthDay = $('#birthDay').val();
            var updatedCscId = $('#cscId').val(); // Assuming this is the ID of the selected option

            // Perform PATCH request to update the child data
            $.ajax({
                url: '/admin/table/children',
                type: 'PATCH',
                contentType: 'application/json',
                data: JSON.stringify({
                    Children_ID: Children_ID,
                    fullName: updatedFullName,
                    birthDay: updatedBirthDay,
                    CSC_ID_No: updatedCscId
                }),
                success: function(response){
                    // Optionally handle success response, e.g., close modal or update UI
                    alert('Data updated successfully:', response);
                    location.reload();
                },
                error: function(xhr, status, error){
                    console.log('Unable to update child information.');
                    console.error('Error:', error);
                }
            });
        });
    });

    /**
     * Add functionality for the childTable
     */
    $('#addSaveChangesBtn').click(function(){
        var cscID = $('#addcscId option:selected').val();
        var fullName = $('#addfullName').val();
        var birthDay = $('#addbirthDay').val();

        if (fullName === '') {
            alert('Full name cannot be empty.');
            return;
        }

        // Perform POST request to add a new child
        $.ajax({
            url: '/admin/add/children',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                CSC_ID_No: cscID,
                fullName: fullName,
                birthDay: birthDay
            }),
            success: function(response){
                // Optionally handle success response, e.g., close modal or update UI
                // alert('Child added successfully:', response);
                location.reload();
            },
            error: function(xhr, status, error){
                console.log('Unable to add child information.');
                alert('Error:', error);
            }
        });
    });
});
