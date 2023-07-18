window.addEventListener('resize', adjustFontSize);

function adjustFontSize() {
  var containers = [
    { id: 'responsive-text1', textClass: 'main-text1', initialFontSize: 30 },
    { id: 'responsive-text2', textClass: 'main-text2', initialFontSize: 70 },
    { id: 'responsive-text3', textClass: 'sub-text', initialFontSize: 15 }
    // Add more containers with their respective ID, text class, and initial font size as needed
  ];

  containers.forEach(function(container) {
    var containerElement = document.getElementById(container.id);
    var textElement = containerElement.querySelector('.' + container.textClass);
    var containerWidth = containerElement.offsetWidth;
    var maxWidth = containerWidth * 0.9; // Adjust this value as needed
    var maxFontSize = 32; // Adjust this value as the maximum font size you desire

    var fontSize = Math.min(container.initialFontSize, maxFontSize); // Set initial font size

    // Reduce font size until it fits within the container width or reaches the maximum font size
    while (textElement.offsetWidth > maxWidth && fontSize > 0 && fontSize < maxFontSize) {
      fontSize--;
      textElement.style.fontSize = fontSize + 'px';
    }
  });
}

adjustFontSize(); // Run initially
