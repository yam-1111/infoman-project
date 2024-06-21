

$(document).ready(function () {
  function addChildForm(child = {}) {
    childCounter++;
    let fullName = child.fullName || "";
    let birthDay = child.birthDay || "";

    let childForm = `
      <div class="child-form row gap-3 align-items-center p-2" id="childForm${childCounter}">
          <div class="col-4">
              <div class="form-group">
                  <label for="fullName${childCounter}">Full Name</label>
                  <input type="text" class="form-control" placeholder="Children Name" id="childfullName${childCounter}" name="childfullName${childCounter}" value="${fullName}" required>
              </div>
          </div>
          <div class="col-4">
              <div class="form-group">
                  <label for="birthDay${childCounter}">Birth Day</label>
                  <input type="date" class="form-control" id="childbirthDay${childCounter}" name="childbirthDay${childCounter}" value="${birthDay}" required>
              </div>
          </div>
          <div class="col-3">
              <button type="button" class="btn btn-danger removeChildButton" data-id="${childCounter}">Remove</button>
          </div>
      </div>
    `;
    $("#childrenContainer").append(childForm);

   
  }

  $("#addChildrenBtn").click(function () {
    addChildForm();
    childData.push({ fullName: "", birthDay: "" });
  });

  $(document).on("click", ".removeChildButton", function () {
    let id = $(this).data("id");
    childData.splice(id - 1, 1);
  });

  $("#removeChildrenBtn").click(function () {
    $("#childrenContainer").empty();
    childCounter = 0;
    childData = [];
  });

  function populateChildren() {
    childData.forEach(child => {
      if (child) {
        addChildForm(child);
      }
    });
  }

  if(counter == 1){
    console.log("adding the children...");
    populateChildren();
  }


});

