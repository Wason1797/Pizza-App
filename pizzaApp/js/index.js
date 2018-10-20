/**
 * POST the order on /pizza
 * @param order 
 * 
 * ****************************
 * Please change '/pizza' with
 * your service endpoint below
 * ****************************
 */
function postOrder(order) {  

    formatedIngredients  ={}
    
    var orderModel = {
        "client": order.dni,
        "pizza": Number(order.size),
        "ingredients": JSON.stringify(order.ingredients).replace("[", "{").replace("]", "}")
    }    
    fetch('http://localhost:8000/order/post/', {
        method: 'POST',
        body: JSON.stringify(orderModel),
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    })
        .then(res => res.json())
        .then(res => showNotification());
}

function postClient(order) {
    var client = {
        "client_id": order.dni,
        "client_name": order.name,
        "address": order.address,
        "phone": order.phone
    };      
    fetch('http://localhost:8000/client/post/', {
        method: 'POST',
        body: JSON.stringify(client),
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    })
        .then(res => res.json())
        .then(res => showNotification());
    
}

/**
 * Get the form and submit it with fetch API
 */
let orderForm = $("#order-form");
orderForm.submit((event) => {

    let order = getOrderData();
    postClient(order)
    postOrder(order);

    event.preventDefault();
    event.currentTarget.reset();
});

/**
 * Gets the order data with JQuery
 */
function getOrderData() {
    let ingredients = [];
    $.each($("input[name='ingredients']:checked"), function (el) {
        ingredients.push($(this).val());
    });

    return {
        dni:$("input[name='dni']").val(),
        name: $("input[name='name']").val(),
        address: $("input[name='address']").val(),
        phone: $("input[name='phone']").val(),
        size: $("input[name='size']:checked").val(),
        ingredients
    }
}

/**
 * Shows a notification when the order is accepted
 */
function showNotification() {
    let orderAlert = $("#order-alert");
    orderAlert.toggle()
    setTimeout(() => orderAlert.toggle(), 5000);
}
