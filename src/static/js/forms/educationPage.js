window.levels = ["elementary", "secondary", "tertiary", "post"];
window.counts = {
  elementary: 0,
  secondary: 0,
  tertiary: 0,
  post: 0,
};

$(document).ready(function () {
  function toggleHighestAttainment(id, isChecked, level) {
    if (isChecked) {
      $(`#highestAttainment${level}${id}`).hide();
    } else {
      $(`#highestAttainment${level}${id}`).show();
    }
  }

  function createForm(level, count, data = {}) {
    let schoolName = data.schoolName || "";
    let degree = data.degree || "";
    let gradsStart = data.gradsStart || "";
    let gradsEnd = data.gradsEnd || "";
    let isGraduate = data.isGraduate || false;
    let highestAttainment = data.highestAttainment || "";
    let AchievementInput = data.AchievementInput || "";

    return `
      <div class="${level}-form row gap-3 align-items-center m-2" id="${level}Form${count}">
        <div class="col-4">
          <div class="form-group">
            <label for="${level}Name${count}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="${level}SchoolName${count}" name="${level}SchoolName${count}" value="${schoolName}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}DegreeName${count}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="${level}DegreeName${count}" name="${level}DegreeName${count}" value="${degree}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}Start${count}">Start date</label>
            <input type="date" class="form-control" id="${level}Start${count}" name="${level}Start${count}" value="${gradsStart}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}End${count}">End date</label>
            <input type="date" class="form-control" id="${level}End${count}" name="${level}End${count}" value="${gradsEnd}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="${level}Graduate${count}" data-id="${count}" data-level="${level}" ${isGraduate ? 'checked' : ''}>
              <label class="form-check-label" for="${level}Graduate${count}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${level}${count}">
          <label for="highestAttainmentInput${level}${count}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <div class="col-sm-5">
            <input type="text" class="form-control" id="highestAttainmentInput${level}${count}" placeholder="Highest Attainment" value="${highestAttainment}">
          </div>
        </div>
        <div class="col-md-8">
          <label for="${level}AchievementInput${count}">Achievements / Awards / Honor Received</label>
          <input type="text" class="form-control" id="${level}AchievementInput${count}" value="${AchievementInput}">
        </div>
        <div class="col-3">
          <button type="button" class="btn btn-danger removeButton" data-id="${count}" data-level="${level}">Remove</button>
        </div>
      </div>
    `;
  }

  levels.forEach(level => {
    $(`#add${capitalize(level)}Btn`).click(function () {
      counts[level]++;
      let form = createForm(level, counts[level]);
      $(`#${level}Container`).append(form);

      $(document).on("change", `#${level}Graduate${counts[level]}`, function () {
        let id = $(this).data("id");
        let isChecked = $(this).is(":checked");
        toggleHighestAttainment(id, isChecked, level);
      });

      toggleHighestAttainment(counts[level], false, level);

     /**TODO : fix the bug - when removing the 1st item it deletes all */
      $(document).on("click", ".removeButton", function () {
        let id = $(this).data("id");
        let level = $(this).data("level");
        $(`#${level}Form${id}`).remove();
      });
    });

    $(`#remove${capitalize(level)}Btn`).click(function () {
      $(`#${level}Container`).empty();
      counts[level] = 0;
    });
  });

  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  function populateEducationForms() {
    console.log('Populating education forms');
    window.levels.forEach(level => {
      if (educationData[level]) {
        educationData[level].forEach(education => {
          counts[level]++;
          let form = createForm(level, counts[level], education);
          $(`#${level}Container`).append(form);

          $(document).on("change", `#${level}Graduate${counts[level]}`, function () {
            let id = $(this).data("id");
            let isChecked = $(this).is(":checked");
            toggleHighestAttainment(id, isChecked, level);
          });

          toggleHighestAttainment(counts[level], education.isGraduate, level);

          $(document).on("click", ".removeButton", function () {
            let id = $(this).data("id");
            let level = $(this).data("level");
            $(`#${level}Form${id}`).remove();
            educationData[level].splice(id - 1, 1);
          });
        });
      }
    });
  }

  // Call populateEducationForms on page load
  populateEducationForms();
});
