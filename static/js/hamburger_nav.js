    document.addEventListener("DOMContentLoaded", function () {
      const toggleBtn = document.getElementById("hamburgerToggle");
      const closeBtn = document.getElementById("closeSideNav");
      const sideNav = document.getElementById("sideNav");
  
      toggleBtn.addEventListener("click", () => {
        sideNav.classList.add("active");
      });
  
      closeBtn.addEventListener("click", () => {
        sideNav.classList.remove("active");
      });
  
      // Optional: Close on click outside
      document.addEventListener("click", function (e) {
        if (!sideNav.contains(e.target) && !toggleBtn.contains(e.target)) {
          sideNav.classList.remove("active");
        }
      });
    });

    // when already clicked and open with link still close the harburger if screen resizes
    window.addEventListener("resize", function () {
    const screenWidth = window.innerWidth;
    if (screenWidth > 1024) {
        sideNav.classList.remove("active");
    }
    });
  