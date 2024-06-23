
$(document).ready(function () {
  function addChildForm(child = {}) {

    console.log("child length: " + Object.keys(child).length + "\n" + JSON.stringify(child));

    childCounter = $('.child-form').length + 1;
    window._childCounter = childCounter;

    console.log("childCounter: " + childCounter);
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
  });

  /**TODO : fix the bug - when removing the 1st item it deletes all */
   $(document).on("click", ".removeChildButton", function () {
    console.log("removing child..." + $(this).data("id"));
    let id = $(this).data("id");
    $(`.child-form[id="childForm${id}"]`).remove();
    childData.splice(id - 1, 1);
    
  });



  $("#removeChildrenBtn").click(function () {
    $("#childrenContainer").empty();
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

