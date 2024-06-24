console.log("form loaded");

// global counters
window.counter = 0;
window._childCounter = 0;
window._elementary = 0;
window._secondary = 0;
window.college = 0;
window.post = 0;

// global data
var formData = {};
window.childData = [];
var educationData = {};

const pages = ["personal_info", "children", "education"];

$(document).ready(function () {
  // Function to load content
  window.loadPage = (page) => {
    // getter on personal_info
    $("input, select, textarea")
      .not(
        "#childrencontainer input, #childrencontainer select, #childrencontainer textarea, #elementary input, #elementary select, #elementary textarea, #secondary input, #secondary select, #secondary textarea, #college input, #college select, #college textarea, #post input, #post select, #post textarea"
      )
      .each(function () {
        if ($(this).is(":radio")) {
          if ($(this).is(":checked")) {
            formData[$(this).attr("name")] = $(this).val();
          }
        } else {
          formData[$(this).attr("name")] = $(this).val();
        }
      });

    // getter on children
    let childCounter = $(".child-form").length;

    for (let j = 1; j <= childCounter; j++) {
      let fullName = $(`#childfullName${j}`).val();
      let birthDay = $(`#childbirthDay${j}`).val();
      if (fullName && birthDay) {
        if (!childData.find((_child) => _child.fullName == fullName)) {
          childData.push({ fullName: fullName, birthDay: birthDay});
        }
      }
    }

    // getter on education
    function educationDataChecker(jsonObject, nestedJson, key) {
      if (nestedJson[key]) {
        return nestedJson[key].some(
          (item) => JSON.stringify(item) === JSON.stringify(jsonObject)
        );
      }
      return false;
    }

    console.log("reading education background");
    let _educationCounter = [];
    let _educationDegree = ["elementary", "secondary", "vocational", "tertiary", "post"];
    for (let i = 0; i < _educationDegree.length; i++) {
      let educationCounter = $(`.${_educationDegree[i]}-form`).length;
      _educationCounter.push(educationCounter);
      // extract the data from inputs
      for (let x = 1; x <= _educationCounter[i]; x++) {
        console.log(
          "Educational Count :" +
            _educationCounter[i] +
            "current degree : " +
            _educationDegree[i]
        );
        // read the form rows
        let schoolName = $(`#${_educationDegree[i]}SchoolName${x}`).val();
        let degree = $(`#${_educationDegree[i]}DegreeName${x}`).val();
        let gradsStart = $(`#${_educationDegree[i]}Start${x}`).val();
        let gradsEnd = $(`#${_educationDegree[i]}End${x}`).val();
        let isGraduate = $(`#${_educationDegree[i]}Graduate${x}`).is(
          ":checked"
        );
        let highestAttainment = isGraduate
          ? ""
          : $(`#highestAttainmentInput${_educationDegree[i]}${x}`).val();
        let AchievementInput = $(
          `#${_educationDegree[i]}AchievementInput${x}`
        ).val();
        let educationInfo = {
          schoolName: schoolName,
          degree: degree,
          gradsStart: gradsStart,
          gradsEnd: gradsEnd,
          isGraduate: isGraduate,
          highestAttainment: highestAttainment,
          AchievementInput: AchievementInput,
        };
        console.log("edu data: " + JSON.stringify(educationInfo));
        // check if the form is not empty
        if (schoolName && degree && gradsStart && gradsEnd) {
          // Check if the degree already exists in the educationData dictionary
          if (!educationData[_educationDegree[i]]) {
            educationData[_educationDegree[i]] = [];
          }

          // Push the educationInfo object into the array for the appropriate degree
          if (
            !educationDataChecker(
              educationInfo,
              educationData,
              _educationDegree[i]
            )
          ) {
            console.log("pushed the edu data" + educationInfo);
            educationData[_educationDegree[i]].push(educationInfo);

            // Log the updated educationData dictionary to the console
            console.log(educationData);
          }
        }
      }
    }

    $("#parentContainer").fadeOut(100, function () {
      $(this).load("/static/html/form/" + page + ".html", function () {
        $(this).fadeIn(150);
        // Repopulate the form data

        for (let name in formData) {
          let element = $(`[name="${name}"]`);
          if (element.is(":radio")) {
            element.filter(`[value="${formData[name]}"]`).prop("checked", true);
          } else {
            element.val(formData[name]);
          }
        }

        // Update navigation buttons visibility
        if (counter == 0) {
          $("#prevButton").hide();
          _childCounter = 0;
        } else {
          $("#prevButton").show();
        }

        if (counter == 2) {
          $("#nextButton").hide();
          $("#buttonContainer").append(
            '<button type="submit" class="btn btn-success" id="submitForm">Submit Form</button>'
          );
        } else {
          $("#nextButton").show();
          // Ensure the submit button is removed if it exists and the counter is not 2
          $("#submitForm").remove();
          _childCounter = 0;
        }
      });
    });
  };

  loadPage("personal_info");

  // Handle navigation clicks
  window.nextPage = () => {
    counter++;
    if (counter >= pages.length) {
      counter = 0;
    }
    loadPage(pages[counter]);
  };

  window.prevPage = function () {
    if (counter > 0) {
      counter--;
    } else {
      counter = pages.length - 1;
    }
    loadPage(pages[counter]);
  };
});

// submitting the form
$("#submitForm").click(function () {
  var combinedData = {
    formData: formData,
    childData: childData,
    educationData: educationData,
  };

  $.ajax({
    url: "your-endpoint-url",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(combinedData),
    success: function (response) {
      // Handle success
      console.log("Ajax request successful");
      console.log(response);
    },
    error: function (xhr, status, error) {
      // Handle error
      console.error("Ajax request error:", status, error);
    },
  });
});
