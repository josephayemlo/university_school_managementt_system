  
  
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // Handle AJAX link clicks
  $(document).on("click", ".ajax_link", function(e) {
    e.preventDefault();

   
    const url = $(this).attr("href");
    $("#ajaxContainer").html("<p>Loading...</p>");

    $.ajax({
      url: url,
      type: "GET",
      success: function(response) {
        $("#ajaxContainer").html(response);
      },
      error: function(xhr) {
        $("#ajaxContainer").html("<p style='color:red;'>Error loading page.</p>");
      }
    });
  });

  // ✅ Handle AJAX form submission
  $(document).on("submit", "form.ajax_form", function(e) {

    e.preventDefault();

    const form = $(this);
    const url = form.attr("action");
    const formData = form.serialize();

    $.ajax({
      url: url,
      type: "POST",
      data: formData,
      headers: {
        "X-CSRFToken": getCookie("csrftoken")
      },
      success: function(response) {
        $("#ajaxContainer").html(response);
      },
      error: function(xhr) {
        $("#ajaxContainer").html("<p style='color:red;'>Submission failed.</p>");
      }
    });
  });
