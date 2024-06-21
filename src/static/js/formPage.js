console.log("form loaded");

// global counters
window.counter = 0;
window.childCounter = 0;
window.elementary = 0;
window.secondary = 0;
window.college = 0;
window.post = 0;

// global data
var formData = {};
var childData = [];

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
    console.log('i am exexucted')
    function isChildrenExist(fullName){
        for (let j = 0; j < childData.length; j++) {
            console.log(childData[j].fullName + "-" + fullName )
            if (childData[j].fullName === fullName ) {
                return false;
            }
        }
        
        return true
    }
    function updateChildData() {
        // Check if childCounter is 0
        if (childCounter === 0) {
          return;
        }
      
        // Loop through each child form to get data
        for (let i = 1; i <= childCounter; i++) {
          let fullName = $(`#childfullName${i}`).val();
          let birthDay = $(`#childbirthDay${i}`).val();
      
          if (fullName && birthDay) {  // Only add non-blank entries and unique
                if(isChildrenExist(fullName)){
                    childData[i - 1] = {
                        fullName: fullName,
                        birthDay: birthDay
                    };
                }

          } 
        //   else {
        //     // If blank, remove this element and adjust the array
        //     childData.splice(i - 1, 1);
        //     // Adjust the counter to reflect the removed element
        //     childCounter--;
        //     // Re-evaluate the loop from the current position
        //     i--;
        //   }
        }
      
        console.log(childData);
      }
      updateChildData();

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
