// Ensure the image is in Composite mode to see all colors at once
run("Make Composite");

// Channel 1 -> Magenta & Auto B&C
Stack.setChannel(1);
run("Magenta");
run("Enhance Contrast", "saturated=0.35");

// Channel 2 -> Green & Auto B&C
Stack.setChannel(2);
run("Green");
run("Enhance Contrast", "saturated=0.35");

// Channel 3 -> Blue & Auto B&C
Stack.setChannel(3);
run("Blue");
run("Enhance Contrast", "saturated=0.35");

// Channel 4 -> Red & Auto B&C
Stack.setChannel(4);
run("Red");
run("Enhance Contrast", "saturated=0.35");

// Optional: Reset display to show all channels merged
Stack.setDisplayMode("composite");
updateDisplay();