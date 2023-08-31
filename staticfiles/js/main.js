const sideBarToolsBtn = document.querySelectorAll("a.tools-button");
  const sideBarBig = document.querySelector(".side-bar-big");
  const sideBarSmall = document.querySelector(".side-bar-small");
  sideBarToolsBtn.forEach(function (link) {
    link.addEventListener("click", function () {
      sideBarBig.classList.toggle("active");
      sideBarSmall.classList.toggle("active");
    });

  })

