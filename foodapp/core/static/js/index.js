const add = () =>{
    const quantityElement = document.getElementById('quantity');
    const increaseButton = document.getElementById('plus');

    // Initialize quantity
    let quantity = 0;

    // Add click event listener to the button
    increaseButton.addEventListener('click', () => {
    // Increment the quantity
    quantity++;
    
    // Update the quantity displayed in the HTML
    quantityElement.textContent = quantity;

    })
}  