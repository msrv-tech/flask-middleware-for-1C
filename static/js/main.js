async function addToCart(productId) {
    try {
        const response = await fetch('/api/cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product_id: productId })
        });

        const result = await response.json();

        if(response.ok) {
            console.log('Товар добавлен:', result);
            location.reload();
        } else {
            console.error('Ошибка:', result.error);
        }
    } catch (error) {
        console.error('Ошибка сети:', error);
    }
}

function removeFromCart(productId) {
    fetch(`/api/cart/${productId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.error) });
        }
        // Динамическое удаление элемента без перезагрузки
        const row = document.getElementById(`product-${productId}`);
        if (row) row.remove();

        // Обновление счетчика в шапке
        const cartCount = document.querySelector('.cart-count');
        if (cartCount) {
            const newCount = parseInt(cartCount.textContent) - 1;
            cartCount.textContent = newCount > 0 ? newCount : 0;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert(error.message);
    });
}