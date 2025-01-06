// Select the Title element using jQuery
const $title = $("#Title-misaka");

// ====== RGB RGB RGB RGB RGB RGB RGB =============//
// Function to generate smooth color changes
let r = 255,
  g = 0,
  b = 0; // Start with red
let step = 0.5; // Increment value for smoothness

function rgbcolor() {
  if (r === 255 && g < 255 && b === 0) g += step; // Red to yellow
  else if (g === 255 && r > 0 && b === 0) r -= step; // Yellow to green
  else if (g === 255 && b < 255) b += step; // Green to cyan
  else if (b === 255 && g > 0) g -= step; // Cyan to blue
  else if (b === 255 && r < 255) r += step; // Blue to magenta
  else if (r === 255 && b > 0) b -= step; // Magenta to red

  // Set the new color
  $title.css("color", `rgb(${r}, ${g}, ${b})`);
}

// Use setInterval to call the function repeatedly
setInterval(rgbcolor, 10); // Adjust the interval for speed

// ====== RGB RGB RGB RGB RGB RGB RGB =============//

// jquery <3 -------- 😍😍😍😍😍😍😍😍😍😍😍😍😍

// change h1
$("h1").click(function () {
  $(this).text("balls");
});

// change only misakamikoto class
$(".misakamikoto").click(function () {
  $(this).text("I want to be shot by misaka's railgun");
});

// change misaka mikoto image

$(document).ready(function () {
  // Array of image links
  const images = [
    "https://comicvine.gamespot.com/a/uploads/original/11118/111187046/6975187-d9sjnt0xsaengjm.png%20orig.png",
    "https://s1.zerochan.net/Misaka.Mikoto.600.4061558.jpg",
    "https://i.redd.it/is-misaka-mikoto-canonically-supposed-to-be-beautiful-v0-pw9dmjng5smc1.jpg?width=850&format=pjpg&auto=webp&s=9a711f4b359071536e1a6cc69867e11e3bd16757",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1ea08e12-847b-4c43-8433-ff86b833fd7b/dfzu5df-8cb180a9-6e8f-48b4-a9e0-528c5b946806.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFlYTA4ZTEyLTg0N2ItNGM0My04NDMzLWZmODZiODMzZmQ3YlwvZGZ6dTVkZi04Y2IxODBhOS02ZThmLTQ4YjQtYTllMC01MjhjNWI5NDY4MDYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.u27Q84w-ZXVtk_fWI627h2Sqo7mbAFwszkoWVw72z-U",
  ];

  // Index to track the current image
  let currentIndex = 0;

  // Event listener for the click
  $(".misakamikotoimage").click(function () {
    // Update the image source to the next link
    $(this).attr("src", images[currentIndex]);

    // Increment the index and loop back if necessary
    currentIndex = (currentIndex + 1) % images.length;
  });
});

// change svg color
$(document).ready(function () {
  // When any SVG element with a specific class is clicked
  $(
    ".head, .weapon, .body-person, .left-leg, .right-leg, .right-hand, .left-hand"
  ).click(function () {
    const clickedElement = $(this); // Store the clicked element reference

    // Trigger the color picker
    $("#colorPicker").click();

    // Unbind any previous change events to avoid conflicts
    $("#colorPicker").off("change");

    // When a color is picked
    $("#colorPicker").change(function () {
      // Get the selected color
      const selectedColor = $(this).val();

      // Change the "fill" attribute of the clicked element
      clickedElement.attr("fill", selectedColor);
    });
  });
});
