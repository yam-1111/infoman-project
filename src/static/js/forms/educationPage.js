window.elementary = 0;
window.secondary = 0;
window.college = 0;
window.post = 0;

$(document).ready(function () {
  // Function to toggle highest attainment input fields
  function toggleHighestAttainment(id, isChecked) {
    if (isChecked) {
      $(`#highestAttainment${id}`).hide();
    } else {
      $(`#highestAttainment${id}`).show();
    }
  }

  // elementary
  $("#addElementaryBtn").click(function () {
    elementary++;
    let elementaryForm = `
      <div class="shadow-sm elementary-form row gap-3 align-items-center m-2 m-2" id="elementaryForm${elementary}">
        <div class="col-4">
          <div class="form-group">
            <label for="elementaryName${elementary}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="elementarySchoolName${elementary}" name="elementarySchoolName${elementary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="elementaryDegreeName${elementary}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="elementaryDegreeName${elementary}" name="elementaryDegreeName${elementary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="elementaryStart${elementary}">Start date</label>
            <input type="date" class="form-control" id="elementaryStart${elementary}" name="elementaryStart${elementary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="elementaryEnd${elementary}">End date</label>
            <input type="date" class="form-control" id="elementaryEnd${elementary}" name="elementaryEnd${elementary}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="elemGraduate${elementary}" data-id="${elementary}">
              <label class="form-check-label" for="elemGraduate${elementary}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${elementary}">
          <label for="highestAttainmentInput${elementary}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <div class="col-sm-5">
            <input type="text" class="form-control" id="highestAttainmentInput${elementary}" placeholder="Highest Attainment">
          </div>
        </div>

        <div class="col-md-8">
             <label for="elementaryAchievementInput${elementary}" >Achievements / Awards / Honor Received</label>
            <input type="text" class="form-control" id="elementaryAchievementInput${elementary}">
        </div>
        <div class="col-3">
          <button type="button" class="btn btn-danger removeElementaryButton" data-id="${elementary}">Remove</button>
        </div>
      </div>
    `;
    $("#elementaryContainer").append(elementaryForm);

    // Attach event listener for the graduate checkbox
    $(document).on("change", `#elemGraduate${elementary}`, function () {
      let id = $(this).data("id");
      let isChecked = $(this).is(":checked");
      toggleHighestAttainment(id, isChecked);
    });

    // Initial state
    toggleHighestAttainment(elementary, false);

    // Remove button functionality
    $(document).on("click", ".removeElementaryButton", function () {
      let id = $(this).data("id");
      $("#elementaryForm" + id).remove();
    });
  });

  $("#removeElementaryBtn").click(function () {
    $("#elementaryContainer").empty();
    elementary = 0;
  });

  // secondary
  $("#addSecondaryBtn").click(function () {
    secondary++;
    let secondaryForm = `
      <div class="secondary-form row gap-3 align-items-center m-2" id="secondaryForm${secondary}">
        <div class="col-4">
          <div class="form-group">
            <label for="secondaryName${secondary}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="secondarySchoolName${secondary}" name="secondarySchoolName${secondary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="secondaryDegreeName${secondary}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="secondaryDegreeName${secondary}" name="secondaryDegreeName${secondary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="secondaryStart${secondary}">Start date</label>
            <input type="date" class="form-control" id="secondaryStart${secondary}" name="secondaryStart${secondary}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="secondaryEnd${secondary}">End date</label>
            <input type="date" class="form-control" id="secondaryEnd${secondary}" name="secondaryEnd${secondary}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="secGraduate${secondary}" data-id="${secondary}">
              <label class="form-check-label" for="secGraduate${secondary}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${secondary}">
          <label for="highestAttainmentInput${secondary}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <div class="col-sm-5">
            <input type="text" class="form-control" id="highestAttainmentInput${secondary}" placeholder="Highest Attainment">
          </div>
        </div>

        <div class="col-md-8">
             <label for="secondaryAchievementInput${secondary}" >Achievements / Awards / Honor Received</label>
            <input type="text" class="form-control" id="secondaryAchievementInput${secondary}">
        </div>

        <div class="col-3">
          <button type="button" class="btn btn-danger removeSecondaryButton" data-id="${secondary}">Remove</button>
        </div>
      </div>
    `;
    $("#secondaryContainer").append(secondaryForm);

    // Attach event listener for the graduate checkbox
    $(document).on("change", `#secGraduate${secondary}`, function () {
      let id = $(this).data("id");
      let isChecked = $(this).is(":checked");
      toggleHighestAttainment(id, isChecked);
    });

    // Initial state
    toggleHighestAttainment(secondary, false);

    // Remove button functionality
    $(document).on("click", ".removeSecondaryButton", function () {
      let id = $(this).data("id");
      $("#secondaryForm" + id).remove();
    });
  });

  $("#removeSecondaryBtn").click(function () {
    $("#secondaryContainer").empty();
    secondary = 0;
  });

  // tertiary
  $("#addTertiaryBtn").click(function () {
    college++;
    let tertiaryForm = `
      <div class="tertiary-form row gap-3 align-items-center m-2" id="tertiaryForm${college}">
        <div class="col-4">
          <div class="form-group">
            <label for="tertiaryName${college}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="tertiarySchoolName${college}" name="tertiarySchoolName${college}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="tertiaryDegreeName${college}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="tertiaryDegreeName${college}" name="tertiaryDegreeName${college}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="tertiaryStart${college}">Start date</label>
            <input type="date" class="form-control" id="tertiaryStart${college}" name="tertiaryStart${college}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="tertiaryEnd${college}">End date</label>
            <input type="date" class="form-control" id="tertiaryEnd${college}" name="tertiaryEnd${college}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="terGraduate${college}" data-id="${college}">
              <label class="form-check-label" for="terGraduate${college}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${college}">
          <label for="highestAttainmentInput${college}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <div class="col-sm-5">
            <input type="text" class="form-control" id="highestAttainmentInput${college}" placeholder="Highest Attainment">
          </div>
        </div>
        <div class="col-md-8">
             <label for="tertiaryAchievementInput${college}" >Achievements / Awards / Honor Received</label>
            <input type="text" class="form-control" id="tertiaryAchievementInput${college}">
        </div>
        <div class="col-3">
          <button type="button" class="btn btn-danger removeTertiaryButton" data-id="${college}">Remove</button>
        </div>
      </div>
    `;
    $("#tertiaryContainer").append(tertiaryForm);

    // Attach event listener for the graduate checkbox
    $(document).on("change", `#terGraduate${college}`, function () {
      let id = $(this).data("id");
      let isChecked = $(this).is(":checked");
      toggleHighestAttainment(id, isChecked);
    });

    // Initial state
    toggleHighestAttainment(college, false);

    // Remove button functionality
    $(document).on("click", ".removeTertiaryButton", function () {
      let id = $(this).data("id");
      $("#tertiaryForm" + id).remove();
    });
  });

  $("#removeTertiaryBtn").click(function () {
    $("#tertiaryContainer").empty();
    college = 0;
  });

  // post
  $("#addPostBtn").click(function () {
    post++;
    let postForm = `
      <div class="post-form row gap-3 align-items-center m-2" id="postForm${post}">
        <div class="col-4">
          <div class="form-group">
            <label for="postName${post}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="postSchoolName${post}" name="postSchoolName${post}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="postDegreeName${post}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="postDegreeName${post}" name="postDegreeName${post}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="postStart${post}">Start date</label>
            <input type="date" class="form-control" id="postStart${post}" name="postStart${post}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="postEnd${post}">End date</label>
            <input type="date" class="form-control" id="postEnd${post}" name="postEnd${post}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="postGraduate${post}" data-id="${post}">
              <label class="form-check-label" for="postGraduate${post}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${post}">
        <div class="col-sm-5">
          <label for="highestAttainmentInput${post}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <input type="text" class="form-control" id="highestAttainmentInput${post}" placeholder="Highest Attainment">
        </div>
        </div>

        <div class="col-8">
             <label for="postAchievementInput${post}">Achievements / Awards / Honor Received</label>
            <input type="text" class="form-control" id="postAchievementInput${post}" name="postAchievementInput${post}">
        </div>
        <div class="col-2">
          <button type="button" class="btn btn-danger removePostButton" data-id="${post}">Remove</button>
        </div>
      </div>
    `;
    $("#postContainer").append(postForm);

    // Attach event listener for the graduate checkbox
    $(document).on("change", `#postGraduate${post}`, function () {
      let id = $(this).data("id");
      let isChecked = $(this).is(":checked");
      toggleHighestAttainment(id, isChecked);
    });

    // Initial state
    toggleHighestAttainment(post, false);

    // Remove button functionality
    $(document).on("click", ".removePostButton", function () {
      let id = $(this).data("id");
      $("#postForm" + id).remove();
    });
  });

  $("#removePostBtn").click(function () {
    $("#postContainer").empty();
    post = 0;
  });
});
