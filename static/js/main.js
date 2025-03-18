async function addToCart(productId) {
    const response = await fetch('/api/cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: productId })
    });

    if(response.ok) {
        location.reload(); // Обновляем страницу
    }
}

function removeFromCart(productId) {
    fetch(`/api/cart/${productId}`, { method: 'DELETE' })
        .then(() => location.reload());
}