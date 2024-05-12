// Select all h2 elements within product sections
const productTitles = document.querySelectorAll('.product h2');

// Add event listeners to each h2 element
productTitles.forEach(title => {
    // Add mouseenter event listener to h2 element
    title.addEventListener('mouseenter', function() {
        // Change background color of parent product section on mouse enter
        this.parentElement.style.backgroundColor = '#ffcc00';
    });

    // Add mouseleave event listener to h2 element
    title.addEventListener('mouseleave', function() {
        // Revert background color of parent product section on mouse leave
        this.parentElement.style.backgroundColor = '';
    });
});
