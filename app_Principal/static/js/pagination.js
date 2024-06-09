const form_change = (clickedButton, groupToShow) => {
  const buttons = document.querySelectorAll(".btn-pag");
  buttons.forEach((button) => button.classList.remove("active"));
  clickedButton.classList.add("active");

  const group = document.querySelectorAll(".group");
  group.forEach((group) => group.classList.remove("active-group"));
  document.getElementById(groupToShow).classList.add("active-group");

  console.log(groupToShow);
  if (groupToShow == "second-group") {
    document.getElementById(groupToShow).classList.add("grid-templ");
  } else {
    group.forEach((group) => group.classList.remove("grid-templ"));
  }
};
