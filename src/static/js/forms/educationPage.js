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

  function createForm(level, count) {
    return `
      <div class="${level}-form row gap-3 align-items-center m-2" id="${level}Form${count}">
        <div class="col-4">
          <div class="form-group">
            <label for="${level}Name${count}">School Name</label>
            <input type="text" class="form-control" placeholder="School Name" id="${level}SchoolName${count}" name="${level}SchoolName${count}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}DegreeName${count}">Basic Education / Degree / Course <span class="text-muted"> (Write in full) </span> </label>
            <input type="text" class="form-control" placeholder="Basic Education / Degree / Course" id="${level}DegreeName${count}" name="${level}DegreeName${count}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}Start${count}">Start date</label>
            <input type="date" class="form-control" id="${level}Start${count}" name="${level}Start${count}" required>
          </div>
        </div>
        <div class="col-4">
          <div class="form-group">
            <label for="${level}End${count}">End date</label>
            <input type="date" class="form-control" id="${level}End${count}" name="${level}End${count}" required>
          </div>
        </div>
        <div class="form-group row">
          <div class="col-sm-5">
            <div class="form-check">
              <input class="form-check-input graduate-checkbox" type="checkbox" id="${level}Graduate${count}" data-id="${count}" data-level="${level}">
              <label class="form-check-label" for="${level}Graduate${count}">Graduated</label>
            </div>
          </div>
        </div>
        <div class="form-group row" id="highestAttainment${level}${count}">
          <label for="highestAttainmentInput${level}${count}" class="col-sm-2 col-form-label">Highest Attainment</label>
          <div class="col-sm-5">
            <input type="text" class="form-control" id="highestAttainmentInput${level}${count}" placeholder="Highest Attainment">
          </div>
        </div>
        <div class="col-md-8">
          <label for="${level}AchievementInput${count}">Achievements / Awards / Honor Received</label>
          <input type="text" class="form-control" id="${level}AchievementInput${count}">
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
});
