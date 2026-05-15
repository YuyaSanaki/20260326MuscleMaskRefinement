// Ensure the image is in Composite mode to see all colors at once
run("Make Composite");

// Channel 1 -> Magenta
Stack.setChannel(1);
run("Magenta");

// Channel 2 -> Green
Stack.setChannel(2);
run("Green");

// Channel 3 -> Blue
Stack.setChannel(3);
run("Blue");

// Channel 4 -> Red
Stack.setChannel(4);
run("Red");

// Optional: Reset display to show all channels merged
Stack.setDisplayMode("composite");
updateDisplay();